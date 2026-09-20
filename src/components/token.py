import json

from pydantic import BaseModel

from enums.token_types import BooleanToken, NumberToken, StringToken, TokenType


class Node(BaseModel):
    id: str


class Service(Node):
    name: str
    description: str
    scope: str
    location: str


class Token(Node):
    name: str
    description: str
    type: type[TokenType]

    @classmethod
    def generateFromJson(cls, json_definition: str):
        """Uses a JSON serialised string to create an instance of self.

        :param json_definition: JSON serialised definition to generate of self.
        :type json_definition: str
        """
        # Convert JSON string to a dictionary
        json_def = json.loads(json_definition)

        # TODO: There has to be a more scalable way to do this part. Can't check every token type like this.
        if json_def["type"] == "String":
            token_type = StringToken
        elif json_def["type"] == "Number":
            token_type = NumberToken
        elif json_def["type"] == "Boolean":
            token_type = BooleanToken
        else:
            print("Invalid token")

        return cls(
            id=json_def["id"],
            name=json_def["name"],
            description=json_def["description"],
            type=token_type,
        )
