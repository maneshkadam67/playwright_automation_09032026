# db_helper.py
import mysql.connector

class DBHelper:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

    def get_row_count(self, table_name):
        self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        return self.cursor.fetchone()[0]

    def verify_row_count(self, table_name, expected_count):
        actual = self.get_row_count(table_name)
        return actual == expected_count

    def close(self):
        self.cursor.close()
        self.conn.close()
