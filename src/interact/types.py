from pydantic import BaseModel
from fastapi import FastAPI

class PostgresQueryType(BaseModel):
    connection_string : str
    query : str
    
class SqlQueryType(BaseModel):
    connection_string : str
    query : str
    
class MysqlQueryType(BaseModel):
    connection_string : str
    query : str
    