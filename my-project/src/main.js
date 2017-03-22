// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

import Header from './header/App'
import header_router from './router/header_router'

import Note from './note/App'
import router from './router/index'

Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  el: '#header',
  router: header_router,
  template: '<Header/>',
  components: { Header }
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  template: '<Note/>',
  components: { Note }
})