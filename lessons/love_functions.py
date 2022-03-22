def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    count_some: int = 0

    while count_some < n:
        love_note += love_note + love(to) + "\n"
        count_some += 1
    return love_note