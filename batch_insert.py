from database import db_connection

def insert_batch(data,table,value):
    connection = db_connection()
    cursor = connection.cursor()

    # Query
    if (value == "emp"):
        query = "INSERT INTO "+table+" (id,name,date_time,department_id,job_id) VALUES (%s,%s,%s,%s,%s)"
    else:
        query = "INSERT INTO "+table+" (id,name) VALUES (%s,%s)"

    cursor.executemany(query, data)
    connection.commit()

    cursor.close()
    connection.close()

    return 'Batch transactions inserted successfully', 200