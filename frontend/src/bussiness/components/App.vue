<script>
  import Navbar from './Navbar.vue'

  export default {
    name: "App",

    components: {
      Navbar
    },

    data: function() {
      return {
      	foods: [
      	{id: 'food1',
      	picture: '../images/flower.jpg',
      	name: 'aaa',
      	price: 5,
        amount: 34},
        {id: 'food2',
      	picture: '../images/flower.jpg',
      	name: 'bbb',
      	price: 8,
        amount: 654},
        {id: 'food3',
      	picture: '../images/flower.jpg',
      	name: 'ccc',
      	price: 10,
        amount: 25},
        {id: 'food4',
      	picture: '../images/flower.jpg',
      	name: 'ddd',
      	price: 6,
        amount: 48},
        {id: 'food5',
      	picture: '../images/flower.jpg',
      	name: 'abc',
      	price: 2,
        amount: 209},
        {id: 'food6',
      	picture: '../images/flower.jpg',
      	name: 'bcd',
      	price: 7,
        amount: 234},
        {id: 'food7',
      	picture: '../images/flower.jpg',
      	name: 'bbd',
      	price: 1,
        amount: 254},
        {id: 'food8',
      	picture: '../images/flower.jpg',
      	name: 'eee',
      	price: 10,
        amount: 87},
        {id: 'food9',
      	picture: '../images/flower.jpg',
      	name: 'cde',
      	price: 9,
        amount: 342},
        {id: 'food10',
      	picture: '../images/flower.jpg',
      	name: 'ace',
      	price: 5,
        amount: 24},
        {id: 'food11',
      	picture: '../images/flower.jpg',
      	name: 'beg',
      	price: 5,
        amount: 34},
        {id: 'food12',
      	picture: '../images/flower.jpg',
      	name: 'dkl',
      	price: 5,
        amount: 112},
        {id: 'food13',
      	picture: '../images/flower.jpg',
      	name: 'ads',
      	price: 5,
        amount: 48},
        {id: 'food14',
      	picture: '../images/flower.jpg',
      	name: 'dad',
      	price: 5,
        amount: 29}
      	],
      	searchText: '',
      	bussinessName: 'lalalal'
      }
    }
  }
</script>

<template>
  <div>
  	<navbar :search-text.sync="searchText" :bussiness-name="bussinessName"></navbar>
 	<router-view :foods.sync="foods" :search-text.sync="searchText"></router-view>
  </div>
</template>
