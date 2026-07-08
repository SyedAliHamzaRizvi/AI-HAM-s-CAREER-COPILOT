from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os 
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": r"C:\Users\DELL\Desktop\python\AI CAREER COPILOT\isrgrootx1.pem",
            "verify_cert": True,
            "verify_identity": True
        }
    }
)


SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()