import os

from pretty_handy_init.enums.visibility import Visibility


class GitConnector:

    """Class responsible for communication with Git Version Control."""

    def __init__(self, project_folder: str) -> None:
        """Initializes the Git Connector Class.

        Args:
            project_folder (str): Local Project folder to version control.
        """
        self._github_username = os.getenv('GITHUB_USERNAME', 'username')
        self._github_email = os.getenv('GITHUB_EMAIL', 'example@email.com')
        self._github_access_token = os.getenv(
            'GITHUB_ACCESS_TOKEN', 'access_token'
        )
        self._project_folder = project_folder

        self._configure_git()

    @staticmethod
    def _configure_variable(variable: str, value: str) -> None:
        """Configures `variable` if the `value` is not what provided.

        Args:
            variable (str): Variable to modify.
            value (str): Value to check for match.
        """
        if os.popen(f'git config --global --get {variable}').read() != value:
            os.system(f'git config --global {variable} "{value}"')

    def _configure_git(self) -> None:
        """Configures Git username and email."""
        self._configure_variable('user.email', self._github_email)
        self._configure_variable('user.name', self._github_username)

    def _github_repo_does_not_exist(
        self, github_username: str, github_repo_name: str
    ) -> bool:
        """Checks if user has the given repository.

        Args:
            github_username (str): Name of GitHub user.
            github_repo_name (str): Name of GitHub repository.

        Returns:
            bool: Existence of GitHub repository.
        """
        return (
            '"message": "Not Found"'
            in os.popen(
                'curl -s https://api.github.com/repos'
                f'/{github_username}/{github_repo_name}'
            ).read()
        )

    def _create_github_repo(
        self,
        github_username: str,
        github_repo_name: str,
        github_repo_visibility: str,
    ) -> None:
        """Creates GitHub repository if it does not exist.

        Args:
            github_username (str): Name of GitHub user.
            github_repo_name (str): Name of GitHub repository.
            github_repo_visibility (str): Visibility of GitHub repository.
        """
        if self._github_repo_does_not_exist(
            github_username=github_username, github_repo_name=github_repo_name
        ):
            is_repo_private = (
                'true' if github_repo_visibility == 'private' else 'false'
            )

            data = (
                f'{{"name":"{github_repo_name}", "private":{is_repo_private}}}'
            )

            curl_command = f"""
            curl -s -o /dev/null -L -X POST \
                -H "Accept: application/vnd.github+json" \
                -H "Authorization: Bearer {self._github_access_token}" \
                -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/user/repos -d '{data}'
            """

            os.system(curl_command)

    def push_project_to_github(
        self, project_name: str, project_visibility: Visibility
    ) -> None:
        """Pushes initial commit of single README.md file to GitHub.

        Args:
            project_name (str): Name of the project.
            project_visibility (Visibility): Visibility of GitHub repository.
        """
        repo_url = (
            f'https://github.com/{self._github_username}/{project_name}.git'
        )

        self._create_github_repo(
            github_username=self._github_username,
            github_repo_name=project_name,
            github_repo_visibility=project_visibility.value,
        )

        git_command = [
            f'cd {self._project_folder}',
            'git init',
            'git add README.md',
            'git commit -m "Initial commit"',
            'git branch -M main',
            f'git remote add origin {repo_url}',
            'git push -u origin main',
            'git checkout -b development',
        ]

        os.system('; '.join(git_command))
