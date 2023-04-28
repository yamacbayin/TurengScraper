import sqlite3
from sqlite3 import Error

from Word import Word


class DatabaseManager:
    __database_name = 'WordsDB.sqlite'
    __sql_script_create = ("CREATE TABLE IF NOT EXISTS \"dictionary\"("
                           "\"id\" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                           "\"english_word\" TEXT NOT NULL,"
                           "\"turkish_equal_1\" TEXT NOT NULL,"
                           "\"turkish_equal_2\" TEXT NOT NULL,"
                           "\"turkish_equal_3\" TEXT NOT NULL,"
                           "\"turkish_equal_4\" TEXT NOT NULL,"
                           "\"turkish_equal_5\" TEXT NOT NULL,"
                           "\"wrong_answer\" TEXT NOT NULL)")

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.__database_name)
            self.connection.execute(self.__sql_script_create)
        except Error as error:
            print(error)

    def read_word(self, word_id):
        cursor = self.connection.execute("SELECT * FROM WORDS WHERE _id=" + str(word_id))
        data = cursor.fetchone()
        cursor.close()
        if data is None:
            print("Cannot read word with id: " + str(word_id))
        else:
            word = Word()
            word.english_word = data[1]
            word.wrong_answer = data[3]
            return word

    def write_word(self, word):
        sql = '''INSERT INTO dictionary(english_word,turkish_equal_1,turkish_equal_2,turkish_equal_3,
            turkish_equal_4,turkish_equal_5,wrong_answer) VALUES(?,?,?,?,?,?,?)'''
        cursor = self.connection.cursor()
        data_tuple = (word.english_word,
                      word.turkish_equals_list[0],
                      word.turkish_equals_list[1],
                      word.turkish_equals_list[2],
                      word.turkish_equals_list[3],
                      word.turkish_equals_list[4],
                      word.wrong_answer)
        cursor.execute(sql, data_tuple)
        self.connection.commit()
        cursor.close()

    def get_last_row_id(self):
        """Return the id of last row in dictionary table."""
        cursor = self.connection.execute("SELECT * FROM dictionary ORDER BY id DESC LIMIT 1;")
        data = cursor.fetchone()
        cursor.close()
        if data is None:
            return 1
        else:
            return data[0] + 1

    def close_connection(self):
        self.connection.close()
