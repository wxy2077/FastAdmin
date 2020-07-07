#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 15:17
# @Author  : CoderCharm
# @File    : main.py
# @Software: PyCharm
# @Desc    :
"""

pip install uvicorn

# 推荐启动方式 main指当前文件名字 app指FastAPI对象名称
uvicorn main:app --host=127.0.0.1 --port=8010 --reload


类似flask 工厂模式创建

# 生产启动命令 去掉热重载 (可用supervisor托管后台运行)
uvicorn main:app --host=127.0.0.1 --port=8010

"""


from app.api import create_app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True)

