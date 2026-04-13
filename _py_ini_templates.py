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


from pydantic import BaseModel, ValidationError
from pyseto import encode


from .errs import (
    InvalidTokenPayload,
    InternalServerError,
    InvalidTokenType,
)


import config


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
                raise InvalidTokenType(
                    trace=str(e),
                )

            raise InvalidTokenPayload()

"""


token_extractor: str = """from typing import Callable
import json


from fastapi import Security
from pyseto import decode
from fastapi.security import (
    HTTPAuthorizationCredentials as AuthCredentials,
    HTTPBearer,
)


from .errs import TokenNotFound
from .token_so import SmartToken
import config


sec: HTTPBearer = HTTPBearer()


def token_extractor(
    token: type[SmartToken],
) -> Callable[[AuthCredentials], SmartToken]:
    \"\"\"
    Use:

    @router.method('/')
    def sampled(
        form: Form,
        pool: Connection = Depends(dependency=create_pool),
        token: TokenType = Depends(
            dependency=token_extractor(TokenType),
        ),
    ) -> dict:
        credential: TokenType = token # only use
    \"\"\"
    def extractor(
        credentials: AuthCredentials = Security(dependency=sec),
    ) -> SmartToken:

        if not ( bearer := credentials.credentials ):
            raise TokenNotFound()

        data: dict = decode(
            keys=config.PASITA,
            deserializer=json,
            token=bearer,
        ).payload # type: ignore

        return token.from_dict(**data)
    return extractor # callback
"""
