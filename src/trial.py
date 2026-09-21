from pathlib import Path

import dash_cytoscape as cyto
from dash import Dash, html


from components.nodes import Token
from architecture import Architecture

import networkx as nx


def trial():
    arch = Architecture("Example Architecture", Path("./architecture"))
    arch.genGraph()
    ct = nx.cytoscape_data(arch.graph)
    print(ct)

    # Dash examples
    app = Dash(__name__)
    example_elements = [
        {"data": {"id": "ca", "label": "Canada"}},
        {"data": {"id": "on", "label": "Ontario"}},
        {"data": {"id": "qc", "label": "Quebec"}},
        {"data": {"source": "ca", "target": "on"}},
        {"data": {"source": "ca", "target": "qc"}},
    ]

    app.layout = html.Div(
        [
            html.P("Dash Cytoscape:"),
            cyto.Cytoscape(
                id="cytoscape",
                elements=ct["elements"],
                layout={"name": "breadthfirst"},
                style={"width": "400px", "height": "500px"},
            ),
        ]
    )

    app.run(debug=True)


if __name__ == "__main__":
    trial()
