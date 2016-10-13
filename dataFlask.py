from sqlalchemy.ext.declarative import declarative_base
##### Use in configuration and class code ######
from sqlalchemy.orm import relationship, sessionmaker
##### For creating foriegn key relationship #####
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from passlib.apps import custom_app_context as pwd_context
##### Used for creating hash codes and verification #####
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
##### For cryptographically signed tokens #####

Base = declarative_base()
#####Instance of the declarative_base Class imported above #####
####### insert at end of the file ######

secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

class User(Base):
    __tablename__ = 'user1'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(100))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=6000):
        s = Serializer(secret_key, expires_in = expiration)
        return s.dumps({'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            #Valid Token, but expired
            return None
        except BadSignature:
            #Invalid Token
            return None
        user_id = data['id']
        return user_id


class data_Flask(Base):
    __tablename__ = 'data_flask'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))

    # We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }

engine = create_engine('postgresql+psycopg2://postgres:XxxAahSn@2*5@localhost/restr')


Base.metadata.create_all(engine)