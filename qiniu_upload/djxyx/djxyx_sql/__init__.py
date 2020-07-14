from .table_category_info import CategoryInfo
from .table_game_info import GameInfo
from .table_game_info_2_category_info import GameInfo2CategoryInfo
from .table_game_info_2_tag_info import GameInfo2TagInfo
from .table_game_info_2_version_info import GameInfo2VersionInfo
from .table_tag_info import TagInfo
from .table_version_info import VersionInfo
from .sql_base import session, create_tables

__all__ = [
    session,
    CategoryInfo,
    GameInfo,
    GameInfo2CategoryInfo,
    GameInfo2TagInfo,
    GameInfo2VersionInfo,
    TagInfo,
    VersionInfo
]
create_tables()
