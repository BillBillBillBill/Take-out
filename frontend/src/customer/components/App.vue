<script>
  import Navbar from './Navbar.vue'

  export default {
    name: "App",

    components: {
      'navbar': Navbar
    },

    data: function() {
      return {
        business: [
          {
           id: 1,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://www.baidu.com',
           title: '一饭',
           number: '12345',
           count: 23,
           star: 3},
          {
           id: 2,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '二饭',
           number: '123456',
           count: 89,
           star: 4},
          {
           id: 3,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '三饭',
           number: '456789',
           count: 46,
           star: 2},
          {
           id: 4,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '四饭',
           number: '3456789',
           count: 294,
           star: 5},
          {
           id: 5,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '五饭',
           number: '1236789',
           count: 67,
           star: 2},
          {
           id: 6,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '六饭',
           number: '123459',
           count: 987,
           star: 5},
          {
           id: 7,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '七饭',
           number: '12349',
           count: 3,
           star: 1},
          {
           id: 8,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '八饭',
           number: '456789',
           count: 24,
           star: 2},
          {
           id: 9,
           picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '九饭',
           number: '16789',
           count: 109,
           star: 4}
        ],
        searchText: ''
      }
    }
  }

</script>

<template>
  <div>
    <navbar :search-text.sync="searchText"></navbar>
    <router-view :business.sync="business" :search-text.sync="searchText"></router-view>
  </div>
</template>
