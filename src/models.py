from src.app import db

# hired_employees table
class Employee(db.Model):
    __tablename__ = 'hired_employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime(timezone=True), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))

# departments table
class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100), nullable=False)

# jobs table
class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100), nullable=False)
