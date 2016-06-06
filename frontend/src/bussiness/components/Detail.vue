<script>
  export default {
  	name: 'Detail',
  	data: function() {
  	  return {
  	  	currentOrderId: this.$route.params.orderId,
        current_order_info: {},
        order_food_info: []
  	  }
  	},
    methods: {
      handle_order: function(action, order_id) {
        var that = this;
        var info = {
          action: action,
        }
        $.ajax({
          url: "../api/order/" + order_id,
          type: "PUT",
          contentType: "application/json;charset=utf-8",
          processData: false,
          headers: {'Authorization-Token': localStorage.bussiness_token},
          data: JSON.stringify(info),
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            if (action == "accept") that.current_order_info.status = "已接单";
            else if (action == "close") that.current_order_info.status = "已关闭";
            else that.current_order_info.status = "配送中";
          }
        });
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/order/" + that.currentOrderId,
          async: false,
          type: "GET",
          headers: {'Authorization-Token': localStorage.bussiness_token},
          dataType: "json",
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            var order_info = data.data.order;
            var info = {
              status: order_info.status,
              //make_order_time: order_info.make_order_time,
              order_id: order_info.id,
              store_id: order_info.store,
              order_price: order_info.total_price,
             // order_food_list: order_info.food_list,
              order_note: order_info.note,
              order_delivery_information_address: order_info.delivery_information.address,
              order_delivery_information_phone: order_info.delivery_information.phone
            };
            var newDate = new Date();
            newDate.setTime(parseInt(order_info.make_order_time)*1000 + 3600000*8);
            info.order_date = newDate.toLocaleString();
            that.current_order_info = info;

            var food = order_info.food_list;
            if (that.order_food_info.length == 0) {
              for (var i = 0; i < food.length; i++) {
                var food_data = {
                  count: food[i].count,
                  name: food[i].food.name,
                  //star: food[i].food.average_star,
                  //id: food[i].id,
                  stock: food[i].food.stock,
                  price: food[i].food.price,
                  food_review_list: food[i].food.food_review_list
                };
                if (food[i].food.images[0]) food_data.image = "../api/" + food[i].food.images[0].path;
                that.order_food_info.push(food_data);
              }
            }
          }
        });
      }
      reloadPage();
      $(window).load(function() {
        reloadPage();
      });
      $(window).unload(function() {
        reloadPage();
      });
    }
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 bussiness-order-detail">
  	<div class="column" data-sticky-container>
  	  <div class="sticky" data-sticky data-margin-top="4.5">
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<div class="callout small">
  	  	  	  <div>下单时间：{{current_order_info.order_date}}</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<div class="callout small">
  	  	  	  <div>收货地址：{{current_order_info.order_delivery_information_address}}</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<div class="callout small">
  	  	  	  <div>收货人电话：{{current_order_info.order_delivery_information_phone}}</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<div class="callout small">
  	  	  	  <div>总计：<i class="fi-yen"></i> {{current_order_info.order_price}}</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<div class="callout small">
  	  	  	  <div>状态：{{current_order_info.status}}</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  	<div class="row">
  	  	  <div class="column">
  	  	  	<template v-if="current_order_info.status == '未处理'">
  	  	  	  <div class="button receive-reject" v-on:click="handle_order('accept', current_order_info.order_id)">接单</div>
              <div class="button receive-reject" v-on:click="handle_order('close', current_order_info.order_id)">拒单</div>
  	  	  	</template>
  	  	  	<div v-if="current_order_info.status == '已接单'" class="button delivery" v-on:click="handle_order('transport', current_order_info.order_id)">配送</div>
  	  	  </div>
  	  	</div>
  	  </div>
  	</div>
  	<div class="column">
  	  <template v-for="food in order_food_info">
  	  	<div class="callout small">
  	  	  <div class="row">
  	  	    <div class="column align-middle"><img :src="food.image" /></div>
  	  	  	<div class="column align-middle">{{food.name}}</div>
  	  	  	<div class="column align-middle">{{food.count}}份</div>
  	  	  	<!--<div class="column align-middle"><i class="fi-yen"></i>{{food.price}}/份</div>-->
            <div class="column align-middle">剩余{{food.stock}}份</div>
  	  	  </div>
  	  	</div>
  	  </template>
  	</div>
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