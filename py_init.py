from _py_ini_templates import (
    smart_object_token,
    conf_sqlite_pyseto,
    token_extractor,
    security_errs,
    main_fastapi,
)
from utils import (
    __create_dir_and_enter,
    __create_file,
    __create_dir,
    __move_back,
)


def main() -> None:
    __create_file(name='config.py', content=conf_sqlite_pyseto)
    __create_file(name='main.py', content=main_fastapi)

    # src
    __create_dir_and_enter(name='src')

    # src/tools/
    __create_dir('tools')

    # src/models/
    __create_dir('models')

    # src/queries/
    __create_dir('queries')
    __move_back()


    # api/
    __create_dir_and_enter('api')

    # api/security
    __create_dir_and_enter('security')
    __create_file(name='token_so.py', content=smart_object_token)
    __create_file(name='extractor.py', content=token_extractor)
    __create_file(name='errs.py', content=security_errs)


if __name__ == '__main__':
    main()
