<script>
  export default {
    name: "Order",
    props: ['searchText'],

    data: function() {
      return {
        orders: [
        {
          order_id: 'order1',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '未处理', //可以选择接单或拒单
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order2',
          order_date: '2016-05-10',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '已接单', //可以选择配送中
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order3',
          order_date: '2016-05-07',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '配送中', //不可以操作
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order4',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '已完成', //
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order5',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '已取消', //不可以操作
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order6',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '已完成',
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order7',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '配送中', //不可以操作
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        },
        {
          order_id: 'order8',
          order_date: '2016-05-09',
          customer_name: 'ccc',
          customer_address: '中山大学慎思园7号520',
          customer_tel: '18819481246',
          order_total: 22,
          order_amount: 11,
          order_status: '未处理', //可以选择接单或拒单
          foods: [
          {food_name: 'aaa',
           food_image: '../images/flower.jpg',
           food_amount: 2,
           food_price: 4},
          {food_name: 'bbb',
           food_image: '../images/flower.jpg',
           food_amount: 3,
           food_price: 2},
          {food_name: 'ccc',
           food_image: '../images/flower.jpg',
           food_amount: 1,
           food_price: 3},
          {food_name: 'ddd',
           food_image: '../images/flower.jpg',
           food_amount: 5,
           food_price: 1},
          ]
        }
        ]
      }
    },
    methods: {
      changeMouseOverStyle: function() {
        $(event.target).addClass("mouseoverstyle");
      },
      resetMouseLeaveStyle: function() {
        $(event.target).removeClass("mouseoverstyle");
      }
    }
  }
</script>

<template>
  <div>
    <div class="row small-up-1 medium-up-2 large-up-4">
      <template v-for="order in orders | filterBy searchText in 'order_date' 'order_status' 'customer_name' 'customer_address' 'customer_tel'">
        <div class="column order-info" v-on:mouseenter="changeMouseOverStyle" v-on:mouseleave="resetMouseLeaveStyle">
          <a v-link="{name: 'detail', params: {orderId:order.order_id}}">
          <div class="row">
            <div class="column">
              订单日期：{{order.order_date}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              收货人姓名：{{order.customer_name}}
            </div>
          </div>
          <div class="row">
            <div class="column">
            收货人地址：{{order.customer_address}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              收货人联系电话：{{order.customer_tel}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              订单食物数量：{{order.order_amount}}件
            </div>
          </div>
          <div class="row">
            <div class="column">
              订单总价：<i class="fi-yen"></i> {{order.order_total}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              订单状态：{{order.order_status}}
            </div>
          </div>
          </a>
          <div class="row">
            <div class="column">
              <template v-if="order.order_status == '未处理'">
                <div class="button receive-reject">接单</div>
                <div class="button receive-reject">拒单</div>
              </template>
              <div v-if="order.order_status == '已接单'" class="button delivery">配送中</div>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>
