<script>
  export default {
    name: "Order",
    props: ['searchText'],

    data: function() {
      return {
        bubble: true,
        orders: [
        {bussiness: 'aaa',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order1",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '未处理'
         },
         {bussiness: 'bbb',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order2",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'ccc',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order3",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'ddd',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order4",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已接单'
         },
         {bussiness: 'eee',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order5",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已取消'
         },
         {bussiness: 'fff',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order6",
         date: '2016-03-24',
         total: 10,
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '未处理'
        },
        {bussiness: 'ggg',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order7",
         date: '2016-03-24',
         total: 10,
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'hhh',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order8",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'iii',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order9",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '未处理'
         },
         {bussiness: 'jjj',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order10",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已取消'
         },
         {bussiness: 'kkk',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order11",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'lll',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order12",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '未处理'
        },
        {bussiness: 'nnn',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order13",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'mmm',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order14",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'ooo',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order15",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          },
         {food_name: 'a',
          amount: 3,
          price: 5
          }],
         status: '已完成'
        }]
      }
    },
    methods: {
      cancelOrder: function(orderid) {
        alert("成功取消订单");
      },
      completeOrder: function(orderid) {
        alert("成功确认收货");
      }
    }
  }
</script>

<template>
  <div>
   <!-- <div class="row small-up-1 medium-up-2 large-up-4">
      <template v-for="item in orders">
        <div class="column orderlist">
          <a href="#">
              <div class="column">
                <img :src="item.picture" />
              </div>
              <div class="column">
                <div class="row">{{item.address}}</div>
                <div class="row">{{item.tel}}</div>
                <template v-for="li in item.order_list">
                  <div class="row">
                    <div class="column">{{li.food_name}}</div>
                    <div class="column">{{li.amount}}份</div>
                    <div class="column">￥{{li.price}}/份</div>
                  </div>
                </template>
              </div>
          </a>
        </div>
      </template>
    </div>-->
    <!--<div class="row small-up-1 medium-up-2 large-up-4">
      <template v-for="item in orders">
        <div class="column">
          <a :data-open="item.orderid">
            <div class="row customer-item" small-2>
              <div class="column">
                <img :src="item.picture" />
              </div>
              <div class="column">
                <div class="row">商家：{{item.bussiness}}</div>
                <div class="row">地址：{{item.address}}</div>
                <div class="row">电话：{{item.tel}}</div>
                <div class="row">状态：{{item.status}}</div>
                <a v-if="item.status == '已完成'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment">评价</a>
                <a v-if="item.status == '已取消' || item.status == '已完成'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment">投诉</a>
                <a v-if="item.status == '未处理'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment">取消订单</a>
              </div>
            </div>
          </a>

          <div class="reveal" :id="item.orderid" data-reveal>
            <img :src="item.picture" />
            <p>商家：{{item.bussiness}}</p>
            <p>地址：{{item.address}}</p>
            <p>电话：{{item.tel}}</p>
            <p>状态：{{item.status}}</p>
            <a v-if="item.status == '已完成'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment" data-close>评价</a>
            <p>订单详情：</p>
            <template v-for="li in item.order_list">
              <div class="row">
                <div class="column">{{li.food_name}}</div>
                <div class="column">{{li.amount}}份</div>
                <div class="column">￥{{li.price}}/份</div>
              </div>
            </template>
            <div class="row">
              <div class="column small-4 order_head">合计:</div>
              <div class="column small-4 small-offset-4">￥{{item.total}}</div>
            </div>
            <button class="close-button" data-close aria-label="Close modal" type="button">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

        </div>
      </template>
    </div>-->
    <div class="row small-up-1 medium-up-2 large-up-3">
      <template v-for="item in orders | filterBy searchText">
        <div class="column">
          <a v-link="{name: 'order_detail', params: {orderId: item.orderid}}">
            <div class="row order_row">
              <div class="column medium-5 align-middle">
                <h4 class="order_head">{{item.bussiness}}</h4>
                <img :src="item.picture">
              </div>
              <div class="column align-bottom">
                <div class="row">{{item.date}}</div>
                <div class="row">收货人地址：{{item.address}}</div>
                <div class="row">收货人电话：{{item.tel}}</div>
                <div class="row">
                  订单状态：{{item.status}}
                </div>
                <div class="row">
                  <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
                  <div v-if="item.status == '已完成'" class="button comment" data-open="comment">评价</div>
                  <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
                  <div v-if="item.status == '已取消' || item.status == '已完成'" class="button complain" data-open="complain">投诉</div>
                  <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
                  <div v-if="item.status == '未处理'" class="button cancel" data-open="cancel">取消订单</div>
                  <div v-if="item.status == '配送中'" class="button complete" data-open="complete">完成订单</div>
                </div>
                <div class="reveal" id="comment" data-reveal>
                  <form method="post" action="./">
                    <div>
                      您的评分是：{{grade}} 分
                      <template v-for="n in 5">
                        <i class="fi-star gray grade-star" v-bind:class="n+''" :id="'star-'+n" v-on:click="getGrade(n)" v-on:mouseover="hoverGrade(n)"></i>
                      </template>
                    </div>
                    <textarea id="comment_text" name="comment" placeholder="Enter your comments on this order"></textarea>
                    <input class="button expanded" id="comment_button" type="submit" value="提交评价"></input>
                  </form>
                  <button class="close-button" data-close aria-label="Close modal" type="button">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="reveal" id="complain" data-reveal>
                  <form method="post" action="./">
                    <label>投诉原因：
                      <textarea id="complain_text" name="complain" placeholder="Enter your complain reasons here."></textarea>
                    </label>
                    <input class="button expanded" id="complain_button" type="submit" value="提交投诉"></input>
                  </form>
                  <button class="close-button" data-close aria-label="Close modal" type="button">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="reveal" id="cancel" data-reveal>
                  <div class="button expanded" id="cancel_button" v-on:click="cancelOrder(currentOrderId)">确认取消</div>
                  <div class="button expanded" data-close>不取消了</div>
                </div>
                <div class="reveal" id="complete" data-reveal>
                  <div class="button expanded" id="complete_button" v-on:click="completeOrder(currentOrderId)">确认收货</div>
                  <div class="button expanded" data-close>手滑点错了</div>
                </div>
              </div>
            </div>
          </a>
        </div>
      </template>
    </div>
  </div>
</template>
