import os
from typing import Optional

from pretty_handy_init.enums.visibility import Visibility
from pretty_handy_init.project_setup.project import Project


class PythonProject(Project):

    """Represents a Python Project Setup object."""

    def __init__(
        self,
        default_project_files_folder: str,
        project_name: Optional[str] = None,
        project_visibility: Visibility = Visibility.PRIVATE,
    ) -> None:
        """Initializes the Python Project Class.

        Args:
            default_project_files_folder (str): Default Project files folder
                path.
            project_name (Optional[str]): Name of the Project. Defaults to
                None.
            project_visibility (Visibility): Project GitHub Repo Visibility.
                Defaults to Private.
        """
        super().__init__(
            default_project_files_folder=default_project_files_folder,
            project_name=project_name,
            project_visibility=project_visibility,
        )
        self._package_name = self._project_name_snake.lower()

    @staticmethod
    def _create_folder_with_init_file(
        destination_folder_path: str, folder_name: str
    ) -> None:
        """Creates folder with __init__.py file in it.

        Args:
            destination_folder_path (str): Folder to modify.
            folder_name (str): New folder name.
        """
        folder = os.path.join(destination_folder_path, folder_name)
        os.makedirs(folder, exist_ok=True)
        open(os.path.join(folder, '__init__.py'), 'w')

    def _create_python_package(self) -> None:
        """Creates Python package."""
        self._create_folder_with_init_file(
            destination_folder_path=self._project_folder,
            folder_name=self._package_name,
        )

    def _create_test_folder(self) -> None:
        """Creates test folder."""
        self._create_folder_with_init_file(
            destination_folder_path=self._project_folder, folder_name='test'
        )

    def _setup_virtual_environment(self) -> None:
        """Creates virtual environment."""
        venv_path = os.path.join(self._project_folder, 'venv')
        os.system(f'python -m venv {venv_path}')
        open(os.path.join(self._project_folder, 'requirements.txt'), 'w')

    def setup_python_project(self) -> None:
        """Sets up Python project."""
        # Create the project folder
        self._create_project_folder()

        # Create the Python package
        self._create_python_package()

        # Create the test folder
        self._create_test_folder()

        # Copy default project files
        self._copy_default_project_files()

        # Setup Python Virtual Environment
        self._setup_virtual_environment()

        # Create default README.md file
        self._create_readme()

        # Push project to GitHub
        self._git_connector.push_project_to_github(
            project_name=self._project_name_snake,
            project_visibility=self._project_visibility,
        )

        # Update README.md
        self._update_readme()
