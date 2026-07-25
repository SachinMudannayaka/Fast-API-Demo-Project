from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url = "mysql+pymysql://root:<PW>@localhost:3306/fastapi_demo"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit = False,autoflush=False, bind=engine)
