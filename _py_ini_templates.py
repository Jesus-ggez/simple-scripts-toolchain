main_fastapi: str = """from fastapi import FastAPI


app: FastAPI = FastAPI()


def main() -> None:
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


class TokenNotFound(TokenException):
    def __init__(self) -> None:
        super().__init__(
            message='token not found',
        )

\"\"\"
class UnauthorizedError(HTTPException):
    def __init__(self) -> None:
        super().__init__(...)

#\"\"\"
"""


from secrets import token_bytes
conf_sqlite_pyseto: str = f"""from sqlite3 import Connection, connect


from pyseto import Key, KeyInterface


PASITA: KeyInterface = Key.new(
    key={ token_bytes(nbytes=32) },
    purpose='local',
    version=4,
)


def create_pool() -> Connection:
    return connect('zample.db')


def create_tables() -> None:
    _pool: Connection = create_pool()
    for table in (
    ):
        _pool.execute(table)
        _pool.commit()

    _pool.close()
"""


smart_object_token: str = """from typing import Optional, Self
import json


from pydantic import BaseModel, ValidationError
from pyseto import encode, decode
from fastapi import Security
from fastapi.security import (
    HTTPAuthorizationCredentials as AuthCredentials,
    HTTPBearer,
)


from .errs import (
    InvalidTokenPayload,
    InternalServerError,
    InvalidTokenType,
    TokenNotFound,
)


import config


sec: HTTPBearer = HTTPBearer()


class SmartToken(BaseModel):
    exp: Optional[str] = None
    lifetime: int = 15
    id: str


    def into_token(self) -> str:
        try:
            return encode(
                payload=self.model_dump(exclude={'lifetime', }),
                exp=self.lifetime * 60,
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
        credentials: AuthCredentials = Security(dependency=sec),
    ) -> Self:
        if not ( bearer := credentials.credentials ):
            raise TokenNotFound()

        data: dict = decode(
            keys=config.PASITA,
            deserializer=json,
            token=bearer,
        ).payload # type: ignore

        return cls.from_dict(data=data)
"""

