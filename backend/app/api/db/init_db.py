from sqlalchemy.orm import Session

from app.api.api_v1.auth.schemas import user as user_schemas
from app.api.api_v1.auth.curd import curd_user
from app.core.config import settings


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    user = curd_user.get_by_email(db, email=settings.FIRST_MALL)

    if not user:
        user_in = user_schemas.UserCreate(
            nickname=settings.FIRST_SUPERUSER,
            email=settings.FIRST_MALL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            role_id=settings.FIRST_ROLE
        )
        user = curd_user.create(db, obj_in=user_in)  # noqa: F841
        print(f"用户创建成功")
    else:
        print("此邮箱已经注册过了")
