from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class GameInfo2CategoryInfo(Base):
    __tablename__ = 'game_info_2_category_info'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    categoryId = Column(Integer)
    gameId = Column(Integer)


def insert_gameInfo2CategoryInfo(categoryId, gameId):
    gameInfo2CategoryInfo = session.query(GameInfo2CategoryInfo) \
        .filter_by(categoryId=categoryId, gameId=gameId).first()
    if not gameInfo2CategoryInfo:
        gameInfo2CategoryInfo = GameInfo2CategoryInfo()
        gameInfo2CategoryInfo.categoryId = categoryId
        gameInfo2CategoryInfo.gameId = gameId
        session.add(gameInfo2CategoryInfo)
        session.commit()
    return gameInfo2CategoryInfo
