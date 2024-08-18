from db.postgres_db import HandlePostgres
from exceptions import PostgresQueryException

def postgres_query(connection: str, query: str):    
    handle_postgres = HandlePostgres(connection, query)

    if handle_postgres.connect() != None:
        return {"message":"error"}
    
    try:
        result = handle_postgres.query_of_fetch() 
        return result
    except PostgresQueryException as psex:
        return {"message":"Postgres Query Error,Please Check Query Statement"}



def mysql_query():
    return {"message":"data"}


def sqlserver_query():
    return {"message":"data"}