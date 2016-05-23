<script>
  export default {
  	name: 'Detail',
  	data: function() {
  	  return {
  	  	currentOrderId: this.$route.params.orderId,
  	  	orders: [
  	  	  {orderid: 'order1',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '未处理',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order2',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '已接单',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order3',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '配送中',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order4',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '已完成',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order5',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '已取消',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order6',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '未处理',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order7',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '配送中',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]},
  	  	  {orderid: 'order8',
  	  	  address: '中山大学慎思园7号',
  	  	  tel: '18819481246',
  	  	  total: 20,
  	  	  date: '2016-03-24',
  	  	  status: '已完成',
  	  	  order_list: [
  	  	  {food_name: 'aa',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'bb',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'cc',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'dd',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ee',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'ff',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'gg',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4},
  	  	  {food_name: 'hh',
  	  	  amount: 2,
  	  	  remainaomunt: 56,
  	  	  picture: '../images/flower.jpg',
  	  	  price: 4}
  	  	  ]}
  	  	]
  	  }
  	},
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 bussiness-order-detail">
  	<template v-for="item in orders">
  	  <template v-if="item.orderid == currentOrderId">
  	  	<div class="column" data-sticky-container>
  	  	  <div class="sticky" data-sticky data-margin-top="4.5">
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <div class="callout small">
  	  	  	  	  <div>下单时间：{{item.date}}</div>
  	  	  	    </div>
  	  	  	  </div>
  	  	    </div>
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <div class="callout small">
  	  	  	  	  <div>收货地址：{{item.address}}</div>
  	  	  	    </div>
  	  	  	  </div>
  	  	    </div>
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <div class="callout small">
  	  	  	  	  <div>收货人电话：{{item.tel}}</div>
  	  	  	    </div>
  	  	  	  </div>
  	  	    </div>
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <div class="callout small">
  	  	  	  	  <div>总计：<i class="fi-yen"></i> {{item.total}}</div>
  	  	  	    </div>
  	  	  	  </div>
  	  	    </div>
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <div class="callout small">
  	  	  	  	  <div>状态：{{item.status}}</div>
  	  	  	    </div>
  	  	  	  </div>
  	  	    </div>
  	  	    <div class="row">
  	  	  	  <div class="column">
  	  	  	    <template v-if="item.status == '未处理'">
  	  	  	  	  <div class="button receive-reject">接单</div>
                  <div class="button receive-reject">拒单</div>
  	  	  	    </template>
  	  	  	    <div v-if="item.status == '已接单'" class="button delivery">配送中</div>
  	  	  	  </div>
  	  	    </div>
  	  	  </div>
  	  	</div>
  	  	<div class="column">
  	  	  <template v-for="order in item.order_list">
  	  	  	<div class="callout small">
  	  	  	  <div class="row">
  	  	  	  	<div class="column align-middle"><img :src="order.picture" /></div>
  	  	  	  	<div class="column align-middle">{{order.food_name}}</div>
  	  	  	  	<div class="column align-middle">{{order.amount}}份</div>
  	  	  	  	<div class="column align-middle"><i class="fi-yen"></i>{{order.price}}/份</div>
  	  	  	  </div>
  	  	  	</div>
  	  	  </template>
  	  	</div>
  	  </template>
  	</template>
  </div>
</template>

<style lang="sass">
  // Import
  @import "../variables.scss";

  // Style
  * {
    box-sizing:border-box;
    -moz-box-sizing:border-box; /* Firefox */
    -webkit-box-sizing:border-box; /* Safari */
  }

  .bussiness-order-detail {
    margin-top: 20px;
  }
</style>