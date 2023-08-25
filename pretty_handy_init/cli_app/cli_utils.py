from typing import List, Union

from pyfiglet import figlet_format
from termcolor import colored, cprint

from pretty_handy_init.config import Config
from pretty_handy_init.enums.language import Language
from pretty_handy_init.enums.project_type import ProjectType
from pretty_handy_init.enums.visibility import Visibility
from pretty_handy_init.utils import get_formatting_method


def display_logo() -> None:
    """Displays App Logo."""
    cprint(figlet_format(Config.LOGO, font=Config.LOGO_FONT), Config.COLOR)


def print_choices(
    choices: Union[List[Language], List[ProjectType], List[Visibility]],
    default_value: int = 0,
    format_method: str = 'upper',
) -> None:
    """Prints choices for user.

    Args:
        choices (Union[List[Language], List[ProjectType], List[Visibility]]):
            Available choices.
        default_value (int): Default selected value. Defaults to 0.
        format_method (str): Name of option string formatting method.
            Defaults to 'upper'.
    """
    format_str = get_formatting_method(format_method_name=format_method)

    for choice_index, choice_value in enumerate(choices):
        if choice_index == default_value:
            print(f'[{choice_index}] - {format_str(choice_value.value)}')
        else:
            print(f'{choice_index} - {format_str(choice_value.value)}')

    print()


def get_user_choice(
    prompt: str,
    choices: Union[List[Language], List[ProjectType], List[Visibility]],
    default: int = 0,
) -> Union[Language, ProjectType, Visibility]:
    """Prompts the user for input.

    Args:
        prompt (str): Prompt to display before decision making for context.
        choices (Union[List[Language], List[ProjectType], List[Visibility]]):
            Available choices.
        default (int): Default selected value. Defaults to 0.

    Returns:
        Union[Language, ProjectType, Visibility]: Final selected value.
    """
    user_choice = None

    try:
        user_choice = int(input(colored(prompt, Config.COLOR)))
    except ValueError:
        user_choice = default
    finally:
        if user_choice not in list(range(len(choices))):
            user_choice = default

    return choices[user_choice]
