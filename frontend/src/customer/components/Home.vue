<script>
  export default {
    name: "Home",
    data: function() {
      return {
        business: [
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '一饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '二饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '三饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '四饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '五饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '六饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '七饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '八饭',
           number: '123456789'},
          {picture: '../images/flower.jpg',
           alt: 'flower',
           myurl: 'http://baidu.com',
           title: '九饭',
           number: '123456789'}
        ]
      }
    }
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 large-up-4" id="customer-home">
    <template v-for="item in business">
      <div class="column">
        <a v-bind:href="item.myurl">
          <div class="row customer-item" small-2>
            <div class="column">
              <img :src="item.picture" />
            </div>
            <div class="column">
              <div class="row">
                {{item.title}}
              </div>
              <div class="row">
                {{item.number}}
              </div>
            </div>
          </div>
        </a>
      </div>
    </template>
  </div>
</template>
