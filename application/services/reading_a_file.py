from application.services.config import FILES_INPUT_DIR
import os


def get_file_string(name: str = "text.txt"):
    txt_file = os.path.join(FILES_INPUT_DIR, name)

    if os.path.exists(txt_file):
        with open(txt_file) as text_file:
            lines = text_file.readlines()

        return "<br>".join(lines)
    else:
        raise FileNotFoundError(f"File not found: {txt_file}")
