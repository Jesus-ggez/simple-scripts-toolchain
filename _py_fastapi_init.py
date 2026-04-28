from secrets import token_bytes


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


# from api._ import router as Router


app: FastAPI = FastAPI()


def main() -> None:
    # app.include_router(router=Router)
    ...



if __name__ == '__main__':
    main()

    from uvicorn import run

    run(
        host='0.0.0.0',
        port=4000,
        app=app,
    )
"""

conf_sqlite_pyseto: str = f"""from sqlite3 import Connection, connect


from pyseto import Key, KeyInterface


def __create_key(bkey: bytes) -> KeyInterface:
    return Key.new(
        purpose='local',
        version=4,
        key=bkey,
    )

# simple tokens
PASITA: KeyInterface = __create_key(bkey={ token_bytes(nbytes=32) })


def create_pool() -> Connection:
    return connect('zample.db')


def create_tables() -> None:
    _pool: Connection = create_pool()
    for table in [
    ]:
        _pool.execute(table)
        _pool.commit()

    _pool.close()
"""




unix_time: str = """from datetime import datetime


def unix_now() -> int:
    return int( datetime.now().timestamp() )

"""


exc: str = """from fastapi import HTTPException, status

class (HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.,
            detail='',
        )
"""

