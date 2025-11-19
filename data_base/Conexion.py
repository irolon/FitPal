import sqlite3

class Conexion:
    def __init__(self, path):
        self.conexion = sqlite3.connect(path, check_same_thread=False)
        self.conexion.execute("PRAGMA foreign_keys = ON;")
        self.conexion.row_factory = sqlite3.Row
        self.cursor = self.conexion.cursor()
