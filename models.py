from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///data/peipsi_birds.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class PeipsiBirds(Base):
    __tablename__ = 'birds'
    id = Column(Integer, primary_key=True)
    order = Column(String(30))
    family = Column(String(30))
    name_rus = Column(String(30))
    name_lat = Column(String(30))
    signs = Column(String(3000))
    habitat = Column(String(3000))


class FuncPeipsiBirds:
    @staticmethod
    def add_bird(bird_data: dict):
        birds = PeipsiBirds(
            order=bird_data['order'], 
            family=bird_data['family'],
            name_rus=bird_data['name_rus'], 
            name_lat=bird_data['name_lat'], 
            signs=bird_data['signs'],
            habitat=bird_data['habitat']
            )
            
        if bird_data['name_rus'] not in [birds.name_rus for birds in FuncPeipsiBirds.get_birds()]:
            session.add(birds)
            session.commit()
    
    @staticmethod
    def get_birds():
        birds = session.query(PeipsiBirds).all()
        return birds
