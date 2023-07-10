from database import db_connection
import csv

def upload_data(file,table,value):

    # Check if the file has a valid extension
    if not file.filename.endswith('.csv'):
        return 'Invalid file type. Please upload a CSV file', 400

    try:
        # Read the CSV file
        csv_data = file.read().decode('utf-8')
        data = list(csv.reader(csv_data.splitlines()))

        # Connect to the database
        connection = db_connection()

        # Insert data into the departments table
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

        return 'Data uploaded successfully', 200

    except Exception as e:
        return str(e), 500