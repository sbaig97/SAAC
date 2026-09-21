from components.graph import GraphObject
from enums.token_types import BooleanToken, NumberToken, StringToken, TokenType


class Node(GraphObject):
    """Defines nodes in a graph"""


class Service(Node):
    description: str
    scope: str
    location: str


class Token(Node):
    description: str
    type: type[TokenType]

    @classmethod
    def generateFromJson(cls, obj_def: dict):
        """Uses a dict to create an instance of self.

        :param obj_def: A dictionary containing all the information required to instantiate an object of this class.
        :type obj_def: dict
        """

        # TODO: There has to be a more scalable way to do this part. Can't check every token type like this.
        token_type = obj_def["properties"]["type"]
        if token_type == "String":
            token_type = StringToken
        elif token_type == "Number":
            token_type = NumberToken
        elif token_type == "Boolean":
            token_type = BooleanToken
        else:
            print(f"Invalid value: {token_type}")

        return cls(
            id=obj_def["id"],
            label=obj_def["label"],
            description=obj_def["properties"]["description"],
            type=token_type,
        )
