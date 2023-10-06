from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://wudkfjug:M71bebQQl4MS3EQGr1TW-2NZ3Dc_QJJL@cornelius.db.elephantsql.com/wudkfjug"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
