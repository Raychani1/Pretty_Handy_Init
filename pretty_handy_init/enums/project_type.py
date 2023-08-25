from enum import Enum


class ProjectType(Enum):

    """Represents the Enumeration of supported project types."""

    CLI = 'cli'

    def __str__(self):
        return self.value
