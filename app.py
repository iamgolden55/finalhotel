from flask import Flask, render_template, jsonify
import dbfunc  # This is the added import for your database functions

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Frontend tech',
    'location':'Bengaluru, Nigeria',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':3,
    'title':'Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':4,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
]

@app.route("/")
def hello():
    return render_template('home.html', 
                           jobs= JOBS,
                           company_name='Jovian')

@app.route("/login")
def login():
    clients = dbfunc.fetch_data("SELECT * FROM ava_jobs")  # Adjusted to call fetch_data with a specific query
    return render_template('login.html', client=clients)

@app.route("/register")
def register():
    clients = dbfunc.fetch_data("SELECT * FROM ava_jobs")  # Adjusted to call fetch_data with a specific query
    return render_template('register.html', client=clients)



@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/api/jobs/<int:job_id>")
def get_job(job_id):
  for job in JOBS:
    if job['id'] == job_id:
      return jsonify(job)
  return jsonify({'message':'Job not found'})

if __name__ == "__main__":
    app.run(debug=True)