from _py_fastapi_init import (
    conf_sqlite_pyseto,
    argon_content,
    main_fastapi,
    exc,
)
from utils import (
    __create_dir_and_enter,
    __create_file_and_exit,
    __create_file,
    __move_back
)


def __create_security() -> None:
    __create_dir_and_enter(name='security')
    __create_file_and_exit(name='core.py', content='')


def __create_tools_package() -> None:
    __create_dir_and_enter(name='tools')

    # tools/hashing
    __create_dir_and_enter(name='hashing')
    __create_file_and_exit(name='argon.py', content=argon_content)

    # tools/time
    __create_dir_and_enter(name='date')
    __create_file_and_exit(name='unix.py', content='')

    __move_back() # exit to tools


def __create_root_files() -> None:
    __create_file(name='config.py', content=conf_sqlite_pyseto)
    __create_file(name='main.py', content=main_fastapi)


def __create_api_package() -> None:
    __create_dir_and_enter(name='api')
    __create_file_and_exit(name='exc.py', content=exc)


def main() -> None:
    # remove security for simplification fold-struct
    __create_security()
    __create_tools_package()
    __create_root_files()

    __create_api_package()



if __name__ == '__main__':
    main()
