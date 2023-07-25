from database import db_connection
import pandas as pd

def result_query(query):

    # Connect to the database
    connection = db_connection()

    # Execute the query
    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Convert the rows to a list of dictionaries
    result = []
    for row in rows:
        result.append(dict(zip(cursor.column_names, row)))

    return result