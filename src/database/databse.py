import json
import sqlite3
from typing import List, Any
from database.item import DatabaseItem

class Database():
    """
    Quick-Sqlite-Database
    """
    def __init__(self, path: str, name: str = "__default__", auto_init: Any = None) -> None:
        self.path = path
        self.conn = sqlite3.connect(path)
        self.name = name
        self.auto_init = auto_init

        c = self.conn.cursor()
        check = c.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.name}';")

        if (not list(check)):
            c = self.conn.cursor()
            c.execute(
                f'CREATE TABLE `{self.name}` (`key` CHAR(255) NOT NULL PRIMARY KEY, `value` JSON);')
            self.conn.commit()

    def __str__(self) -> str:
        return '{'+ ', '.join(map(str, self.get_all())) + '}'
    
    def __repr__(self) -> str:
        return f"<Database path={self.path} name={self.name} auto_init={self.auto_init}>"

if __name__ == "__main__":
    pass
    # db = Database("test.db", auto_init=0)
    # print(repr(db))
    