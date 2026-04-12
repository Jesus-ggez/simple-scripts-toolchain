import os


from typing import Callable


__create_dir: Callable = os.mkdir
__move_to: Callable = os.chdir
__exec: Callable = os.system

__move_back: Callable = lambda: __move_to('..')


def __create_dir_and_enter(name: str) -> None:
    __create_dir(name)
    __move_to(name)


def __create_file(name: str, content: str) -> None:
    with open(name, 'w') as doc:
        doc.write(content)


def __create_file_and_exit(name: str, content: str) -> None:
    __create_file(name=name, content=content)
    __move_back()
