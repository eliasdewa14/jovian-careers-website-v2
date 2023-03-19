from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_single_job

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

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)