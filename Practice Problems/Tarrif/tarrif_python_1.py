
def valid_response(text_box: str) -> bool:
    accepted = ".ABCDEU"

    # Check for illegal replacement character in original
    if "." in text_box:
        return False

    # Remove whitespace, A* to replacement character
    text_box = text_box.replace("A*", ".").replace(" ", "")

    # Too many grades
    if len(text_box) > 4:
        return False

    for char in text_box:
        # Check for non-legal character
        if char not in accepted:
            return False

    return True

