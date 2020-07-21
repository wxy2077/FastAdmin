import request from '@/utils/request'

export function getList(params) {
  return request(
    '/auth/table/list',
    'get',
    params
  )
}
