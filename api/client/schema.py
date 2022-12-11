from typing import Optional

from pydantic import BaseModel, validator


class ChatGetQueryQuery(BaseModel):
    prompt: str


class PaintGetGetImageQuery(BaseModel):
    prompt: str


class ValidationError(BaseModel):
    loc: Optional[list] = None
    msg: Optional[str] = None
    type: Optional[str] = None

    @validator("loc")
    def optional_loc(cls, val: list):
        if val is not None:
            return val
        else:
            raise ValueError("loc may not be None")

    @validator("msg")
    def optional_msg(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("msg may not be None")

    @validator("type")
    def optional_type(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("type may not be None")


class HTTPValidationError(BaseModel):
    detail: list[ValidationError]
