from abc import ABC, abstractmethod
import sqlite3


class BaseDAO(ABC):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cur = conn.cursor()
        
    @abstractmethod
    def create_table(self): ...
    @abstractmethod
    def create(self): ...
    @abstractmethod
    def read_by_id(self, id_: int): ...
    @abstractmethod
    def update(self, id_: int): ...
    @abstractmethod
    def delete(self, id_: int): ...
    @abstractmethod
    def list(self): ...