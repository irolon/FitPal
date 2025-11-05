import sqlite3

class Conexion:
    def __init__ (self,path):
        self.conexion = sqlite3.connect(path)
        self.conexion.execute("PRAGMA foreign_keys = ON;")
        self.conexion.row_factory = sqlite3.Row1
        self.cursor = self.conexion.cursor()

