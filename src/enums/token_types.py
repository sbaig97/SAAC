from abc import ABC

from pydantic import BaseModel


class TokenType(BaseModel, ABC):
    """Abstract class for defining token types

    :raises TypeError: Raised if 'type' field is not defined by subclass.
    :raises TypeError: Raised if 'description' field is not defined by subclass.
    :raises TypeError: Raised if 'constraints' field is not defined by subclass.
    :raises TypeError: Raised if 'example' field is not defined by subclass.
    """

    type: str
    description: str
    constraints: list
    example: str

    def __init_subclass__(cls, **kwargs):

        super().__init_subclass__(**kwargs)

        if "type" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define 'type'")

        if "description" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define 'description'")

        if "constraints" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define 'constraints'")

        if "example" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define 'example'")


class StringToken(TokenType):
    type: str = "String"
    description: str = "A token that may only contain a quoted string."
    constraints: list[str] = [
        "Shall be a quoted string, i.e., characters must start and end with quotes.",
        "Token contents shall be on the first line only",
    ]
    example: str = '"EXAMPLE"'


class NumberToken(TokenType):
    type: str = "Number"
    description: str = "A token that contains a number."
    constraints: list[str] = [
        "Shall only contain numbers from 0-9.",
        "Token contents shall be on the first line only.",
    ]
    example: str = "12345"


class BooleanToken(TokenType):
    type: str = "Boolean"
    description: str = (
        "A token that contains one of two possibilities that define a boolean."
    )
    constraints: list[str] = [
        "Shall only contain the character array 'true', or 'false'.",
        "Token contents shall be on the first line only.",
    ]
    example: str = "true"
