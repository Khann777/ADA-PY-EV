import psycopg2

def init_db():
    conn = psycopg2.connect(
        dbname="taskbot_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()