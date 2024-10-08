from database import engine
from models import Base

# Crée les tables dans la base de données
Base.metadata.create_all(bind=engine)
