from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import pymysql

engine= create_engine(
    "mysql+pymysql://Scar3max:Mantoo%40028@localhost:3306/SkillGapAI",
    pool_pre_ping=True,
    )
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base=declarative_base()
pymysql.install_as_MySQLdb()