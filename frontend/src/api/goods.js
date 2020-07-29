import request from '@/utils/request'

// 添加分类
export function addCategory(data) {
  return request(
    '/goods/add/category',
    'post',
    data
  )
}

// 删除分类
export function delCategory(data) {
  return request(
    '/goods/del/category',
    'post',
    data
  )
}

// 修改分类
export function modifyCategory(data) {
  return request(
    '/goods/modify/category',
    'post',
    data
  )
}

// 开启分类
export function enabledCategory(data) {
  return request(
    '/goods/enabled/category',
    'post',
    data
  )
}

// 获取分类
export function getCategory(data) {
  return request(
    '/goods/query/category',
    'get',
    data
  )
}

// 获取全部分类
export function getCategoryList(data) {
  return request(
    '/goods/query/category/list',
    'get',
    data
  )
}

// 通过name和front_desc查询分类
export function searchCategoryList(data) {
  return request(
    '/goods/search/category',
    'post',
    data
  )
}
