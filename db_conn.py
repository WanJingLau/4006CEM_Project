import pyodbc as db

conn = db.connect(DRIVER='{ODBC Driver 17 for SQL Server}', Server="(local)\SQLEXPRESS", uid="ebook", pwd="ebook123",database="master",Trusted_Connection='yes').cursor()

def readFromDb(dbQuery):
    conn.execute(dbQuery)
    return conn.fetchone()

def insertUpdateDeleteToDb(dbQuery):
    conn.execute(dbQuery)
    result = conn.rowcount
    conn.commit()
    return result