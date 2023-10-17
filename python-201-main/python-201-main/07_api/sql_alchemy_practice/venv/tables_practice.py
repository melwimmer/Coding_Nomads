# import sqlalchemy
# from pprint import pprint
# engine = sqlalchemy.create_engine('mysql+pymysql://melanie:Amma!108@localhost/sakila')
# connection = engine.connect()
# metadata = sqlalchemy.MetaData()

##This is to create a new table

# newTableyay = sqlalchemy.Table('newTableyay', metadata,
#                        sqlalchemy.Column('Id', sqlalchemy.Integer()),
#                        sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
#                        sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
#                        sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
#               )

# metadata.create_all(engine)

# # to see if it worked, go to the workbench and check if it was created. 


# # now to insert info on the table: 
# query = sqlalchemy.insert(newTable)
# new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
#                {'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
# result_proxy = connection.execute(query,new_records)


import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://melanie:Amma!108@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload_with=engine)
##This is to insert only one value to the table. 
# query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=50000.00, active=True)
# result_proxy = connection.execute(query)
# connection.commit()

#This is to return multiple values to the table. 
query = sqlalchemy.insert(newTable)
new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
result_proxy = connection.execute(query,new_records)
connection.commit()

#The comit is needed 

