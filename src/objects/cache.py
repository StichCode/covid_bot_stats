import ast
import sqlite3

from loguru import logger

from config import CONFIG
from src.functions.init_admins import insert_admins
from src.queries import DATABASE_STATIC, DATABASE_USERS


def str2dict(s: str):
    return ast.literal_eval(s)


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        [self.cursor.execute(query) for query in [DATABASE_USERS, DATABASE_STATIC]]

    @property
    def cursor(self):
        return self.conn.cursor()

    def put(self, table, *args):
        self.cursor.execute("INSERT INTO {0} VALUES ({1}, {2}, {3});".format(table, *args))
        self.conn.commit()
        logger.info(f"Data insert into {table} with {','.join([str(i) for i in args])} complete")

    def get(self, table, one=False, column=None):
        __sql = "SELECT {0} FROM {1};".format(str(column or '*'), table)
        data = self.cursor.execute(__sql)
        return data.fetchone() if one else data.fetchall()

    def change_subscr(self, user_id, subs):
        self.cursor.execute("UPDATE users SET subscribe={0} WHERE id={1};".format(subs, user_id))
        self.conn.commit()

    def is_exist(self, id_user):
        if not self.cursor.execute("SELECT * FROM users WHERE id = {0}".format(id_user)).fetchone():
            return False
        return True

    def is_subs(self, id_user):
        """ True if user want notify about covid """
        user_subs = self.cursor.execute("SELECT subscribe FROM users WHERE id = {0}".format(id_user)).fetchone()
        if user_subs is None or not user_subs[0]:
            # logger.warning(f"No user with this id {str(id_user)}, try to subs or unsubs")
            return False
        return True


CACHE = DataBase()
insert_admins(CACHE)
