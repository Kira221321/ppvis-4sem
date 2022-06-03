import sqlite3


class DataBase:

    _db = 'database/leaderboard.db'

    def __init__(self):
        self.leaders = self.get_leaders()
        
    @classmethod
    def connect_database(cls):
        cls.conn = sqlite3.connect(cls._db)
        cursor = cls.conn.cursor()
        return cursor

    @classmethod
    def get_leaders(cls):
        cursor = DataBase.connect_database()
        leaders = []
        for row in cursor.execute("SELECT * FROM leaders ORDER BY score DESC"):
            leaders.append(row)
        return leaders

    @classmethod
    def get_leader_score(cls):
        cursor = cls.connect_database()
        try:
            for x in cursor.execute("SELECT MAX(score) FROM leaders"):
                leader_score = x[0]
        except Exception as e:
            leader_score = 0
        return leader_score if leader_score else 0

    @classmethod
    def add_new_record(cls, nickname, record):
        cursor = cls.connect_database()
        cursor.execute('''INSERT INTO leaders VALUES (?, ?)''', (nickname, record))
        cls.conn.commit()
        print("Add new record!")
        cls.conn.close()
