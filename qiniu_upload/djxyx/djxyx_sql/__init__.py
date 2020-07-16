from .table_category_info import CategoryInfo, insert_categoryInfo
from .table_game_info import GameInfo, insert_gameInfo
from .table_game_info_2_category_info import GameInfo2CategoryInfo, insert_gameInfo2CategoryInfo
from .table_game_info_2_tag_info import GameInfo2TagInfo, insert_gameInfo2TagInfo_not_exists
from .table_game_info_2_version_info import GameInfo2VersionInfo, insert_GameInfo2VersionInfo_not_exists
from .table_tag_info import TagInfo, insert_tagInfo
from .table_version_info import VersionInfo, insert_versionInfo
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
    insert_gameInfo2TagInfo_not_exists,
    insert_tagInfo,
    insert_versionInfo,
    insert_categoryInfo,
    insert_gameInfo,
    insert_GameInfo2VersionInfo_not_exists,
    commit
]
create_tables()
