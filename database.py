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
  
  