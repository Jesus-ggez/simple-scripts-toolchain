from _py_ini_templates import (
    smart_object_token,
    conf_sqlite_pyseto,
    security_errs,
    main_fastapi,
)
from utils import (
    __create_dir_and_enter,
    __create_file,
    __create_dir,
)


def __create_security_package() -> None:
    __create_dir_and_enter(name='security')
    __create_file(name='token_so.py', content=smart_object_token)
    __create_file(name='errs.py', content=security_errs)


def __create_root_files() -> None:
    __create_file(name='config.py', content=conf_sqlite_pyseto)
    __create_file(name='main.py', content=main_fastapi)


def main() -> None:
    __create_root_files()

    __create_dir('tools')
    __create_dir('api')

    __create_security_package()

if __name__ == '__main__':
    main()
