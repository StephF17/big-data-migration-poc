from flask import request
from sqlalchemy.exc import DataError
from . import sshconnect
from . import dbconnect
from .app import app, db
from .models import Employee, Department, Job

@app.route('/hr/hired_employees', methods=['POST'])
def insert_employees():
    try:
        data = request.json
        if not isinstance(data, list):
            return {"message":"Invalid request. Expected a JSON array.)"}, 400
        
        # Limit of records per request (1000)
        if len(data) > 1000:
            return {"message":"Invalid request. Row limit exceeded (1000).)"}, 400
    
        # Filter data
        filtered_data = []
        for record in data:
            try:
                id = record["id"]
                name = record["name"]
                datetime = record["datetime"]
                department_id = record["department_id"]
                job_id = record["job_id"]
                new_record = Employee(id, name, datetime, department_id, job_id)
                filtered_data.append(new_record)
            except DataError as e:
                app.logger.error("DataError: %s", e)
        
        try:
            # Database connection
            server = sshconnect.create_tunnel()
            conn = dbconnect.create_connection()
            # Upload records
            cursor = conn.cursor()
            for employee in filtered_data:
                query = '''
                    INSERT INTO hired_employees
                    (id, name, datetime, department_id, job_id)
                    VALUES (%s, %s, %s, %s, %s)
                '''
                cursor.execute(cursor, (employee.id, employee.name, employee.datetime, employee.department_id, employee.job_id))

            conn.commit()
        finally:
            # Stop connection
            dbconnect.close_connection(conn)
            sshconnect.close_tunnel(server)
    
        return {"message": ("%s records were inserted successfully", len(filtered_data))}, 200

    except Exception as e:
        app.logger.error("Error: %s", e)
        return {"message":"There has been an error processing your request"}, 500


@app.route('/hr/departments', methods=['POST'])
def insert_departments():
    try:
        data = request.json
        if not isinstance(data, list):
            return {"message":"Invalid request. Expected a JSON array.)"}, 400
        
        # Limit of records per request (1000)
        if len(data) > 1000:
            return {"message":"Invalid request. Row limit exceeded (1000).)"}, 400

        # Filter data
        filtered_data = []
        for record in data:
            try:
                id = record["id"]
                department = record["deparment"]
                new_record = Department(id, department)
                filtered_data.append(new_record)
            except DataError as e:
                app.logger.error("DataError: %s", e)
        
        try:
            # Database connection
            server = sshconnect.create_tunnel()
            conn = dbconnect.create_connection()
            # Upload records
            cursor = conn.cursor()
            for department in filtered_data:
                cursor.execute("INSERT INTO departments(id, department) VALUES (%s, %s)", (department.id, department.department))

            conn.commit()
        finally:
            # Stop connection
            dbconnect.close_connection(conn)
            sshconnect.close_tunnel(server)
    
        return {"message": ("%s records were inserted successfully", len(filtered_data))}, 200

    except Exception as e:
        app.logger.error("Error: %s", e)
        return {"message":"There has been an error processing your request"}, 500


@app.route('/hr/jobs', methods=['POST'])
def insert_jobs():
    try:
        data = request.json
        if not isinstance(data, list):
            return {"message":"Invalid request. Expected a JSON array.)"}, 400
        
        # Limit of records per request (1000)
        if len(data) > 1000:
            return {"message":"Invalid request. Row limit exceeded (1000).)"}, 400

        # Filter data
        filtered_data = []
        for record in data:
            try:
                id = record["id"]
                job = record["job"]
                new_record = Job(id, job)
                filtered_data.append(new_record)
            except DataError as e:
                app.logger.error("DataError: %s", e)
        
        try:
            # Database connection
            server = sshconnect.create_tunnel()
            conn = dbconnect.create_connection()
            # Upload records
            cursor = conn.cursor()
            for job in filtered_data:
                cursor.execute("INSERT INTO jobs(id, job) VALUES (%s, %s)", (job.id, job.job))

            conn.commit()
        finally:
            # Stop connection
            dbconnect.close_connection(conn)
            sshconnect.close_tunnel(server)
    
        return {"message": ("%s records were inserted successfully", len(filtered_data))}, 200

    except Exception as e:
        app.logger.error("Error: %s", e)
        return {"message":"There has been an error processing your request"}, 500
