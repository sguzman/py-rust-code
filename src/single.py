import bs4
import functools
import sys

import xml
import xml.etree
import xml.etree.ElementTree


def main() -> None:
    xml_filename: str = sys.argv[1]
    tree = xml.etree.ElementTree.parse(xml_filename)
    root = tree.getroot()

    for s in root.findall('/main'):
        print(s)


if __name__ == '__main__':
    main()
