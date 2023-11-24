import psycopg2

def GetConnection(conectionString):
    connection = psycopg2.connect(conectionString)
    cursor = connection.cursor()
    return connection, cursor

def GetView(cursor, viewName):
    selectView = f'SELECT * FROM {viewName}'
    cursor.execute(selectView)
    View = cursor.fetchall()
    return View
