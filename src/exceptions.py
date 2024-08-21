

class QueryError(Exception):
    pass


class QuerySyntaxError(QueryError):
    pass
        

class PostgresQueryException(QueryError):
    def __init__(self, *args: object) -> None:
        self.message = object
        super().__init__(*args)


class MySqlQueryException(QueryError):
    def __init__(self, *args: object) -> None:
        self.message = object
        super().__init__(*args)
