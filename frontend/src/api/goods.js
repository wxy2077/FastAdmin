import request from '@/utils/request'

export function addCategory(data) {
  return request(
    '/goods/add/category',
    'post',
    data
  )
}

export function delCategory(data) {
  return request(
    '/goods/del/category',
    'post',
    data
  )
}

export function modifyCategory(data) {
  return request(
    '/goods/modify/category',
    'post',
    data
  )
}

export function getCategory(data) {
  return request(
    '/goods/query/category',
    'get',
    data
  )
}

export function getCategoryList(data) {
  return request(
    '/goods/query/category/list',
    'get',
    data
  )
}
