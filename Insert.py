from tbay import User, Item,Bid, session

ade=User(username = 'adek',password = 'jjkkkk')
phil=User(username="philj", password="jihsk")
jolade=User(username="joladew", password="huip")
Baseball= Item(name="Nike",description="sports shoes", seller=ade)
bid1=Bid(price=3.00,bidder=phil, item_bid=Baseball)
bid2=Bid(price=5.00, bidder=jolade, item_bid=Baseball)
Baseball.price=[3.00,5.00]

session.add_all([ade, Baseball,phil, jolade, bid1, bid2])
session.commit()

print (max(Baseball.price))