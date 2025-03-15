import re
import unicodedata
from urllib.parse import urlparse


def convert_str_keep_alphanumeric(text_str) -> str:
    pattern = r"[^0-9a-zA-Z_\-\s]+"

    return re.sub(pattern, "", text_str)


def convert_str_to_snake_case(text_str):
    """converts 'snake_case_str' to 'snakeCaseStr'"""

    return text_str.replace(" ", "_").lower()


def convert_str_remove_accents(text_str: str) -> str:
    return "".join(
        c
        for c in unicodedata.normalize("NFD", text_str)
        if unicodedata.category(c) != "Mn"
    )


def convert_str_file_name(text_str: str) -> str:
    """convert strings to clean file name or url"""

    return convert_str_keep_alphanumeric(
        convert_str_to_snake_case(convert_str_remove_accents(text_str))
    )


def convert_url_file_name(text_str: str) -> str:
    """convert strings to clean file name or url"""

    o = list(urlparse(text_str))

    o[1] = o[1].replace("www.", "").replace(".", "_")

    o[2] = o[2][1:].replace("/", "_")

    if o[2] == "":
        o[2] = "index"

    print("o2", o[2])

    o = [convert_str_file_name(val) for val in o[1:3]]

    path = "/".join(list(o))
    if path.startswith("_"):
        path = path[1:]

    if path.endswith("_"):
        path = path[:-1]

    return path
