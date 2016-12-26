from urllib import request
import contextlib


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
