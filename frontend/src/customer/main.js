import scss from './app.scss'

import Vue from 'vue'
import Resource from 'vue-resource'
import Router from 'vue-router'

import App from './components/App.vue'
import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Detail from './components/Detail.vue'
import Order from './components/Order.vue'
import Orderdetail from './components/Orderdetail.vue'
import About from './components/About.vue'

// Install plugins
Vue.use(Router)
Vue.use(Resource)

// Set up a new router
var router = new Router()

// Route config
router.map({
  '/login':{
    name: 'login',
    component: Login
  },
  '/home':{
    name: 'home',
    component: Home
  },
  '/home/:bussinessId':{
    name: 'detail',
    component: Detail
  },
  '/order':{
    name: 'order',
    component: Order
  },
  '/order/:orderId':{
    name: 'order_detail',
    component: Orderdetail
  },
  '/about':{
    name: 'about',
    component: About
  }
})

// For every new route scroll to the top of the page
router.beforeEach(function () {
  window.scrollTo(0, 0)
})

// If no route is matched redirect home
router.redirect({
  '*': '/home'
})

// Start up our app
router.start(App, '#app')
