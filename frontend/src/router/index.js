import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'el-icon-s-home' }
    }]
  },
  {
    path: '/goods',
    component: Layout,
    redirect: '/goods/display',
    name: 'Goods',
    meta: { title: '商品管理', icon: 'el-icon-s-goods' },
    children: [
      {
        path: 'display',
        component: () => import('@/views/goods/display/index'), // Parent router-view
        name: 'Display',
        meta: { title: '商品列表', icon: 'el-icon-tickets' }
      },
      {
        path: 'setting',
        component: () => import('@/views/goods/setting/index'),
        name: 'Setting',
        meta: { title: '商品设置', icon: 'el-icon-setting' }
      },
      {
        path: 'add',
        component: () => import('@/views/goods/add/index'),
        name: 'Setting',
        meta: { title: '添加商品', icon: 'el-icon-folder-add' }
      }
    ]
  },
  {
    path: '/orders',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Orders',
        component: () => import('@/views/orders/index'),
        meta: { title: '订单', icon: 'el-icon-s-order' }
      }
    ]
  },
  {
    path: '/user',
    component: Layout,
    children: [{
      path: 'index',
      name: 'User',
      component: () => import('@/views/user/index'),
      meta: { title: '用户管理', icon: 'el-icon-user-solid' }
    }]
  },
  {
    path: '/cart',
    component: Layout,
    children: [{
      path: 'index',
      name: 'Cart',
      component: () => import('@/views/cart/index'),
      meta: { title: '购物车', icon: 'el-icon-shopping-cart-full' }
    }]
  },
  {
    path: '/shop',
    component: Layout,
    name: 'Shop',
    meta: { title: '店铺设置', icon: 'el-icon-office-building' },
    children: [
      {
        path: 'ad',
        component: () => import('@/views/shop/ad/index'), // Parent router-view
        name: 'Ad',
        meta: { title: '广告设置', icon: 'el-icon-reading' }
      },
      {
        path: 'display',
        component: () => import('@/views/shop/display/index'), // Parent router-view
        name: 'Display',
        meta: { title: '显示设置', icon: 'el-icon-monitor' }
      },
      {
        path: 'freight',
        component: () => import('@/views/shop/freight/index'), // Parent router-view
        name: 'freight',
        meta: { title: '运费模版', icon: 'el-icon-printer' }
      },
      {
        path: 'shipper',
        component: () => import('@/views/shop/shipper/index'), // Parent router-view
        name: 'Shipper',
        meta: { title: '快递设置', icon: 'el-icon-takeaway-box' }
      },
      {
        path: 'notice',
        component: () => import('@/views/shop/notice/index'), // Parent router-view
        name: 'Notice',
        meta: { title: '公告', icon: 'el-icon-message-solid' }
      }
    ]
  },
  // 个人中心
  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: () => import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: '个人中心', icon: 'user', noCache: true }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }

]

const createRouter = () => new Router({
  mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
