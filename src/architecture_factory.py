import os
from pathlib import Path

from pydantic import BaseModel

from components.token import Token


class ArchitectureFactory:
    arch_folder = Path("./architecture")

    def generateArchitecture(self, arch_name: str, definitions: Path):
        """
        Uses the JSON definitions provided by the user to generate an Architecture object

        :param name: Name to be given to the Architecture model.
        :type name: str
        :param definitions: Folder where all the definition files are found.
        :type definitions: Path
        :return: The Architecture model.
        :rtype: Architecture
        """
        file_paths = []

        # Discover all files under the architecture folder.
        for dirpath, _, filenames in os.walk(definitions):
            for f in filenames:
                file_path = Path(".") / Path(dirpath) / f
                file_paths.append(file_path)

        # Loop over each one and based on file type and contents, create the associated objects.
        nodes = []
        edges = []

        for fp in file_paths:
            with open(fp, "r") as file:
                file_content = file.read()

            # TODO: At this point we need to load the file content into a dictionary so we can query it. Then we make a decision on which object needs to be created.

            nodes.append(Token.generateFromJson(json_definition=file_content))

        # TODO: remove me
        for t in nodes:
            print(
                t.id,
                t.name,
                t.type,
                t.description,
            )

        return Architcture(name=arch_name, nodes=nodes, edges=edges)


class Architcture(BaseModel):
    name: str
    nodes: list
    edges: list

    # Methods that generate the graph representation here would be useful.

    def checkConstraints(self):
        """Method that checks the nodes and edges and verifies all hard constraints are satisfied."""

        # For example, we want to ensure all IDs are unique. If they are not, throw an error
