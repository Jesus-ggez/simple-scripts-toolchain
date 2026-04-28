from sys import argv as term_args


from _py_pkg_router import init_router
from _py_fastapi_init import exc
from utils import (
    __create_dir_and_enter,
    __create_file_and_exit,
    __create_file,
)


def main() -> None:
    for router_name in term_args[1:]:
        __create_dir_and_enter(name=router_name)

        __create_file(name='exc.py', content=exc)

        ctt: str = init_router.replace('__name__', router_name)
        __create_file_and_exit(name='__init__.py', content=ctt)


if __name__ == '__main__':
    main()
