from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base


class GameInfo2CategoryInfo(Base):
    __tablename__ = 'game_info_2_category_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    categoryId = Column(Integer)
    gameId = Column(Integer)
