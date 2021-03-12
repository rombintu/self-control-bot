import sqlite3
from datetime import date, datetime, timedelta


def select_all_today():
    db = sqlite3.connect("database.db")
    sql = db.cursor()
    today = str(date.today())

    script = "SELECT name, time FROM clients WHERE date=?"

    sql.execute(script, (today, ))
    return sql.fetchall()
    

def select_all_yesterday():
    db = sqlite3.connect("database.db")
    sql = db.cursor()
    
    today = date.today()
    yesterday = str(today - timedelta(days=1))

    script = "SELECT name, time FROM clients WHERE date=?"

    sql.execute(script, (yesterday, ))
    return sql.fetchall()
    
def add_req(name):
    db = sqlite3.connect("database.db")
    sql = db.cursor()
    now_time = datetime.now().strftime('%H:%M')
    now_date = str(date.today())

    script_check = "SELECT id FROM clients WHERE name=? AND date=?"
    sql.execute(script_check, (name, now_date, ))
    check_count = sql.fetchall()
    if len(check_count) > 0:
        return "Видимо ты уже сегодня отмечался, попробуй завтра"
    else:
        script_push = "INSERT INTO clients (name, time, date) VALUES (?,?,?)"
        sql.execute(script_push, (name, now_time, now_date, ))
        db.commit()
        db.close()
        return "Красавчик"