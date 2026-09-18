from pydantic import BaseModel, Field


class Document(BaseModel):
    name: str
    sections: list = Field(default_factory=list)

    def addSection(self, section: Section):
        """Adds a new Section to the document. Sections appear in the order they are added.

        :param section: The Section to add to the end of the document.
        :type section: Section
        """
        self.sections.append(section)


class Section(BaseModel):
    title: str
    contents: list = Field(default_factory=list)

    def addContent(self, content: Section | Statement):
        """Adds new content to the end of the section. Content appears in the order they are added.

        :param content: Content to add to the section
        :type content: Section | Statement
        """
        self.contents.append(content)


class Statement(BaseModel):
    text: str = ""
    ref: str = ""


class Figure(Statement):
    pass


class Table(Statement):
    pass
