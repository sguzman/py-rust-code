import functools
import operator
import sys

import typing
from typing import List
from typing import Optional
from typing import Tuple

import xml
import xml.etree
import xml.etree.ElementTree


def args() -> str:
    return sys.argv[1]


@functools.cache
def indent(n: int) -> str:
    return '\t' * n


Data = Tuple[Optional[str], Optional[int], Optional[str]]


def heading(obj) -> Optional[str]:
    obj = obj.findall('*')[1]
    if obj is not None:
        return obj.text
    else:
        return None


def num(obj) -> Optional[int]:
    obj = obj.findall('*')[0]
    if obj is not None:
        return obj.attrib.get('value')
    else:
        return None


def section(obj) -> Data:
    return (
        obj.attrib.get('identifier'),
        num(obj),
        heading(obj)
    )


def strip_tag(s: str) -> str:
    s = s.lstrip('{http://xml.house.gov/schemas/uslm/1.0')
    return s.lstrip('}')


def dive(root, n=0, in_section=False) -> None:
    tag = strip_tag(root.tag)

    if in_section:
        sec = section(root)

        print(sec)

    for child in root.findall('*'):
        tag = strip_tag(child.tag)
        dive(child, n + 1, tag == 'section')


def main() -> None:
    xml_filename: str = sys.argv[1]
    tree = xml.etree.ElementTree.parse(xml_filename)
    root = tree.getroot()

    dive(root)


if __name__ == '__main__':
    main()
