from enum import Enum


class Language(Enum):

    """Represents the Enumeration of supported languages."""

    PYTHON = 'python'

    def __str__(self):
        return self.value
