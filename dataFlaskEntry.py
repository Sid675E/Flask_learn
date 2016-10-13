from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataFlask import data_Flask,User,Base
from passlib.apps import custom_app_context as pwd_context

engine = create_engine('postgresql+psycopg2://postgres:XxxAahSn@2*5@localhost/restr')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


Item1 = data_Flask(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce")

session.add(Item1)
session.commit()


Item2 = data_Flask(name="French Fries", description="with garlic and parmesan")

session.add(Item2)
session.commit()

Item3 = data_Flask(name="French Fries", description="with garlic and parmesan")

session.add(Item3)
session.commit()


user1 = User(username="Sidra", password_hash=pwd_context.encrypt("h"))
session.add(user1)
session.commit()

user2 = User(username="Ahmed", password_hash=pwd_context.encrypt("humpty"))
session.add(user2)
session.commit()