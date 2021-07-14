import sqlite3


#Make a connection with the database
def connect():
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS courseM (id INTEGER PRIMARY KEY,link TEXT,title TEXT ,headline TEXT,instructor TEXT,rating TEXT,review TEXT )")
    conn.commit()
    conn.close()

def search(title,instructor):
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    print("search established ")
    cur.execute("SELECT * FROM courseM WHERE title = ? OR instructor=? ",(title,instructor))
    rows=cur.fetchall()
    conn.close()
    print("case closed")
    print("sadasdas",rows)
    return rows

def insert(link,title,headline, instructor,rating,review):
    try:
        conn = sqlite3.connect('source.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        cursor.execute(" INSERT INTO courseM (link,title,headline, instructor,rating,review) VALUES (?, ?,?,?,?,?)", (link,title,headline, instructor,rating,review))
        conn.commit()
        print("inserted successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert  data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")


def view():
    conn=sqlite3.connect("source.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM courseM")
    rows=cur.fetchall()
    conn.close()
    for row in rows:
        print(row)
    return rows

connect()