from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base

from qiniu_upload.djxyx.djxyx_sql.sql_base import engine


class GameInfo(Base):
    __tablename__ = 'game_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    icon = Column(Text)
    name = Column(String(32))
    info = Column(Text)
    md5 = Column(String(32))


if __name__ == "__main__":
    Base.metadata.create_all(engine, checkfirst=True)
