from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Chaîne de connexion à ta base de données PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.ezdgfffkfljicnoozrcl:Alaska40023010+*@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

# Créer l'engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Créer la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer le modèle de base
Base = declarative_base()
