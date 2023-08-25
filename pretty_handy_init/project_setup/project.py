import os
import re
import shutil
from typing import Optional

from termcolor import colored, cprint
from tqdm import tqdm

from pretty_handy_init.config import Config
from pretty_handy_init.enums.visibility import Visibility
from pretty_handy_init.git.git_connector import GitConnector


class Project:

    """Represents a Project Setup object."""

    def __init__(
        self,
        default_project_files_folder: str,
        project_name: Optional[str] = None,
        project_visibility: Visibility = Visibility.PRIVATE,
    ) -> None:
        """Initializes the Project Class.

        Args:
            default_project_files_folder (str): Default Project files folder
                path.
            project_name (Optional[str]): Name of the Project. Defaults to
                None.
            project_visibility (Visibility): Project GitHub Repo Visibility.
                Defaults to Private.
        """
        self._project_name = (
            project_name
            if project_name is not None
            else self.__get_project_name()
        )
        self._project_name_snake = self._project_name.replace(' ', '_')
        self._project_visibility = project_visibility
        self._project_docker = self._project_name_snake.lower()
        self._project_folder = os.path.join(
            'init_dir', self._project_name_snake
        )
        self._default_project_files_folder = default_project_files_folder
        self._git_connector = GitConnector(project_folder=self._project_folder)

    @staticmethod
    def __get_project_name() -> str:
        """Asks the user for the project name.

        Returns:
            str: Project name from the user.
        """
        return input(colored(Config.PROJECT_NAME_PROMPT, Config.COLOR))

    def _create_project_folder(self) -> None:
        """Creates project folder."""
        os.makedirs(self._project_folder, exist_ok=True)

    def _copy_default_project_files(self) -> None:
        """Copies default project files to destination"""
        source_folder = self._default_project_files_folder
        destination_folder = self._project_folder

        for file_name in tqdm(os.listdir(source_folder)):
            # Construct full file path
            source = os.path.join(source_folder, file_name)
            destination = os.path.join(destination_folder, file_name)

            # Copy only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                cprint(f'Copied {file_name}', Config.COLOR)

    def _create_readme(self) -> None:
        """Creates default README.md file."""
        os.system(
            f"echo \"# {self._project_name}\" > "
            f"{os.path.join(self._project_folder, 'README.md')}"
        )

    def _update_readme(self) -> None:
        """Updates existing project README.md file based on template."""
        input_readme_path = os.path.join(
            os.getcwd(), 'resources', 'readme', 'README.md'
        )
        output_readme_path = os.path.join(self._project_folder, 'README.md')

        replacement_mapping = {
            '<user>': self._git_connector._github_username,
            '<repo>': self._project_name_snake,
            '<dockerhub_username>': os.getenv(
                'DOCKERHUB_USERNAME', 'dockerhub_username'
            ),
            '<docker_image_tag>': self._project_docker,
            '<docker_image_container>': f'{self._project_docker}_container',
        }

        with open(input_readme_path, 'r') as input_readme:
            lines = input_readme.readlines()

            for pattern, value in replacement_mapping.items():
                lines = [re.sub(pattern, value, line) for line in lines]

            with open(output_readme_path, 'a') as output_readme:
                output_readme.writelines(lines)
