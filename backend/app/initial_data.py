
"""

创建初始化

角色以及用户

初始化配置信息在 app/core/config/

"""
import logging

from app.api.db.init_db import init_db
from app.api.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
