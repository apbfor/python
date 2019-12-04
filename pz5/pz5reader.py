"""Read files"""
from abc import ABC, abstractmethod
import json
import xml
import xml.etree.ElementTree as elemTree


class Reader(ABC):
    """Abstract class"""

    @abstractmethod
    def read(self, filename):
        pass


class ReaderJson(Reader):
    """Read JSON files"""
    def read(self, filename):
        """Read method"""
        try:
            with open(filename, "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            print("File was not found!")
            exit(1)
        except json.decoder.JSONDecodeError:
            print("Invalid syntax in file!")
            exit(1)
        return data


class ReaderXml(Reader):
    """Read XML files"""
    def read(self, filename):
        """Read method"""
        try:
            tree = elemTree.parse(filename)
        except FileNotFoundError:
            print("File was not found!")
            exit(1)
        except xml.elemTree.ElementTree.ParseError:
            print("Invalid syntax in file!")
            exit(1)

        root = tree.getroot()
        return root


class ReaderIhl:
    """Iterator"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result


def main():
    read_j = ReaderJson()
    buf = read_j.read("file.json")
    print(buf)

    read_x = ReaderXml()
    buf = read_x.read("file.xml")

    print(buf.tag)

    length = len(buf)
    for i in range(length):
        print(buf[i].tag + ': ' + buf[i].text)

    for num in ReaderIhl(1, 5):
        print(num)


if __name__ == "__main__":
    main()

