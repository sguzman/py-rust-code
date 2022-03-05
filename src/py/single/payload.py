import untangle

from file_to_text import exec as ft
from slurp import exec as slp
from arg import exec as arg
from compose import exec as cmp

def exec() -> None:
    a = arg()
    text = ft(a)
    obj = untangle.parse(text)
    print(obj.uscDoc.main)
