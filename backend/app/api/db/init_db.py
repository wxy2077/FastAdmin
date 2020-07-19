from sqlalchemy.orm import Session

from api.api_v1.auth.schemas import user as user_schemas, role as role_schemas

from api.api_v1.auth.crud import curd_user, curd_role
from core.config import settings


# make sure all SQL Alchemy models are imported (db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    for temp_role in settings.DEFAULT_ROLE:
        role = curd_role.query_role(db, role_id=temp_role.get("role_id"))
        if not role:
            role_in = role_schemas.RoleCreate(
                role_id=temp_role.get("role_id"),
                role_name=temp_role.get("role_name"),
                permission_id=temp_role.get("permission_id"),
                re_mark=temp_role.get("re_mark")
            )
            role = curd_role.create(db, obj_in=role_in)
            print(f"角色创建成功:{role.role_name}")
        else:
            print(f"此角色id已存在:{role.role_id}")

    user = curd_user.get_by_email(db, email=settings.FIRST_MALL)

    if not user:
        user_in = user_schemas.UserCreate(
            nickname=settings.FIRST_SUPERUSER,
            email=settings.FIRST_MALL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            role_id=settings.FIRST_ROLE,
            avatar=settings.FIRST_AVATAR
        )
        user = curd_user.create(db, obj_in=user_in)  # noqa: F841
        print(f"{user.nickname}用户创建成功 角色id:{user.role_id}")
    else:
        print(f"{user.nickname}此用户邮箱:{user.email}已经注册过了")
