from orm_connection import Session
from sqlalchemy import *
from sqlalchemy.orm import joinedload
from alchemy_orm import Author, Address, Book
import datetime

session = Session()

# select_authors = select(Author).options(joinedload(Author.books), joinedload(Author.address))
select_authors = select(Author).options(joinedload(Author.books), joinedload(Author.address)).filter_by(id=1)
# select_authors = select(Author).options(joinedload(Author.books), joinedload(Author.address)).where(Author.id > 1)
# all_authors = session.execute(select_authors).scalars().unique().all()
a = session.execute(select_authors).unique().scalar_one() # tylko jeden autor


# for a in all_authors:
#     print(f'Autor{a.name} napisał{len(a.books)} książki i mieszka w {a.address.country} {a.address.city}')


print(f'Autor{a.name} napisał{len(a.books)} książki i mieszka w {a.address.country} {a.address.city}')

# print(all_authors)

#jeden autor -2
a = session.get(Author, 9999)
print(a)

# Insert
# author = Author(name='Andrzej', email='email', login='login', middle_name='middle')
# author.address = Address(country='Litwa', city='Wilno')
# author.books = [
#     Book(title='Jeden', publication_date = datetime.date.today()),
#     Book(title='Dwa', publication_date = datetime.date.today()),
# ]

# session.add(author)
# session.commit()

# Update
author = session.get(Author, 7)
author.middle_name = 'Jan'
for b in author.books:
    if b.title == 'Jeden':
        b.description = 'To jest pierwsza ksiażka!'

session.add(author)
session.commit()


# author = session.get(Author, 7)
# author.middle_name = 'Jan'
# author.books=author


#delete
author = session.get(Author, 7)
session.delete(author)
session.commit()












