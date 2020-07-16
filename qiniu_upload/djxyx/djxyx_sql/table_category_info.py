from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class CategoryInfo(Base):
    __tablename__ = 'category_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))


def insert_categoryInfo(id, name):
    category = session.query(CategoryInfo) \
        .filter_by(id=id).first()
    if not category:
        category = CategoryInfo()
        category.id = id
        category.name = name
        session.add(category)
        session.commit()
    return category
