from typing import Union, List, Any

from database.oointerface import Cocktail


class AbstractSQLDatabase:

    def __init__(self, connection: str):
        raise NotImplemented

    def query(self, query: str) -> Union[List[Any], None]:
        raise NotImplemented

    def commit(self):
        raise NotImplemented


class AbstractDatabase:

    def create_database(self):
        """creates the database instance"""
        raise NotImplemented

    def add_cocktail(self):
        """Add a cocktail to the list"""
        raise NotImplemented

    def add_ingredient(self):
        """Add an ingredient to the list"""
        raise NotImplemented

    def edit_cocktail(self):
        """Edit a cocktail in the list"""
        raise NotImplemented

    def edit_ingredient(self):
        """Edit an ingredient in the list"""
        raise NotImplemented

    def get_cocktails(self) -> List[Cocktail]:
        """Return filtered cocktails list"""
        raise NotImplemented
