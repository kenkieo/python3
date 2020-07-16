from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session
from qiniu_upload.djxyx.djxyx_sql.sql_base import engine
from hashlib import md5


class GameInfo(Base):
    __tablename__ = 'game_info'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    icon = Column(Text)
    name = Column(String(32))
    info = Column(Text)
    md5 = Column(String(32))


def insert_gameInfo(id, icon, name, info):
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


def queryGameInfoList():
    return session.query(GameInfo)


def queryGameInfo(id):
    return session.query(GameInfo).filter_by(id=id).first()


if __name__ == "__main__":
    Base.metadata.create_all(engine, checkfirst=True)
