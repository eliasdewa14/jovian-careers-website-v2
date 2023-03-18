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
"""
with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))
  
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all()):", type(result_all))
  first_result = result_all[0]
  print("type(first_result:", type(first_result))
"""
  
  