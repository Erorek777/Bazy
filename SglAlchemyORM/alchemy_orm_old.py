import datetime
from typing import Optional, Annotated, List
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

str255 = Annotated[str, mapped_column(String(255))]
intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

library_metadata = MetaData(schema='Library_orm')

Base = DeclarativeBase
class Base(DeclarativeBase):
    metadata = library_metadata

    event_autors = Table(
        'event_autors',
        Base.metadata,
        Column('autors_id', ForeignKey('autors.id')),
    )
    # type_annotation_map = {
    #    str255: String(255)
    # }

class Author(Base):
    __tablename__ = 'author'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    # id = Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id: Mapped[intpk]
    # name = Column(String) #varchar(max)
    name: Mapped[str]
    # email = Column(String(255))
    # email = Mapped[str] = mapped_column(String(255))
    email: Mapped[str255]
    # login = Column(String(100), default='No Login')
    login: Mapped[str] = mapped_column(String(100), default='No Login')
    # middle_name = Column(String(255), nullable=True)
    middle_name: Mapped[Optional[str]]

    book: Mapped[List['Book']] = relationship(back_populates='author', cascade='delete, delete-orphan') #u orphane suń sierote
    Address: Mapped[List['Address']] = relationship(back_populates='author', cascade='delete, delete-orphan')
class Address(Base):
    __tablename__ = 'address'

    id: Mapped[intpk]
    country: Mapped[str255]
    city: Mapped[str255]
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))
    author: Mapped[Author] = relationship(relationship(back_populates='addresses'))


class Book(Base):
    __tablename__ = 'author'

    id: Mapped[intpk]
    title: Mapped[str255]
    description: Mapped[Optional[str]]
    publication_date: Mapped[datetime.date]

    author_id: Mapped[int] = mapped_column(ForeignKey('autor.id'))

    autor: Mapped['Author'] = relationship(back_populates='books')







