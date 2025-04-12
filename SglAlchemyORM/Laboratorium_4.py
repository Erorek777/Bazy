from typing import Optional, Annotated, List
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, \
    relationship  # Mapped jest klasą generyczną można w [] podawać typ danych
import datetime

str255 = Annotated[str, mapped_column(String(255))]
intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

library_metadata = MetaData(schema='library_orm')

class Base(DeclarativeBase):
    metadata = library_metadata

class User(Base):
    __tablename__ = 'user'

    id: Mapped[intpk]
    first_name: Mapped[str255]
    last_name: Mapped[str255]
    middle_name: Mapped[str255]

class Carts(Base):
    __tablename__ = 'carts'
    cards_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    middle_name: Mapped[datetime.date]

class Carts_products(Base):
    __tablename__ = 'carts_products'
    cards_id: Mapped[int] = mapped_column(ForeignKey('cards.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products_id'))

class Products(Base):
    __tablename__ = 'products'
    product_id: Mapped[int]
    tittle: Mapped[str255]
    description: Mapped[str255]
    price: Mapped[float]




