template_date_unix: str = """from datetime import datetime


def get_now() -> int:
    return int( datetime.now().timestamp() )
"""

template_date_iso: str = """from datetime import datetime


def get_now() -> str:
    return datetime.now().isoformat()
"""

template_hash_argon2id: str = """from nacl.pwhash import argon2id


def to_hash_or_raises(value: str) -> str:
    return argon2id.str(
        password=value.encode(encoding='utf-8')
    ).decode('utf-8')


def veryfy_or_raises(password: str, hashed: str) -> None:
    # raises InvalidkeyError if password and hashed are not equals
    argon2id.verify(
        password_hash=hashed.encode(),
        password=password.encode(),
    )
"""

template_regex_builder: str = """from typing import Self


class Regex:

    def __init__(self) -> None:
        self.__regex: set[str] = set()


    def __str__(self) -> str:
        value: str = ''.join(self.__regex)

        return value if not value else r'^{}.*$'.format(value)


    def __repr__(self) -> str:
        return f'Regex(value={str(self)})'


    def at_least_one_upper(self) -> Self:
        self.__regex.add( r'(?=.*[A-Z])' )
        return self


    def at_least_one_lower(self) -> Self:
        self.__regex.add( r'(?=.*[a-z])' )
        return self


    def at_least_one_digit(self) -> Self:
        self.__regex.add( r'(?=.*\\d)' )
        return self


    def at_least_one_symbol(self) -> Self:
        self.__regex.add( r'(?=.*[@$!%?&])' )
        return self


    def at_least_one_alpha(self) -> Self:
        self.__regex.add( r'(?=.*[A-Za-z])' )
        return self

    def matches(self, val: str) -> bool:
        import re

        return bool( re.match(self.__str__(), val) )
"""


