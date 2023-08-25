from typing import Callable


def get_formatting_method(format_method_name: str) -> Callable:
    """Fetches string formatting method based on method name.

    Args:
        format_method_name (str): Name of formatting method.

    Raises:
        AttributeError: Error raised in case method does not exist.

    Returns:
        Callable: Found string formatting method.
    """
    if not hasattr(str, format_method_name):
        raise AttributeError(
            f"'{format_method_name}' is not a valid string method."
        )

    return getattr(str, format_method_name)
