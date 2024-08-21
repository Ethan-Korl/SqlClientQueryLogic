from typing import Union
from http_client.types import (
    PostgresQueryType,
    MysqlQueryType,
    SqlQueryType
    )
from fastapi import FastAPI
from http_client.handlers import (
    postgres_query,
    mysql_query,
    sqlserver_query
    )

app = FastAPI()

@app.post("/mysql-query")
def mysql(query: MysqlQueryType):
    return mysql_query()


@app.post("/postgres-query")
def postgres(query: SqlQueryType):
    # print(query.)
    return postgres_query(query.connection_string, query.query)


@app.post("/sqlserver-query")
def sqlserver(query: PostgresQueryType):
    return sqlserver_query()

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
