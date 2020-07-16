from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session
from qiniu_upload.djxyx.djxyx_sql.sql_base import engine


class Data2Qiniu(Base):
    __tablename__ = 'data2qiniu'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    icon = Column(Text)
    url = Column(Text)


def insert_data2Qiniu(id, url, icon):
    data2Qiniu = session.query(Data2Qiniu).filter_by(id=id).first()
    if not data2Qiniu:
        data2Qiniu = Data2Qiniu()
        data2Qiniu.id = id
        data2Qiniu.url = url
        data2Qiniu.icon = icon
        session.add(data2Qiniu)
        session.commit()
    return data2Qiniu


def query_data2Qiniu(id):
    return session.query(Data2Qiniu).filter_by(id=id).first()


if __name__ == "__main__":
    Base.metadata.create_all(engine, checkfirst=True)
