from src.doc_tools.document import Document, Section, Statement
from jinja2 import Environment, FileSystemLoader


def main():
    # Main document
    doc = Document(name="Software Architecture Document")

    # Introduction section
    sec_intro = Section(title="Introduction")
    sec_intro.addContent(Statement(text="This is the introduction of the document"))
    sec_intro.addContent(Statement(text="Another statement"))
    sec_intro_scope = Section(title="Scope")
    sec_intro_scope.addContent(Statement(text="Here we can describe the scope"))
    sec_intro.addContent(sec_intro_scope)

    # Section 2
    section2 = Section(title="Second section")
    statement2 = Statement(text="Another statement")
    section2.addContent(statement2)

    doc.addSection(section=sec_intro)
    doc.addSection(section=section2)

    print(doc.model_dump_json())

    # Jinja example
    env = Environment(loader=FileSystemLoader("./src/html_templates"))
    template = env.get_template("example_template.html.j2")
    html = template.render(doc=doc)
    with open("example_template.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
