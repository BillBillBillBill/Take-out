import scss from './app.scss'

import Vue from 'vue'
import Resource from 'vue-resource'
import Router from 'vue-router'

import App from './components/App.vue'
import Home from './components/Home.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import Complain from './components/Complain.vue'
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
  '/register':{
    name: 'register',
    component: Register
  },
  '/home':{
    name: 'home',
    component: Home
  },
  '/complain':{
    name: 'complain',
    component: Complain
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
