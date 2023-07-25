from database.basic import AbstractDatabase, AbstractSQLDatabase


class SQLiteDB(AbstractSQLDatabase, AbstractDatabase):

    def create_database(self):
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
                link varchar(500),
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
