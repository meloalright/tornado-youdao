import Vue from 'vue'
import Router from 'vue-router'
import Button from '@/components/Button'
import Head from '@/components/Head'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/note/',
      name: 'Button',
      component: Button
    },

    {
      path: '/note/share/',
      name: 'Head',
      component: Head
    }
  ]
})
