from urllib import request
import contextlib
import os


def get_url_resource(url, decoding='utf-8'):
    """
    Fetch a url resource.

    Args:
        url: location of the resource.
        decoding: decode the resource to a standard (optional).
    Returns:
        A decoded resource.
    """
    with contextlib.closing(request.urlopen(url)) as response:
        result = response.read()
        return result if not decoding else result.decode(decoding)


def get_last_number(resource):
    """
    Extract the last number from a resource.

    Args:
        resource: str resource to extract the last number from.
    Returns:
        The last number from the resource, otherwise None.
    """
    numbers = [int(s) for s in resource.split() if s.isdigit()]
    if len(numbers) > 0:
        return numbers[-1]


def create_dir_run_func(directory, func=None):
    """
    Create a directory if it does not exist and execute a
    function on that directory if one is provided.

    Args:
        directory: the target directory to create and run a function on.
        func: the optional function that should take the directory
            path as the first argument.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    if func and not os.listdir(directory):
        func(directory)
