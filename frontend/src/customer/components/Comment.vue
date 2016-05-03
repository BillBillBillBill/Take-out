<script>
  export default {
  	name: 'Comment',
  	data: function() {
  	  return {
  	    orderdetail: {
  	  	 bussiness: 'bbb',
         picture: '../images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order2",
         total: 10,
         order_list: [
         {food_name: 'a',
          pic: '../images/pic1.jpg',
          amount: 3,
          price: 5
          },
         {food_name: 'b',
          pic: '../images/pic2.jpg',
          amount: 3,
          price: 5
          },
         {food_name: 'c',
          pic: '../images/pic3.jpg',
          amount: 3,
          price: 5
          },
         {food_name: 'd',
          pic: '../images/pic4.jpg',
          amount: 3,
          price: 5
          },
         {food_name: 'e',
          pic: '../images/pic1.jpg',
          amount: 3,
          price: 5
          }],
         status: '已完成'
        }
  	  }
  	}
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <div class="row">
      <div class="column">
  	    <img :src="orderdetail.picture" />
  	  </div>
  	  <div class="column">
  	    <p>商家：{{orderdetail.bussiness}}</p>
        <p>地址：{{orderdetail.address}}</p>
        <p>电话：{{orderdetail.tel}}</p>
        <p>状态：{{orderdetail.status}}</p>
  	  </div>
  	  <div class="column">
  	    <template v-for="li in orderdetail.order_list">
          <a class="row" :data-open="li.food_name">
            <div class="column">{{li.food_name}}</div>
            <div class="column">{{li.amount}}份</div>
            <div class="column">￥{{li.price}}/份</div>
          </a>

          <div class="reveal" :id="li.food_name" data-reveal>
      	    <img :src="li.pic">
      	    <p>名称：{{li.food_name}}</p>
      	    <p>价格：￥{{li.price}}/份</p>
      	    <form method="post" action="./">
    	      <label>评分：
    	  	    <input type="number" id="ordergrade" name="ordergrade" required="required"></input>
    	      </label>
    	      <textarea id="comment_text" placeholder="Enter your comments on this order"></textarea>
    	      <input class="button expand" type="submit" value="提交评价"></input>
    	    </form>
      	    <button class="close-button" data-close aria-label="Close modal" type="button">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        </template>
  	  </div>
    </div>
    <div class="row">
    	<form method="post" action="./">
    	  <label>评分：
    	  	<input type="number" id="ordergrade" name="ordergrade" required="required"></input>
    	  </label>
    	  <textarea id="comment_text" placeholder="Enter your comments on this order"></textarea>
    	  <input class="button" type="submit" value="提交评价"></input>
    	</form>
    </div>
  </div>
</template>