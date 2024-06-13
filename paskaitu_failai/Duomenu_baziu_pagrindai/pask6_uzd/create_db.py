from database import Base,engine


import Models.employees
import Models.projects
import Models.departaments

print("Started creating database")
Base.metadata.create_all(engine)
print("Finished creating database")