import request from '@/utils/request'

export function login(data) {
  return request(
    '/auth/login/access-token',
    'post',
    data
  )
}

export function getInfo(token) {
  return request(
    '/auth/user/info',
    'get',
    token
  )
}

export function logout() {
  return request(
    '/auth/user/logout',
    'post'
  )
}
