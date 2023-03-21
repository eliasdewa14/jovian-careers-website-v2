from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_single_job, add_application_to_db

app = Flask(__name__)
 
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)

@app.route("/job/<job_id>")
def show_job(job_id):
  job = load_single_job(job_id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', job=job)

@app.route("/job/<job_id>/apply", methods=['post'])
def apply_to_job(job_id):
  #data = request.args
  # request.args -> contain information from the url
  data = request.form
  # send an email
  # display an acknowledgement
  job = load_single_job(job_id)
  # return jsonify(data)
  
  # store this in db
  add_application_to_db(job_id, data)
  return render_template('application_submitted.html',
                         application=data, job=job)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)