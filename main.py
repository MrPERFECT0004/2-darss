import psycopg2


class DataBase:
    def __init__(self):
        self.connect = psycopg2.connect(
            database='imtihon',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.connect as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)

                if commit:
                    result = db.commit()

                elif fetchone:
                    result = db.fetchone()

                elif fetchall:
                    result = db.fetchall()

                return result

        def create_employees(self):
            sql = """CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            full_name VARCHAR(50),
            age INTEGER,
            email VARCHAR(50),
            phone VARCHAR(15),
            address VARCHAR(100)
        );
        """

        self.manager(sql, commit=True)

    def insert_employees(self):
        sql = """INSERT INTO employees (full_name, age, email, phone, address) VALUES
        ('Muhammadjon', 'Abdujabborov', 17, 'MuhammadjonAbdujabborov07@gmail.com', 'Fergana'),
        ('Alisher', 'Aliyev', 17, 'Aliyyy@gmail.com', 'Fergana'),
        ('Nuriddin', 'Aliyev', 19, 'nuribek@gmail.com', 'Fergana'),
        ('Asilbek', 'Abdujabborov', 21, 'bekk@gmail.com', 'namangan');
        """
        self.manager(sql, address, commit=True)

    def alter_table(self):
        sql = """ALTER TABLE """

        