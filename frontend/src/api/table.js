import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/auth/table/list',
    method: 'get',
    params
  })
}
