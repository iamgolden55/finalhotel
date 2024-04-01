from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_users_from_db # This is the added import for your database functions

app = Flask(__name__)





    
@app.route("/")
def hello():
    user = load_users_from_db()
    jobs = load_jobs_from_db() # Load the data from the database
    return render_template('home.html',
                           user = user, 
                           jobs= jobs,
                           company_name='Jovian')

 #@app.route("/login")
#def login():
   # clients = engine.fetch_data("SELECT * FROM ava_jobs")  # Adjusted to call fetch_data with a specific query
   # return render_template('login.html', client=clients)

#@app.route("/register")
#def register():
    #clients = engine.fetch_data("SELECT * FROM ava_jobs")
    #users = engine.fetch_data("SELECT * FROM users_db")  # Assuming the table name is 'users' in the 'JOB_DB' database
    #return render_template('register.html', clients=clients, users=users)



@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db)

@app.route("/api/jobs/<int:job_id>")
def get_job(job_id):
  for job in load_jobs_from_db():
    if job['id'] == job_id:
      return jsonify(job)
  return jsonify({'message':'Job not found'})

if __name__ == "__main__":
    app.run(debug=True)