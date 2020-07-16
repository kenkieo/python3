from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class TagInfo(Base):
    __tablename__ = 'tag_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


def insert_tagInfo(tag):
    tagInfo = session.query(TagInfo).filter_by(name=tag).first()
    if not tagInfo:
        tagInfo = TagInfo()
        tagInfo.name = tag
        session.add(tagInfo)
        session.commit()
    return tagInfo
