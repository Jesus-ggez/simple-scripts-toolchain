from sys import argv as term_args

from utils import (
    __create_dir_and_enter,
    __create_file,
    __create_dir,
    __move_back,
    __main__,
)


@__main__
def main() -> None:
    for package_name in term_args[1:]:
        __create_dir_and_enter(name=package_name)
        __create_dir(path='dto')

        named: str = package_name.title()

        for stereotype in (
            'Controller',
            'Repository',
            'Service',
            'Entity',
        ): __create_file(name=named + stereotype + '.java', content='')
        __move_back()
