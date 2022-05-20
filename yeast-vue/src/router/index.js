import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CompaniesView from '../views/CompaniesView'
import TypesView from '../views/TypesView'
import CompaniesDetail from '../views/CompaniesDetail'
import TypesDetail from '../views/TypesDetail'
import AllProducts from '../views/AllProducts'
import YeastDetailAll from '../views/YeastDetailAll'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/companies',
    name: 'Companies',
    component: CompaniesView
  },
  {
    path: '/styles',
    name: 'Styles',
    component: TypesView
  },
  {
    path: '/companies/:company_slug',
    name: 'CompanyDetail',
    component: CompaniesDetail
  },
  {
    path: '/types/:type_slug',
    name: 'TypeDetail',
    component: TypesDetail
  },
  {
    path: '/all-products',
    name: 'AllProducts',
    component: AllProducts
  },
  {
    path: '/:slug',
    name: 'YeastDetailAll',
    component: YeastDetailAll
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
