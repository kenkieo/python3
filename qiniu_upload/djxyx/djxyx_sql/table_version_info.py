from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text

from qiniu_upload.djxyx.djxyx_sql.sql_base import Base, session


class VersionInfo(Base):
    __tablename__ = 'version_info'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text)
    total_size = Column(Integer)
    version_name = Column(Text)
    version_code = Column(Integer)
    orientation = Column(Integer)


def insert_versionInfo(url, total_size, version_name, versionCode, orientation):
    versionInfo = session.query(VersionInfo) \
        .filter_by(url=url).first()
    if not versionInfo:
        versionInfo = VersionInfo()
        versionInfo.url = url
        versionInfo.total_size = total_size
        versionInfo.version_name = version_name
        versionInfo.version_code = versionCode
        versionInfo.orientation = orientation
        session.add(versionInfo)
        session.commit()
    return versionInfo


def query_versionInfo():
    return session.query(VersionInfo).all()


if __name__ == "__main__":
    versionList = query_versionInfo()
    print(len(versionList))