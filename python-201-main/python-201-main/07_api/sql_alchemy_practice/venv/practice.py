import sqlalchemy 
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://melanie:Amma!108@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata,  autoload_with=engine)
film = sqlalchemy.Table('film', metadata,  autoload_with=engine)

# query = sqlalchemy.select(actor)
#Using the where statement
query = sqlalchemy.select(actor).where(actor.columns.first_name == 'PENELOPE')
#Using the in statement
# query = sqlalchemy.select(actor).where(actor.columns.first_name.in_(["PENELOPE", "JOHN", "UMA"]))
#Using the or statement
# query = sqlalchemy.select(film).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating == "PG"))
# query = sqlalchemy.select(film).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating != "PG"))
#order by 
# query = sqlalchemy.select(film).order_by(sqlalchemy.asc(film.columns.replacement_cost))
#sum and other functions
# query = sqlalchemy.select(sqlalchemy.func.sum(film.columns.length))
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

