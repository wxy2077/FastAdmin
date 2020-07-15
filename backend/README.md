# 后台API

## 后台API服务

```
pip install pydantic[email]

```

## 项目文件组织
> 参考Django文件组织,FastAPI官方推荐项目生成,Flask工厂函数。

<details>
<summary>项目文件结构</summary>

```
/alembic                         // alembic 自动生成的迁移配置文件夹,迁移不正确时 产看其中的env.py文件
alembic.ini                      // alembic 自动生成的迁移配置文件
app
|____core                        
| |______init__.py
| |____config                    // 配置文件
| | |______init__.py             // 根据虚拟环境导入不同配置
| | |____development_config.py   // 开发配置
| | |____production_config.py    // 生成配置
| |____security.py               // token password验证          
|____tests
| |______init__.py
|______init__.py
|____api                         // API文件夹
| |____api_v1                    // 版本区分
| | |____auth                    // auth模块
| | | |______init__.py
| | | |____schemas               // 验证model文件夹
| | | | |____user.py             // user验证
| | | | |______init__.py
| | | |____curd                  // curd 文件夹
| | | | |____user.py             // user curd操作
| | | | |______init__.py
| | | |____views.py              // 各模块视图函数
| | |______init__.py
| | |____api.py                  // 路由函数
| |______init__.py
| |____utils                     // 工具类文件夹
| | |____custom_exc.py           // 自定义异常
| | |____response_code.py        // 统一自定义响应状态
| |____models                    // 项目models 文件(我没像django那样放到各模块下面,单独抽出来了)
| | |______init__.py
| | |____auth.py                 // 用户权限相关的
| | |____goods.py                // 商品相关
| | |____shop.py                 // 店铺相关
| |____extensions                // 扩展文件夹
| | |______init__.py
| | |____logger.py               // 扩展日志 loguru 简单配置
| |____common                    // 通用文件夹
| | |______init__.py
| | |____deps.py                 // 通用依赖文件,如数据库操作对象,权限验证对象
| | |____curd_base.py            // curd_base对象
| | |____model_base.py           // model继承base对象(报错暂时不用)
| |____logs
| |____db                        // 数据库
| | |______init__.py
| | |____base_class.py           
| | |____session.py              // 
| | |____base.py                 // 导出全部models 给alembic迁移用
| | |____init_db.py              // 初始化数据
|____utils.py
|____main.py
|____initial_data.py



```

</details>


## alembic 生成表

#### 自动生成迁移文件
> 删除/alembic/versions/文件夹下的文件, 然后在重新提交

```shell
alembic revision --autogenerate -m "init commit"
```

#### 路径问题

```python
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(f"当前路径:{BASE_DIR}")
# /Users/xxxx/MyFile/python_code/FastAdmin/backend

sys.path.insert(0, BASE_DIR) 
# 如果还不行，那就简单直接点 直接写固定
# sys.path.insert(0, "/你的路径/FastAdmin/backend") 

```


#### 生成表
> alembic upgrade head


## 初始化账号密码 

#### 生成初始化账号密码

```shell
cd app
python initial_data.py

```


```shell
username: wg_python@163.com
password: admin12345
```







## 参考


- [alembic导入app noqa](https://stackoverflow.com/questions/32032940/how-to-import-the-own-model-into-myproject-alembic-env-py):https://stackoverflow.com/questions/32032940/how-to-import-the-own-model-into-myproject-alembic-env-py
- [alembic教程](https://alembic.sqlalchemy.org/en/latest/tutorial.html) https://alembic.sqlalchemy.org/en/latest/tutorial.html
- [alembic迁移](https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration): https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration
- [海风小店](https://raw.githubusercontent.com/iamdarcy/hioshop-server/master/hiolabsDB.sql) https://raw.githubusercontent.com/iamdarcy/hioshop-server/master/hiolabsDB.sql
- 