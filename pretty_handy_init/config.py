from dataclasses import dataclass


@dataclass
class Config:
    LOGO = 'Pretty Handy , Init ?'
    LOGO_FONT = 'roman'
    COLOR = 'green'
    LANGUAGE_PROMPT = (
        '\nPlease select a programming language for you project from the '
        'following options (Use the numbers to select option):'
    )
    PROJECT_TYPE_PROMPT = (
        '\nPlease select the type of your programming project from the '
        'following options (Use the numbers to select option):'
    )
    PROJECT_VISIBILITY_PROMPT = (
        '\nPlease select the visibility of your project on GitHub from the '
        'following options (Use the numbers to select option):'
    )
    PROJECT_NAME_PROMPT = '\nProject Name: '
