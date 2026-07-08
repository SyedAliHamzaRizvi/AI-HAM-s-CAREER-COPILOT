from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os 
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable is missing")



engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "verify_cert": True,
            "verify_identity": True
        }
    }
)


SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()