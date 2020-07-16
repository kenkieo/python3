from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session
from qiniu_upload.djxyx.djxyx_sql.sql_base import engine
from hashlib import md5


class Data2Qiniu(Base):
    __tablename__ = 'data2qiniu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    icon = Column(Text)
    url = Column(Text)


def insert_gameInfo(id):
    gameInfo = session.query(GameInfo).filter_by(id=id).first()
    if not gameInfo:
        gameInfo = GameInfo()
        gameInfo.id = id
        gameInfo.icon = icon
        gameInfo.name = name
        gameInfo.info = info
        md5_util = md5()
        md5_util.update(gameInfo.name.encode())
        gameInfo.md5 = md5_util.hexdigest()
        session.add(gameInfo)
    return gameInfo


if __name__ == "__main__":
    Base.metadata.create_all(engine, checkfirst=True)
