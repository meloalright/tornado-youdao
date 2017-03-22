import Vue from 'vue'
import Router from 'vue-router'
import Head from '@/components/Head'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Head',
      component: Head
    },

    {
      path: '/note/(.*)',
      name: 'Head',
      component: Head
    }
  ]
})
