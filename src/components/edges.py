from components.graph import GraphObject


class Edge(GraphObject):
    """Defines edges in a graph"""

    node_1_id: str
    node_2_id: str


class WriteToken(Edge):
    @classmethod
    def generateFromJson(cls, obj_def: dict):
        """Uses a dict to create an instance of self.

        :param obj_def: A dictionary containing all the information required to instantiate an object of this class.
        :type obj_def: dict
        """

        return cls(
            id=obj_def["id"],
            label=obj_def["label"],
            node_1_id=obj_def["properties"]["writer_id"],
            node_2_id=obj_def["properties"]["token_id"],
        )
