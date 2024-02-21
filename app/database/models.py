from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    #SQLAlchemy의 테이블 이름을 의미
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    status = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    #back_populates : 연관된 객체에서 지정된 속성을 찾아서 값을 동기화 해주는 옵션
    cart = relationship("Cart", back_populates="users")

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="carts")