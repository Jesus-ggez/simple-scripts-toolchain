from sys import argv as term_args


from utils import (
    __create_dir_and_enter,
    __create_file_and_exit,
)


def main() -> None:
    for dirname in term_args[1:]:
        __create_dir_and_enter(name=dirname)
        __create_file_and_exit(name='__init__.py', content='')


if __name__ == '__main__':
    main()
