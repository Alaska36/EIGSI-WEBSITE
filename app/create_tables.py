from app.database import engine
from app.models import Base

# Crée les tables dans la base de données
Base.metadata.create_all(bind=engine)
