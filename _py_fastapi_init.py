from base64 import b64encode as encode
from secrets import token_bytes


gitignore: str = """.env
"""


schema_core: str = """def create_table(name: str, cols: list[str]) -> str:
    return (
        'CREATE TABLE IF NOT EXISTS ' + name + ' (\\n' +
        ',\\n'.join(f'    {col}' for col in cols) +
        '\\n)'
    )


def create_fk(name: str, col_ref: str, table_ref: str) -> str:
    return f'{ name } TEXT REFERENCES { table_ref }({ col_ref })'
"""

schema_shared: str = """from typing import Final


# this field is for unix standar
CREATED_AT: Final[str] = 'created_at INTEGER NOT NULL'
IDEN: Final[str] = 'id TEXT NOT NULL PRIMARY KEY'
"""


argon_content: str = """from nacl.pwhash import argon2id


def try_to_hash(v: str) -> str:
    return argon2id.str(password=v.encode()).decode()


def try_compare_hash(value: str, hashed: str) -> None:
    argon2id.verify(
        password_hash=hashed.encode(),
        password=value.encode(),
    )
#"""

main_fastapi: str = """from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()


# from api. import router as Router


app: FastAPI = FastAPI()


def main() -> None:
    # app.include_router(router=Router)
    ...



if __name__ == '__main__':
    from config import create_tables

    create_tables()
    main()

    from uvicorn import run

    run(
        host='0.0.0.0',
        port=4000,
        app=app,
    )
"""

create_new_token_bytes = lambda: token_bytes(
    nbytes=32,
)

dotenv: str = f"""
BEARER_TOKEN_KEY=\"{ encode(create_new_token_bytes()).decode() }\"
"""

conf_sqlite_pyseto: str = """from sqlite3 import Connection, connect
from os import environ as varenv


from pyseto import Key, KeyInterface


def __get_varenv(name: str) -> str:
    if var := varenv.get(name):
        return var

    raise NotImplementedError('any varenv doesnt exists or not implemented')


def __create_key(bkey: bytes) -> KeyInterface:
    return Key.new(
        purpose='local',
        version=4,
        key=bkey,
    )


# simple tokens
PASITA: KeyInterface = __create_key(bkey=__get_varenv(name='BEARER_TOKEN_KEY').encode())


def create_pool() -> Connection:
    return connect('zample.db')


def create_tables() -> None:
    # from schemas import *

    _pool: Connection = create_pool()
    for table in (
    ):
        _pool.execute(table)
        _pool.commit()

    _pool.close()
"""




unix_time: str = """from datetime import datetime


def unix_now() -> int:
    return int( datetime.now().timestamp() )

"""


exc: str = """from fastapi import HTTPException, status

class InternalServerExc(HTTPException):
    def __init__(self, trace: str) -> None:
        print('trace: ', trace)

        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='internal server error',
        )
"""

