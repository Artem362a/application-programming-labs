import argparse
import os
import re

def pars() -> str:
    """
    this function get filename
    :return:filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='path to file')
    args = parser.parse_args()
    return args.filename
def get_text(filename: str) -> str:
    """
    this function get text from filename.txt and return it
    :param:filename
    :return:data
    """
    if not os.path.exists(filename):
        raise Exception("This file does not exist")
    if not filename.endswith(".txt"):
        raise Exception("Is not a text file")
    with open(filename, "r", encoding="utf_8") as file:
        text: str = file.read()
    return text
def find_birth_day(text: str) -> int:
    """
    this function search date of birthday and count people, whose born in 21 century
    :param:text
    :return:
    """
    pattern_date = r'\d{4}'
    date = re.findall(pattern_date, text)
    counter = 0
    for birthday in date:
        if int(birthday) > 2000:
            counter += 1
    return counter
def main():
    """
    it's main =)
    """
    filename = pars()
    try:
        text = get_text(filename)
        birth_day = find_birth_day(text)
        print(birth_day)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
