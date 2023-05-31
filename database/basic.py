from typing import Union, List, Any

from database.oointerface import Cocktail


class AbstractGenericDatabase:

    def __init__(self, connection: str):
        raise NotImplemented

    def query(self, query: str) -> Union[List[Any], None]:
        raise NotImplemented

    def commit(self):
        raise NotImplemented


class AbstractDatabase(AbstractGenericDatabase):

    def create_tables(self):
        self.query("""
            CREATE TABLE Cocktails (
                id integer NOT NULL,
                name varchar(200),
                strength smallint,
                complexity smallint,
                description varchar(1000),
                recipe varchar(20000),
                photo varchar(200),
                primary key (id)
            );
            CREATE TABLE Ingredients (
                id integer NOT NULL,
                name varchar(50),
                description varchar(500),
                link varchar(500),
                photo varchar(200),
                primary key (id)
            );
            CREATE TABLE IngredientsInCocktails (
                id integer NOT NULL,
                cocktail_id integer NOT NULL,
                ingredient_id integer NOT NULL,
                primary key (id, cocktail_id, ingredient_id),
                foreign key (cocktail_id) references Cocktails(id),
                foreign key (ingredient_id) references Ingredients(id)
            )            
        """)
        self.commit()

    def add_cocktail(self):
        # TODO Add a cocktail to the list
        pass

    def add_ingredient(self):
        # TODO Add an ingredient to the list
        pass

    def edit_cocktail(self):
        # TODO Edit a cocktail in the list
        pass

    def edit_ingredient(self):
        # TODO Edit an ingredient in the list
        pass

    def get_cocktails(self) -> List[Cocktail]:
        # TODO Return filtered cocktails list
        pass
