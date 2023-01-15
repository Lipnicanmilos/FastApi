from database import Base, engine 
from models import Blog

print("creating database ....")

Base.metadata.create_all(engine)