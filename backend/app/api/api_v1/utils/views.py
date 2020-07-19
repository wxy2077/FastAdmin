#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:30
# @Author  : CoderCharm
# @File    : views.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

https://fastapi.tiangolo.com/tutorial/request-forms-and-files/

上传文件一定要安装这个库(粗心没注意第一行，卡了俩小时)
pip install python-multipart

https://github.com/tiangolo/fastapi/issues/426#issuecomment-542828790

"""
import os
import shutil
from pathlib import Path
from typing import Union, Any
from tempfile import NamedTemporaryFile
from fastapi import APIRouter, Depends, File, UploadFile

from api.common import deps
from api.extensions import logger
from core.config import settings
from api.utils import response_code

router = APIRouter()


@router.post("/upload/file/", summary="上传图片")
async def upload_image(
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        file: UploadFile = File(...)
):
    logger.info(f"用户{token_data.sub}->上传文件:{file.filename}")

    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = f"{settings.BASE_DIR}/assets"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return response_code.resp_200(data={"image": f"http://127.0.0.1:8010/assets/{tmp_file_name}"})
