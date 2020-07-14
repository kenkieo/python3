from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base


class VersionInfo(Base):
    __tablename__ = 'version_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text)
    total_size = Column(Integer)
    version_name = Column(Text)
    version_code = Column(Integer)
    orientation = Column(Integer)
