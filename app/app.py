from flask import Flask, request, jsonify, render_template
from upload import upload_data,insert_batch
from queries import result_query

app = Flask(__name__)

@app.route('/upload_deps', methods=['POST'])
def upload_deps():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"departments","other")


@app.route('/upload_jobs', methods=['POST'])
def upload_jobs():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"jobs","other")


@app.route('/upload_emp', methods=['POST'])
def upload_emp():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"employees","emp")


@app.route('/batch_insert_deps', methods=['POST'])
def batch_insert_deps():
    try:
        data = request.json
        if not isinstance(data, list):
            return "A list of transactions was expected", 400

        if len(data) == 0:
            return "The transaction list is empty", 400

        if len(data) >= 1000:
            return "The list has more than 1000 transactions",400

        return insert_batch(data,"departments","other")

    except Exception as e:
        return "Error entering transactions :" + str(e), 500


@app.route('/batch_insert_jobs', methods=['POST'])
def batch_insert_jobs():
    try:
        data = request.json
        if not isinstance(data, list):
            return "A list of transactions was expected", 400

        if len(data) == 0:
            return "The transaction list is empty", 400
        
        if len(data) >= 1000:
            return "The list has more than 1000 transactions",400

        return insert_batch(data,"jobs","other")

    except Exception as e:
        return "Error entering transactions :" + str(e), 500


@app.route('/batch_insert_emp', methods=['POST'])
def batch_insert_emp():
    try:
        data = request.json
        if not isinstance(data, list):
            return "A list of transactions was expected", 400

        if len(data) == 0:
            return "The transaction list is empty", 400
        
        if len(data) >= 1000:
            return "The list has more than 1000 transactions",400

        return insert_batch(data,"employees","emp")

    except Exception as e:
        return "Error entering transactions :" + str(e), 500


@app.route('/sql_query1')
def sql_query1():
    query = """SELECT 
        d.name AS department,
        j.name AS job,
        COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 1 AND 3 THEN 1 END) AS 'Q1',
        COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 4 AND 6 THEN 1 END) AS 'Q2',
        COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 7 AND 9 THEN 1 END) AS 'Q3',
        COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 10 AND 12 THEN 1 END) AS 'Q4'
    FROM
        employees e
        INNER JOIN departments d ON e.department_id = d.id
        INNER JOIN jobs j ON e.job_id = j.id
    WHERE
        YEAR(e.date_time) = 2021
    GROUP BY
        department, job
    ORDER BY
        department, job;"""
    
    results = result_query(query)
    return render_template('query1.html', result=results)


@app.route('/sql_query2')
def sql_query2():
    query = """SELECT
        d.id AS id,
        d.name AS department,
        COUNT(e.id) AS hired
    FROM
        departments d
        INNER JOIN employees e ON e.department_id = d.id
    WHERE
        YEAR(e.date_time) = 2021
    GROUP BY
        id, department
    HAVING
        COUNT(e.id) > (
            SELECT AVG(count_emp)
            FROM (
                SELECT COUNT(e.id) AS count_emp
                FROM employees e
                WHERE YEAR(e.date_time) = 2021
                GROUP BY e.department_id
            ) AS sub
        )
    ORDER BY
        hired DESC;"""

    results = result_query(query)
    return render_template('query2.html', result=results)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
