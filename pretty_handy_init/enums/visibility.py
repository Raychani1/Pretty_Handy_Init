from enum import Enum


class Visibility(Enum):

    """Represents the Enumeration of supported GitHub Repo Visibilities."""

    PRIVATE = 'private'
    PUBLIC = 'public'

    def __str__(self):
        return self.value
