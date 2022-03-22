"""My dictionary functions."""

__author__ = "730482406"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert the input."""
    result: dict[str, str] = {}
    for key in a:
        result[a[key]] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Prints most present color in dictionary or if tied, prints first."""
    new_dict: dict[str, int] = {}
    give: str = ""
    i: int = 0
    for key in b:
        if b[key] in new_dict:
            new_dict[b[key]] += 1
        else:
            new_dict[b[key]] = 1
    for key in new_dict:
        if i < new_dict[key]:
            i = new_dict[key]
            give = key
    return give
    

def count(c: list[str]) -> dict[str, int]:
    """Returns a dictionary of a list of integers and a corresponding number of how many times that value appeared in the input list."""
    build_up: dict[str, int] = {}
    for key in c:
        if not (key in build_up):
            build_up[key] = 1
        else:
            build_up[key] = build_up[key] + 1
    return build_up


print(count(['4', '3', '4', '5']))