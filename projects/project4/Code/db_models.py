from sqlalchemy.orm import DeclarativeBase
import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20),unique=True)
    password: Mapped[str] = mapped_column(String(100))
    posts: Mapped[list["posts"]|None] = relationship("Post", back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    datetime_posted: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    content: Mapped[str] = mapped_column(String(2000))
    code: Mapped[str] = mapped_column(String(2000))
    code_language: Mapped[str] = mapped_column(String(20))
    like_count: Mapped[int] = mapped_column(Integer, default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped[Users] = relationship("Users", back_populates="posts")




