from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class GameInfo2TagInfo(Base):
    __tablename__ = 'game_info_2_tag_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    tagId = Column(Integer)
    gameId = Column(Integer)


def insert_gameInfo2TagInfo_not_exists(tagId, gameId):
    gameInfo2TagInfo = session.query(GameInfo2TagInfo).filter_by(tagId=tagId, gameId=gameId).first()
    if not gameInfo2TagInfo:
        gameInfo2TagInfo = GameInfo2TagInfo()
        gameInfo2TagInfo.tagId = tagId
        gameInfo2TagInfo.gameId = gameId
        session.add(gameInfo2TagInfo)
        session.commit()
    return gameInfo2TagInfo
