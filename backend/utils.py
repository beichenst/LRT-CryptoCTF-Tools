"""通用小工具"""
import string

def is_printable(s: str) -> bool:
    return all(c in string.printable for c in s)