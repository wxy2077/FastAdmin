# Import all the models, so that Base has them before being
# imported by Alembic

# imported by Alembic # 方便在Alembic导入,迁移用

from app.api.db.base_class import Base  # noqa

from app.api.models.auth import AdminUser, AdminRole
