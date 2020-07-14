from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base


class CategoryInfo(Base):
    __tablename__ = 'category_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
