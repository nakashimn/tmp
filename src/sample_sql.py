import pandas as pd
import sqlalchemy
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.dialects.sqlite import insert as sqlite_upsert

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(String)

SqlEngine: Engine = sqlalchemy.create_engine("sqlite:///tmp.sqlite")
session: Session = sessionmaker(SqlEngine)()

# ids = ["1","2","3"]
# str_ids = ",".join(ids)
# df_table = pd.read_sql(sql=f"select * from user where id in ({str_ids});", con=SqlEngine)
df_table = pd.read_sql(sql=f"select * from user;", con=SqlEngine)
df_tmp = pd.DataFrame({
    "id": [6],
    "name": ["George"]
})
df_table.loc[df_table["id"]==1, "name"] = "Bob"
df_table = pd.concat([df_tmp, df_table], ignore_index=True)
# df_table.to_sql(name="user", con=SqlEngine, if_exists="replace", index=False)

bulk = df_table.to_dict(orient="records")
for b in bulk:
    record = session.query(User).filter(User.id==b["id"]).one_or_none()
    if record is None:
        session.add(User(**b))
        continue
    record.name = b["name"]
session.commit()
