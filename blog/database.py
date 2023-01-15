from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Lip25nican26@localhost:5432/fastapi"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()

# engine=create_engine("postgresql://postgres:Lip25nican26@localhost/fastapi",
#     echo=True
# )

engine=create_engine("postgresql://lipnicanmilos:wuym59WqUYTN@ep-wandering-voice-977934.eu-central-1.aws.neon.tech/neondb",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
