#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 10:30
# @Author  : CoderCharm
# @File    : test_aioredis.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

测试aioredis

本来是想直接使用redsi的， 但是查阅资料都是使用aioredis

看了很多在FastAPI中使用redis的demo

所以参照着写,把redsi挂载到fastapi app上 在/app/api/__init__.py register_redis函数

使用，从request对象中拿到redis对象
request.app.state.redis


https://github.com/tiangolo/fastapi/issues/1694
https://github.com/tiangolo/fastapi/issues/1742
https://github.com/leonh/redis-streams-fastapi-chat/blob/master/chat.py


import aioredis

async def gen_redis():
    try:
        redis_cli = await aioredis.create_redis_pool(
            ("172.16.137.129", 6379), password="root12345", encoding='utf-8')
        print("返回cli")
        yield redis_cli
    finally:
        print("关闭执行了")
        # https://aioredis.readthedocs.io/en/v1.3.0/api_reference.html#aioredis.RedisConnection.wait_closed
        await redis_cli.wait_closed()


async def a():
    print("开始")
    r = await gen_redis().__anext__()
    print("收到了")
    await r.set("a", 123)
    print("结束了")


asyncio.run(a())

"""

import asyncio

from aioredis import create_redis_pool, Redis

from fastapi import FastAPI, Request, Query

app = FastAPI()


async def get_redis_pool() -> Redis:
    redis = await create_redis_pool(f"redis://:root12345@172.16.137.129:6379/0?encoding=utf-8")
    return redis


@app.on_event('startup')
async def startup_event():
    """
    获取链接
    :return:
    """
    app.state.redis = await get_redis_pool()


@app.on_event('shutdown')
async def shutdown_event():
    """
    关闭
    :return:
    """
    app.state.redis.close()
    await app.state.redis.wait_closed()


@app.get("/test", summary="测试redis")
async def test_redis(request: Request, num: int=Query(123, title="参数num")):
    # redis写入  await异步变同步
    await request.app.state.redis.set("aa", num)
    # redis读取
    v = await request.app.state.redis.get("aa")
    print(v, type(v))
    return {"msg": v}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='test_aioredis:app', host="127.0.0.1", port=8080, reload=True, debug=True)

