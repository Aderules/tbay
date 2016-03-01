from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

#item_user_table = Table('item_user_association', Base.metadata,
      #Column ('items_id', Integer, ForeignKey('items_id')),
      #Column ('users_id', Integer, ForeignKey('users_id'))
#)


class Item(Base):
    __tablename__= 'items'
    
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
   
    seller_id= Column(Integer, ForeignKey ('users.id'), nullable=False)
    bids_made= relationship('Bid', backref='item_bid') 
   
    
class User(Base):
    __tablename__='users'
    
    id= Column(Integer, primary_key=True)
    username=Column(String, nullable=False)
    password=Column(String, nullable=False)
   
    item = relationship('Item', backref='seller')
    bid=relationship("Bid", backref="bidder")
    
    
class Bid(Base):
    __tablename__='bids'
    
    id=Column(Integer, primary_key=True)
    price=Column(Float, nullable=False)
    
    bidder_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    item_bid_id= Column(Integer, ForeignKey('items.id'), nullable=False) 
 
    
    
#user_bid_table = Table('user_bid_association', Base.metadata, 
     #Column('users_id', Integer, ForeignKey('users_id')),
     #Column('bids_id', Integer, ForeignKey('bids_id'))
#)
   
    
Base.metadata.create_all(engine)



