from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'people'
#
#     ssn = Column("ssn", Integer, primary_key=True)
#     first_name = Column("first_name", String)
#     last_name = Column("last_name", String)
#     gender = Column("gender", CHAR)
#     age = Column("age", Integer)
#
#     def __init__(self, ssn, first_name, last_name, gender, age):
#         self.ssn = ssn
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age
#
#     def __repr__(self):
#         return f"({self.ssn}){self.first_name}{self.last_name}({self.gender}{self.age})"
#
#
# engine = create_engine('sqlite:///mydb.db', echo=True)
# Base.metadata.create_all(bind=engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# person = Person(123, "John", "choure", 'female', 89)
# session.add(person)
# session.commit()
#
# p1 = Person(1233, 'anna', 'blue', 'f', 20)
# p2 = Person(1343, 'bob', 'corge', 'f', 20)
# p3 = Person(1533, 'angela', 'maxwell', 'm', 520)
#
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()


class Person(Base):
    __tablename__ = 'people'

    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}){self.first_name}{self.last_name}({self.gender}{self.age})"



class Thing(Base):
    __tablename__ = 'things'

    tid = Column('tid', Integer, primary_key=True)
    description = Column("description", String)
    owner = Column('owner', Integer, ForeignKey('people.ssn'))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}{self.description} owned by {self.owner})"





engine = create_engine('sqlite:///mydb12.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(123, "John", "choure", 'female', 89)
session.add(person)
session.commit()

p1 = Person(1233, 'anna', 'blue', 'f', 20)
p2 = Person(1343, 'bob', 'corge', 'f', 20)
p3 = Person(1533, 'angela', 'maxwell', 'm', 520)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()
results = session.query(Person).filter(Person.age > '100')
for i in results:
    print(i)


# class Thing(Base):
#     __tablename__ = 'things'
#
#     tid = Column('tid', Integer, primary_key=True)
#     description = Column("description", String)
#     owner = Column('owner', Integer, ForeignKey('people.ssn'))
#
#     def __init__(self, tid, description, owner):
#         self.tid = tid
#         self.description = description
#         self.owner = owner
#
#     def __repr__(self):
#         return f"({self.tid}{self.description} owned by {self.owner})"


t1 = Thing(1, "car", p1.ssn)
t2 = Thing(2, "laptop", p2.ssn)
t3 = Thing(3, "ps5", p3.ssn)
t4 = Thing(4, "tool", p3.ssn)
t5 = Thing(5, "book", p1.ssn)
session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()

# results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(person.first_name == "Anna").all()
# for r in results:
#     print(r)
