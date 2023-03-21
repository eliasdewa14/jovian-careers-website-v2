from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
  
    jobs_list = []
    for row in result.all():
      jobs_list.append(row._asdict())
  
    return jobs_list

def load_single_job(job_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {'val': job_id})
    
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
  

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    conn.execute(text("INSERT INTO applications VALUES (job_id = :job_id, full_name = :full_name, email = :email, linkedin_url = :linkedin_url, education = :education, work_experience = work_experience, resume_link = :resume_link)"), {'job_id': job_id, 'full_name': data['full_name'], 'email': data['email'], 'linkedin_url': data['linkedin_url'], 'education': data['education'], 'work_experience': data['work_experience'], 'resume_link': data['resume_link']})