import sqlite3
import app

# Get any text
def getOneRandom():
    sql = "SELECT MT_CONTENT FROM YOUR_TABLE ORDER BY RANDOM() LIMIT 1"
    cur = app.excute_sql_select(sql, None)
    row = cur.fetchone()
    return row[0]

# Get accumulated figures
def getAccCount():
    sql = "SELECT COUNT(1) FROM YOUR_TABLE"
    cur = app.excute_sql_select(sql, None)
    row = cur.fetchone()
    return row[0]

# Add some text
def addMention(paramMention):
    sql = "INSERT INTO YOUR_TABLE (MT_CONTENT, MT_UPTIME) VALUES (:mtContent, DATETIME('NOW', 'LOCALTIME'))"
    param = {'mtContent': paramMention}
    return app.excute_sql_update(sql, param)

# Get specific id of text
def getId(paramMention):
    sql = "SELECT MAX(MT_ID) AS MT_ID FROM YOUR_TABLE WHERE MT_CONTENT = :mtContent"
    param = {'mtContent': paramMention}
    cur = app.excute_sql_select(sql, param)
    row = cur.fetchone()
    return row[0]

# Del specific text
def delMention(paramMention):
    sql = "DELETE FROM YOUR_TABLE WHERE MT_CONTENT = :mtContent"
    param = {'mtContent': paramMention}
    return app.excute_sql_update(sql, param)