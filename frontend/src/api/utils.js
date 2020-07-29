import request from '@/utils/request'

// 上传图片
export function UpLoadImg(data) {
  return request(
    '/utils/upload/file',
    'post',
    data
  )
}
