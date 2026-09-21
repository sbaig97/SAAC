import importlib
import json
import os
from pathlib import Path

import networkx as nx


class Architecture:
    name: str
    nodes: list
    edges: list
    graph: nx.Graph

    def __init__(self, arch_name: str, definitions: Path):
        """
        Uses the JSON definitions provided by the user to generate an Architecture object

        :param name: Name to be given to the Architecture model.
        :type name: str
        :param definitions: Folder where all the definition files are found.
        :type definitions: Path
        """
        self.name = arch_name
        self.nodes = []
        self.edges = []

        # Load nodes and edges modules
        self.nodes_module = importlib.import_module("components.nodes")
        self.edges_module = importlib.import_module("components.edges")

        # Discover all files under the architecture folder.
        file_paths = []
        for dirpath, _, filenames in os.walk(definitions):
            for f in filenames:
                file_path = Path(".") / Path(dirpath) / f
                file_paths.append(file_path)

        # Loop over each one and based on file type and contents, create the associated objects.
        for fp in file_paths:
            self.loadGraphObject(json_definition=fp)

        # Create a graph object from the loaded nodes and edges

    def loadGraphObject(self, json_definition: Path):
        """Takes in a JSON encoded string to generate a Node or Edge. The resulting object is appended to self.

        :param json_definition: Path to JSON definition of graph object
        :type json_definition: Path
        """

        with open(json_definition, "r") as file:
            obj_def = json.loads(file.read())

        # Depending on the object type, invoke the associated class' cnstructor.
        obj_def_id = obj_def["id"]
        obj_def_type = obj_def["graph_object"]

        if str.lower(obj_def_type) == "node":
            class_ref = getattr(self.nodes_module, obj_def["class"])
            self.nodes.append(class_ref.generateFromJson(obj_def=obj_def))

        elif str.lower(obj_def_type) == "edge":
            class_ref = getattr(self.edges_module, obj_def["class"])
            self.edges.append(class_ref.generateFromJson(obj_def=obj_def))

        else:
            print(
                f"Graph object with id '{obj_def_id}' has an invalid value for the 'graph_object' field: '{obj_def_type}'"
            )

    # TODO: This can be improved. Need to re-assess how graph nodes and edges are to be described and represented.
    def genGraph(self):
        """Generates a Graph using the loaded nodes and edges."""

        self.graph = nx.Graph()

        for n in self.nodes:
            self.graph.add_node(n.id)
        for e in self.edges:
            self.graph.add_edge(e.node_1_id, e.node_2_id)

    def findNodebyId(self, id: str):
        """Find anode by ID.

        :param id: Node ID
        :type id: str
        """
        for n in self.nodes:
            if n.id == id:
                return n

    def genCytoscapeDefinition(self) -> dict:
        """_summary_

        :return: A dict that cytoscape can use to construct a visual representation of the graph object.
        :rtype: dict
        """

    # TODO
    def checkConstraints(self):
        """Method that checks the nodes and edges and verifies all hard constraints are satisfied."""

        # For example, we want to ensure all IDs are unique. If they are not, throw an error
