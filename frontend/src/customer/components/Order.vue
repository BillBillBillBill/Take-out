<script>
  export default {
    name: "Order",

    data: function() {
      return {
        orders: [
        {bussiness: 'aaa',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order1",
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
         {bussiness: 'bbb',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order2",
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
         status: '已完成'
         },
         {bussiness: 'ccc',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order3",
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
         {bussiness: 'ddd',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order4",
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
         status: '已接单'
         },
         {bussiness: 'eee',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order5",
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
         status: '已取消'
         },
         {bussiness: 'fff',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order6",
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
    <div class="row small-up-1 medium-up-2 large-up-4">
      <template v-for="item in orders">
        <div class="column customer-item">
          <a :data-open="item.orderid">
            <div class="row">
              <div class="column">
                <img :src="item.picture" />
              </div>
              <div class="column">
                <div class="row">商家：{{item.bussiness}}</div>
                <div class="row">地址：{{item.address}}</div>
                <div class="row">电话：{{item.tel}}</div>
                <div class="row">状态：{{item.status}}</div>
                <a v-if="item.status == '已完成'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment">评价</a>
              </div>
            </div>
          </a>

          <div class="reveal" :id="item.orderid" data-reveal>
            <img :src="item.picture" />
            <p>商家：{{item.bussiness}}</p>
            <p>地址：{{item.address}}</p>
            <p>电话：{{item.tel}}</p>
            <p>状态：{{item.status}}</p>
            <a v-if="item.status == '已完成'" v-link="{name: 'comment', params: {orderId: item.orderid}}" class="button comment">评价</a>
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
    </div>
  </div>
</template>
