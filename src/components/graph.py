from abc import ABC, abstractmethod

from pydantic import BaseModel


class GraphObject(BaseModel, ABC):
    """Abstract class for modelling generic Graph Objects."""

    id: str
    label: str

    @abstractmethod
    def generateFromJson(cls, obj_def: dict):
        """Uses a dict to create an instance of self.

        :param obj_def: A dictionary containing all the information required to instantiate an object of this class.
        :type obj_def: dict
        """
