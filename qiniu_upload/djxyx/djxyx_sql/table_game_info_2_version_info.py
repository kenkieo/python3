from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class GameInfo2VersionInfo(Base):
    __tablename__ = 'game_info_2_version_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    versionId = Column(Integer)
    gameId = Column(Integer)


def insert_GameInfo2VersionInfo_not_exists(versionId, gameId):
    gameInfo2VersionInfo = session.query(GameInfo2VersionInfo).filter_by(
        versionId=versionId, gameId=gameId).first()
    if not gameInfo2VersionInfo:
        gameInfo2VersionInfo = GameInfo2VersionInfo()
        gameInfo2VersionInfo.versionId = versionId
        gameInfo2VersionInfo.gameId = gameId
        session.add(gameInfo2VersionInfo)
        session.commit()
    return gameInfo2VersionInfo
