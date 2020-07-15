# Import all the models, so that Base has them before being
# imported by Alembic

# imported by Alembic # 方便在Alembic导入,迁移用

from api.db.base_class import Base  # noqa

from api.models.auth import AdminUser, AdminRole, MallUser, MallAddress, MallSearchHistory, MallSiteNotice

from api.models.express import MallFreightTemplate, MallRegion, MallShipper

from api.models.goods import MallGoods, MallBanner, MallGoodsGallery, MallGoodsKeywords, MallGoodsSpecification

from api.models.orders import MallOrder, MallCart, MallOrderExpress, MallOrderGoods