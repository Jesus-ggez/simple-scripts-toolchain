from _py_fastapi_init import (
    conf_sqlite_pyseto,
    schema_shared,
    argon_content,
    main_fastapi,
    schema_core,
    dotenv,
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
    __create_file(name='.env', content=dotenv)


def __create_schema_package() -> None:
    __create_dir_and_enter(name='schemas')
    __create_file(name='shared.py', content=schema_shared)
    __create_file_and_exit(name='core.py', content=schema_core)


def __create_api_package() -> None:
    __create_dir_and_enter(name='api')
    __create_file_and_exit(name='exc.py', content=exc)


def main() -> None:
    # remove security for simplification fold-struct
    __create_schema_package()
    __create_security()
    __create_tools_package()
    __create_root_files()

    __create_api_package()



if __name__ == '__main__':
    main()
