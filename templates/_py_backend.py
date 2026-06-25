template_dot_gitignore: str = """.env
"""

template_dot_env: str = """
HOST="0.0.0.0"
PORT=4000
"""

template_main: str = """

def main() -> None: ...


if __name__ == '__main__':
    main()
"""

template_config: str = """from os import environ as varenv


def __get_varenv(name: str) -> str:
    if var := varenv.get(name):
        return var

    raise NotImplementedError('any varenv doesnt exists or not implemented')
"""


template_app: str = """from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from uvicorn import run


from config import __get_varenv # type: ignore
# from api.__ import ___ as Router


type Application = FastAPI


def __run_serve(app: Application) -> None:
    return run(
        host=__get_varenv(name='HOST'),
        port=int(__get_varenv(name='PORT')),
        app=app,
    )


def create_app(app: Application) -> None:
    # app.include_router(router=Router)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )


def app() -> Application:
    app: Application = FastAPI(
        root_path='/api'
    )

    return app
"""
