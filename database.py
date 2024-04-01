from sqlalchemy import create_engine, text

# Your database connection string
engine = create_engine('mysql+mysqlconnector://root:alpha12345@localhost:3306/JOB_DB')

def load_jobs_from_db():
   with engine.connect() as conn:
    # Execute your query
    result = conn.execute(text("select * from jobs_db"))
    
    # Initialize an empty list to store your data
    jobs = []
    
    # Iterate over the result set and add each row to the list as a dictionary
    for row in result:
        jobs.append(dict(row._mapping))
    
    # Now data_list contains all rows as dictionaries
    return jobs
   
def load_users_from_db():
   with engine.connect() as conn:
    # Execute your query
    result = conn.execute(text("select * from users_db"))

    # Initialize an empty list to store your data
    users = []

    # Iterate over the result set and add each row to the list as a dictionary
    for row in result:
        users.append(dict(row._mapping))

    # Now data_list contains all rows as dictionaries
    return users