import re


def find_number(text):
    num = re.findall(r'[0-9]+',text)
    return " ".join(num)
