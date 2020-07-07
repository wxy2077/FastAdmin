from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        import re
        # 转换表名字
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        # 表明格式替换成_格式 如 MallUser 替换成 mall_user
        return "_".join(name_list).lower()
