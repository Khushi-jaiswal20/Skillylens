from app import mysql

def get_user_by_email(email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    return cur.fetchone()

def get_user_analyses(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM analyses WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
    return cur.fetchall()