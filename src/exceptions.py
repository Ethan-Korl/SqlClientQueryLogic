

class QueryError(Exception):
    pass
        

class PostgresQueryException(QueryError):
    def __init__(self, *args: object) -> None:
        self.message = object
        super().__init__(*args)