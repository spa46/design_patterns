import pathlib
from abc import ABCMeta, abstractmethod


class DBManager(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass


class PostgreSQL(DBManager):
    def connect(self):
        print('PostgreSQL 연결')
        return 'connection', []


class MySQL(DBManager):
    def connect(self):
        print('MySQL 연결')
        return 'connection', []


class MsSQL(DBManager):
    def connect(self):
        print('MsSQL 연결')
        return 'connection', []


class DBFactory:
    def __init__(self):
        path = pathlib.Path('config/db.yaml').read_text()
        if path == 'postgresql':
            self.db_object = PostgreSQL()
        elif path == 'mysql':
            self.db_object = MySQL()
        else:
            self.db_object = MsSQL()
        self.connect, self.cursor = self.db_object.connect()


class Item(DBFactory):
    def __init__(self):
       super(Item, self).__init__(self)

    def insert(self):
        self.cursor.insert(0, '데이터 insert')


item = Item()
item.insert()
