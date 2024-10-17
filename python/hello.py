import sys
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Mapper
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# CREATE TABLE user (
#     id varchar(20),
#     username varchar(255),
#     create_time varchar(255),
#     deleted_at varchar(255)
# )

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    username = Column(String(255)),
    create_time = Column(String(255))

engine = create_engine('mysql+mysqldb://root@localhost:3306/sql_test')
DBSession = sessionmaker(bind=engine)

def query_action(sort_by):
    lists = DBSession().query(User).order_by(sort_by)
    print('raw_sql：'+str(lists))
    return lists.all()

if __name__ == "__main__":
    print(sys.argv)
    result = query_action(sys.argv[1])
    for x in result:
        print x.id,x.create_time