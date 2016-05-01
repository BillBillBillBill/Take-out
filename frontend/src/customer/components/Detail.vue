<script>
  import Orbitimages from './Orbitimages.vue'

  export default {
  	name: "Detail",

  	components: {
  	  'orbitimages': Orbitimages
  	},

    data: function() {
      return {
        businessdetail: [
          {
           id: 1,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 4,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '一饭',
           number: '12345',
           count: 23,
           star: 3},
          {
           id: 2,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '二饭',
           number: '123456',
           count: 89,
           star: 4},
          {
           id: 3,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '三饭',
           number: '456789',
           count: 46,
           star: 2},
          {
           id: 4,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '四饭',
           number: '3456789',
           count: 294,
           star: 5},
          {
           id: 5,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '五饭',
           number: '1236789',
           count: 67,
           star: 2},
          {
           id: 6,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '六饭',
           number: '123459',
           count: 987,
           star: 5},
          {
           id: 7,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '七饭',
           number: '12349',
           count: 3,
           star: 1},
          {
           id: 8,
                      foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           money: 5,
           title: '八饭',
           number: '456789',
           count: 24,
           star: 2},
          {
           id: 9,
           foods: [
            {food_name: 'a',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 23,
             star: 3},
             {food_name: 'b',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 45,
             star: 3},
             {food_name: 'c',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 133,
             star: 3},
             {food_name: 'd',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 65,
             star: 3},
             {food_name: 'e',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3},
             {food_name: 'f',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 143,
             star: 3},
             {food_name: 'g',
             picture: '../images/flower.jpg',
             alt: 'flower',
             myurl: 'http://www.baidu.com',
             money: 5,
             count: 543,
             star: 3}
           ],
           title: '九饭',
           number: '16789',
           count: 109,
           star: 4}
        ],
        currentid: this.$route.params.bussinessId-1,
        username: 'iii',
        shopping_cart: [],
        address: '',
        tel: ''
      }
    },
    methods: {
      addFood: function(foodname, money, num) {
        var isFind = false;
          for (var i = 0; i < this.shopping_cart.length; i++) {
            if (this.shopping_cart[i].food_name == foodname) {
              this.shopping_cart[i].amount += num;
              isFind = true;
              break;
            }
          }
          if (!isFind) {
            var temp = {};
            temp.food_name = foodname;
            temp.price = money;
            temp.amount = num;
            this.shopping_cart.push(temp);
          }
      },
      isValidate: function(event) {
        var address = $("#address").val();
        var tel = $("#tel").val();
        if (address == "" || tel == "") {
          return false;
        }
        var tel_reg = /^[1-9][0-9]{10}$/;
        if (tel_reg.test(tel)) {
          this.address = address;
          this.tel = tel;
          return true;
        } else alert("You should enter a valid telphone number.");
        event.preventDefault();
        return false;
      },
      emptyInput: function() {
        $("#address").val("");
        $("#tel").val("");
      }
      /*finishOrder: function() {
        alert("进入确认订单界面！");
      }*/
    }
  }
</script>

<template>
<div>
  <orbitimages></orbitimages>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <template v-for="item in businessdetail[currentid].foods">
      <div class="column">

        <div class="reveal" :id="item.food_name" data-reveal>
          <h2>{{item.food_name}}</h2>
          <img :src="item.picture" />
          <p>${{item.money}}</p>
          <p>{{item.count}}</p>
          <p>{{item.star}}</p>
          <div class="button expanded" data-open="order_again" v-on:click="addFood(item.food_name, item.money, 1)">加入购物车</div>
          <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <a :data-open="item.food_name">
        <img class="thumbnail" :src="item.picture" /></a>
        <h5>{{item.food_name}}</h5>
        <p>${{item.money}}</p>
        <div class="button expanded" data-open="order_again" v-on:click="addFood(item.food_name, item.money, 1)">加入购物车</div>
        
      </div>
    </template>
    <div class="button order_button" data-open="addorder">去下单</div>
    <div class="reveal" id="order_again" data-reveal>
      <h2>成功加入购物车</h2>
      <div class="button expanded" data-close aria-label="Close modal">继续挑选食物</div>
      <div class="button expanded" data-open="addorder">完成啦~去下单</div>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <form class="reveal" id="addorder" method="post" action="./" data-reveal>
      <div>
        <label>地址:
          <input type="text" id="address" name="address" required="required" placeholder="Your Address"></input>
        </label>
        <label>联系电话:
          <input type="tel" id="tel" name="tel" required="required" placeholder="Your Phone Number"></input>
        </label>
      </div>
      <div>
        <ul id="order_list">
          <li class="row order_head">
            <span class="column">食物名称</span>
            <span class="column">数量</span>
            <span class="column">单价</span>
            <span class="column">总价</span>
          </li>
          <template v-for="food in shopping_cart">
            <li class="row">
              <span class="column">{{food.food_name}}</span>
              <span class="column">{{food.amount}}</span>
              <span class="column">{{food.price}}</span>
              <span class="column">{{food.amount}}x{{food.price}}={{food.amount*food.price}}</span>
            </li>
          </template>
        </ul>
      </div>
      <div id="submit_button">
        <input class="button expanded" type="submit" v-on:click="isValidate($event)" value="提交订单"></input>
      </div>
      <button class="close-button" data-close aria-label="Close modal" type="button" v-on:click="emptyInput()">
        <span aria-hidden="true">&times;</span>
      </button>
    </form>
  </div>
  <!--<div class="row small-up- 1 medium-up-2">
    <div class="column">

    </div>
    <div class="colunm">
      <div class="bussiness-info" data-hide-for="small">
        <div class="row bussiness-info-banner">
          商家信息
        </div>
        <div class="row bussiness-info-detail">
          <dl>
            <dt>商家名称:</dt>
            <dd>{{business[currentid].title}}</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>-->
</div>
</template>