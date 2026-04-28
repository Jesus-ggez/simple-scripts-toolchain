argon_content: str = """from nacl.pwhash import argon2id


def try_to_hash(v: str) -> str:
    return argon2id.str(password=v.encode()).decode()


def try_compare_hash(value: str, hashed: str) -> None:
    argon2id.verify(
        password_hash=hashed.encode(),
        password=value.encode(),
    )
#"""

package_security: str = """from .factory import create_token
from .token_so import SmartToken
from .model import *

"""

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

security_errs: str = """from fastapi import HTTPException, status


class InternalServerError(HTTPException):
    def __init__(self, reason: str) -> None:
        print('Internal err: ', reason)
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='internal server error',
        )


class TokenException(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message,
        )


class InvalidTokenType(TokenException):
    def __init__(self, trace: str) -> None:
        print('InvalidTokenType: ', trace)
        super().__init__(
            message='invalid token',
        )


class InvalidTokenPayload(TokenException):
    def __init__(self) -> None:
        super().__init__(
            message='invalid payload',
        )


class InvalidRole(HTTPException):
    def __init__(self, trace: str) -> None:
        print(f'token with invalid role detected: {trace}')
        print('call protocol-5')

        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='internal server error',
        )



\"\"\"
class (HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status,
            detail='',
        )
#\"\"\"
"""


from secrets import token_bytes
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


smart_object_token: str = """from typing import Annotated, Optional, Self
from uuid import uuid4
import json


from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, ValidationError
from pyseto import DecryptError, encode, decode
from fastapi import Depends


from .utils import minutes
from .errs import (
    InvalidTokenPayload,
    InternalServerError,
    InvalidTokenType,
)


import config


sec_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(
    # refreshUrl='/auth/refresh',
    tokenUrl='/auth/token',
)


class SmartToken(BaseModel):
    iden: Optional[str] = None
    lifetime: int = minutes(t=15)
    user_id: str

    def into_token(self) -> str:
        self.iden = str(uuid4())
        try:
            return encode(
                payload=self.model_dump(exclude={'lifetime', }),
                exp=self.lifetime,
                key=config.PASITA,
            ).decode()

        except Exception as e:
            raise InternalServerError(reason=str(e))


    @classmethod
    def from_dict(cls, data: dict) -> Self:
        try:
            return cls(**data)

        except Exception as e:
            if isinstance(e, ValidationError):
                raise InvalidTokenType( trace=str(e) )
            raise InvalidTokenPayload()


    @classmethod
    def extractor(
        cls,
        token: Annotated[str, Depends(dependency=sec_scheme)],
    ) -> Self:
        try:
            data: dict = decode(
                keys=config.PASITA,
                deserializer=json,
                token=token,
            ).payload # type: ignore

            return cls.from_dict(data=data)

        except DecryptError:
            raise InternalServerError( reason='token key are invalid' )
"""

token_factory: str = """from typing import Callable, Optional

from .token_so import SmartToken
from .errs import InvalidRole
from . import model


__get_cls: Callable[[str], Optional[type]] = model.__dict__.get

__cls_types: dict[str, type] = {}

@lambda _: _()
def __() -> None:
    for cls_name in dir(model):
        if cls_name.startswith('__'):
            continue

        if not ( obj := __get_cls(cls_name) ):
            continue

        name: str = cls_name.replace('Token', '').lower()
        __cls_types[name] = obj


def create_token(role: str, iden: str, name: str) -> SmartToken:
    if token := __cls_types.get(role):
        return token(role=role, user_id=iden, name=name)

    raise InvalidRole(trace=role)

"""

utils: str = """def minutes(t: int) -> int: return t * 60
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

