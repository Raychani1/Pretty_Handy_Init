import argparse
import os
from argparse import Namespace
from typing import List

from termcolor import cprint

from pretty_handy_init.cli_app.cli_utils import (
    display_logo,
    get_user_choice,
    print_choices,
)
from pretty_handy_init.config import Config
from pretty_handy_init.enums.language import Language
from pretty_handy_init.enums.project_type import ProjectType
from pretty_handy_init.enums.visibility import Visibility
from pretty_handy_init.project_setup.python_project import PythonProject


class CliApp:

    """Represents the 'Pretty Handy, Init?' Command Line Application itself."""

    def __init__(self, cli_args: List[str]) -> None:
        """Initializes the CLI App Class.

        Args:
            cli_args (List[str]): Passed command line arguments.
        """
        self._cli_args = cli_args
        self._parser = self._setup_argparse()
        self._supported_languages = list(Language)
        self._supported_project_types = list(ProjectType)
        self._supported_project_visibilities = list(Visibility)

    def _setup_argparse(self) -> argparse.ArgumentParser:
        """Initial setup of Argument Parser.

        Returns:
            argparse.ArgumentParser: Finished Argument Parser.
        """
        parser = argparse.ArgumentParser(prog='pretty_handy_init')
        parser.add_argument(
            '-l',
            '--language',
            nargs='?',
            type=lambda language: Language[language.upper()],
            choices=Language,
            default='python',
            help='Programming language used for the project',
            required=False,
        )
        parser.add_argument(
            '-t',
            '--type',
            nargs='?',
            type=lambda language: ProjectType[language.upper()],
            choices=ProjectType,
            default='cli',
            help='Type of programming project',
            required=False,
        )
        parser.add_argument(
            '-v',
            '--visibility',
            nargs='?',
            type=lambda language: Visibility[language.upper()],
            choices=Visibility,
            default='private',
            help='GitHub Repository Visibility',
            required=False,
        )
        parser.add_argument(
            '-n',
            '--name',
            type=str,
            help='Type of programming project',
            required=True,
        )

        return parser

    def _select_programming_language(self) -> Language:
        """Prompts the user to select the programming language for the project.

        Returns:
            Language: Selected programming language.
        """
        cprint(Config.LANGUAGE_PROMPT, Config.COLOR)
        print_choices(choices=self._supported_languages, format_method='title')

        default_value = self._supported_languages[0].value

        return Language(
            get_user_choice(
                prompt=f'Language [{default_value.title()}]: ',
                choices=self._supported_languages,
            )
        )

    def _select_project_type(self) -> ProjectType:
        """Prompts the user to select the project type.

        Returns:
            ProjectType: Selected project type.
        """
        cprint(Config.PROJECT_TYPE_PROMPT, Config.COLOR)
        print_choices(
            choices=self._supported_project_types, format_method='upper'
        )

        default_value = self._supported_project_types[0].value

        return ProjectType(
            get_user_choice(
                prompt=f'Project Type  [{default_value.upper()}]: ',
                choices=self._supported_project_types,
            )
        )

    def _select_project_visibility(self) -> Visibility:
        """Prompts the user to select the visibility of the GitHub repository.

        Returns:
            Visibility: Selected GitHub repository visibility.
        """
        cprint(Config.PROJECT_VISIBILITY_PROMPT, Config.COLOR)
        print_choices(
            choices=self._supported_project_visibilities, format_method='title'
        )

        default_value = self._supported_project_visibilities[0].value

        return Visibility(
            get_user_choice(
                prompt=f'Project Visibility [{default_value.title()}]: ',
                choices=self._supported_project_visibilities,
            )
        )

    @staticmethod
    def _run_setup(project_params: Namespace) -> None:
        """Executes project setup based on parameters.

        Args:
            project_params (Namespace): Project setup parameters.
        """
        if project_params.language == Language.PYTHON:
            python_default_files_folder = os.path.join(
                os.getcwd(), 'resources', 'python'
            )

            project = PythonProject(
                default_project_files_folder=python_default_files_folder,
                project_name=project_params.name,
                project_visibility=project_params.visibility,
            )
            project.setup_python_project()

    def __call__(self) -> None:
        """Makes the CLI App Class callable."""
        display_logo()

        if self._cli_args:
            project_params = self._parser.parse_args(self._cli_args)
        else:
            project_params = Namespace(
                language=self._select_programming_language(),
                type=self._select_project_type(),
                visibility=self._select_project_visibility(),
                name=None,
            )

        self._run_setup(project_params=project_params)
