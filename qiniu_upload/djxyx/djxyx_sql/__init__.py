from qiniu_upload.djxyx.djxyx_sql.table_data_2_qiuniu import Data2Qiniu, query_data2Qiniu, insert_data2Qiniu
from .table_category_info import CategoryInfo, insert_categoryInfo
from .table_game_info import GameInfo, insert_gameInfo, queryGameInfo
from .table_game_info_2_category_info import GameInfo2CategoryInfo, insert_gameInfo2CategoryInfo
from .table_game_info_2_tag_info import GameInfo2TagInfo, insert_gameInfo2TagInfo_not_exists
from .table_game_info_2_version_info import GameInfo2VersionInfo, insert_GameInfo2VersionInfo_not_exists, query_GameInfo2VersionInfo
from .table_tag_info import TagInfo, insert_tagInfo
from .table_version_info import VersionInfo, insert_versionInfo, query_versionInfo
from .sql_base import session, create_tables, commit

__all__ = [
    session,
    CategoryInfo,
    GameInfo,
    GameInfo2CategoryInfo,
    GameInfo2TagInfo,
    GameInfo2VersionInfo,
    TagInfo,
    VersionInfo,
    Data2Qiniu,
    insert_gameInfo2TagInfo_not_exists,
    insert_tagInfo,
    insert_versionInfo,
    insert_categoryInfo,
    insert_gameInfo,
    insert_GameInfo2VersionInfo_not_exists,
    commit,
    query_versionInfo,
    query_GameInfo2VersionInfo,
    queryGameInfo,
    insert_data2Qiniu,
    query_data2Qiniu
]
create_tables()
