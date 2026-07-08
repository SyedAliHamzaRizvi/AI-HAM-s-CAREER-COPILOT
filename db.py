from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = (
    "mysql+pymysql://34nYXCSV3XNFWjJ.root:cU7d1A2dexpWWD9Z"
    "@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"
)


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