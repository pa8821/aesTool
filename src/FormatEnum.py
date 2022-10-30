import enum

class Format(enum.Enum):
    hexadecimal = 0
    ascii = 1

class CipherMode(enum.Enum):
    ECB = 0
    CBC = 1