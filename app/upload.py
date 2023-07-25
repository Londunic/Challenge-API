from database import db_connection
import csv
import pandas as pd
from dateTransformation import dateModificated

def upload_data(file,table,value):

    # Check if the file has a valid extension
    if not file.filename.endswith('.csv'):
        return 'Invalid file type. Please upload a CSV file', 400

    try:
        # Read the CSV file
        csv_data = file.read().decode('utf-8')
        data = list(csv.reader(csv_data.splitlines()))

        #Convert data to Dataframe and change empty to NUll
        df = pd.DataFrame(data,columns=None)
        if (value == "emp"):
            #change the date structure
            df[2] = df[2].apply(dateModificated)
        df = df.applymap(lambda x: None if x == '' else x)
        df = df[df[1].notnull()]
        df = df.drop(df.columns[0], axis=1)
        data2 = df.values.tolist()

        # Connect to the database
        connection = db_connection()

        # Insert data into the departments table
        cursor = connection.cursor()
        # Query
        if (value == "emp"):
            query = "INSERT INTO "+table+" (name,date_time,department_id,job_id) VALUES (%s,%s,%s,%s)"
        else:
            query = "INSERT INTO "+table+" (name) VALUES (%s)"
    
        cursor.executemany(query, data2)
        connection.commit()

        cursor.close()
        connection.close()

        return 'Data uploaded successfully', 200

    except Exception as e:
        return str(e), 500
    

def insert_batch(dataJson,table,value):

    #Data format transformation
    data = []
    for row in dataJson:
        if (value == "emp"):
            aux = [row["name"],row["date_time"],row["department_id"],row["job_id"]]
        else:
            aux = [row["name"]]
        data.append(aux)
    
    # DB Connection
    connection = db_connection()
    cursor = connection.cursor()

    # Query
    if (value == "emp"):
        query = "INSERT INTO "+table+" (name,date_time,department_id,job_id) VALUES (%s,%s,%s,%s)"
    else:
        query = "INSERT INTO "+table+" (name) VALUES (%s)"

    cursor.executemany(query, data)
    connection.commit()

    cursor.close()
    connection.close()

    return 'Batch transactions inserted successfully', 200
    
    #return data
