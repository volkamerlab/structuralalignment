"""
remote.py

Defines remote KLIFS session.
"""

from bravado.client import SwaggerClient

from .core import (
    KinasesFactory,
    LigandsFactory,
    StructuresFactory,
    BioactivitiesFactory,
    InteractionsFactory,
    CoordinatesFactory,
)


class Kinases(KinasesFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client


class Ligands(LigandsFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client


class Bioactivities(BioactivitiesFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client


class Structures(StructuresFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client


class Interactions(InteractionsFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client


class Coordinates(CoordinatesFactory):
    def __init__(self, client):
        super().__init__()
        self.__client = client
