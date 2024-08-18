from typing import Any
import psycopg2
from exceptions import PostgresQueryException

class HandlePostgres:
    def __init__(self, conn_string: str, query: str) -> None:
        self.conn_string = conn_string
        self.query = query
        
    def connect(self) -> None | Exception:
        try:
            # Connect to your postgres DB
            self.conn = psycopg2.connect(self.conn_string)
            return None
        except Exception as ex:
            print(ex)
            return exec

    def query_of_fetch(self) -> list[tuple[Any, ...]] | None:
        try:
            # Open a cursor to perform database operations
            cur = self.conn.cursor()

            # Execute a query
            cur.execute(self.query)

            # Retrieve query results
            records = cur.fetchall()
            return records
        except:
            raise PostgresQueryException("Postgres Query Error,Please Check Query Statement")