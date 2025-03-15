import os
from frontmatter import Frontmatter
import shutil


def upsert_folder(folder_path: str, debug_prn: bool = False, replace_folder=False):

    folder_path = os.path.dirname(folder_path)

    if replace_folder and os.path.exists(folder_path) and os.path.isdir(folder_path):
        folder_path = os.path.join(folder_path, "")
        shutil.rmtree(folder_path)

    if debug_prn:
        print(
            {
                "upsert_folder": os.path.abspath(folder_path),
                "is_exist": os.path.exists(folder_path),
            }
        )

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def read_md_from_disk(file_path):
    data = Frontmatter.read_file(file_path)

    return data["body"], data["attributes"]
