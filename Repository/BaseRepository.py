from abc import ABC, abstractmethod
import sqlite3
from typing import Generic, TypeVar, Optional, Iterable


T = TypeVar("T")  # Entidad de dominio (Usuario, PlanSesionItem, etc.)
ID = TypeVar("ID")  # Tipo de ID (int, str, etc.)

class BaseRepository(ABC, Generic[T, ID]):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn



    @abstractmethod
    def get_by_id(self, entity_id: ID) -> Optional[T]: ...
    @abstractmethod
    def list(self) -> Iterable[T]: ...
    @abstractmethod
    def add(self, entity: T) -> ID: ...
    @abstractmethod
    def update(self, entity: T) -> None: ...
    @abstractmethod
    def delete(self, entity_id: ID) -> None: ...