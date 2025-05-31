from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class SentimentLog(Base):
    __tablename__ = 'sentiment_logs'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    sentiment = Column(String)
    score = Column(Float)

engine = create_engine('sqlite:///sentiment.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
