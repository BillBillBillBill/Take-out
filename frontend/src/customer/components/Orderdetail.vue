<script>
  export default {
  	name: "Orderdetail",
  	data: function() {
  		return {
  			grade: 0,
        foodgrade: 0,
  			isShow: false,
        currentOrderId: this.$route.params.orderId,
        current_order_info: {},
        store_info: {},
        order_food_info: [],
        food_review_list: []
      }
  	},
  	methods: {
  		completeOrder: function(order_id) {
  			var that = this;
        var info = {
          action: "finish",
        }
        if (that.food_review_list.length > 0) info.food_review_list = that.food_review_list;
        $.ajax({
          url: "../api/order/" + order_id,
          type: "PUT",
          contentType: "application/json;charset=utf-8",
          processData: false,
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(info),
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            that.current_order_info.status = '已完成';
            that.grade = 0;
            that.foodgrade = 0;
            that.food_review_list = [];
          }
        });
  		},
      submit_order_comment: function(event, order_id, store_id) {
        var that = this;
        var delivery_time = $("#delivery_time").val();
        var info = {
          action: "finish",
          order_review: {
            delivery_time: delivery_time
          }
        };
        if (that.grade > 0) info.order_review.star = that.grade;
        if ($("#comment_text").val() != "") info.order_review.content = $("#comment_text").val();
        if (that.food_review_list.length > 0) info.food_review_list = that.food_review_list;
        $.ajax({
          url: "../api/order/" + order_id,
          type: "PUT",
          contentType: "application/json;charset=utf-8",
          processData: false,
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(info),
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            that.current_order_info.status = '已完成';
            that.grade = 0;
            that.foodgrade = 0;
            that.food_review_list = [];
          }
        });
        event.preventDefault();
        return false;
      },
      submit_food_comment: function(event, food_id) {
        this.isShow = false;
        var that = this;
        var info = {
          food_id: food_id
        };
        if (that.foodgrade > 0) {
          info.star = that.foodgrade;
          that.foodgrade = 0;
        }
        if ($("#food_comment_text" + food_id).val() != "") {
          info.content = $("#food_comment_text" + food_id).val();
          $("#food_comment_text" + food_id).val("");
        }
        that.food_review_list.push(info);
        event.preventDefault();
        return false;
      },
      submit_complaint_message: function(event, store_id) {
        var that = this;
        var content = $("#complain_text").val();
        var info = {
          content: content,
          store_id: store_id
        };
        $.ajax({
          url: "../api/complaint",
          async: false,
          type: "POST",
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(info),
          contentType: "application/json;charset=utf-8",
          processData: false,
          dataType: "json",
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            $("#complain_text").val("");
          }
        });
        event.preventDefault();
        return false;
      },
  		openComment: function() {
  			this.isShow = true;
  		},
  		resetIsShow: function() {
  			this.isShow = false;
  		},
  		hoverGrade: function(index) {
        this.changeStarsGrade(index);
      },
      getGrade: function(index) {
        this.changeStarsGrade(index);
      },
      resetStars: function() {
        var stars = $("#comment .grade-star");
        for (var i = 0; i < stars.length; i++) {
          $(stars[i]).removeClass("gold").addClass("gray");
        }
      },
      changeStarsGrade: function(index) {
        var stars = $("#comment .grade-star");
        this.resetStars();
        for (var i = 0; i <= index; i++) {
          $(stars[i]).removeClass("gray").addClass("gold");
        }
        this.grade = index + 1;
      },
      hoverFoodGrade: function(id, index) {
        this.changeFoodStarsGrade(id, index);
      },
      getFoodGrade: function(id, index) {
        this.changeFoodStarsGrade(id, index);
      },
      resetFoodStars: function(id) {
        var stars = $("#food" + id + " .grade-star");
        for (var i = 0; i < stars.length; i++) {
          $(stars[i]).removeClass("gold").addClass("gray");
        }
      },
      changeFoodStarsGrade: function(id, index) {
        var stars = $("#food" + id + " .grade-star");
        this.resetFoodStars(id);
        for (var i = 0; i <= index; i++) {
          $(stars[i]).removeClass("gray").addClass("gold");
        }
        this.foodgrade = index + 1;
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
          headers: {'Authorization-Token': localStorage.customer_token},
          dataType: "json",
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            var order_info = data.data.order;
            var info = {
              status: order_info.status,
              make_order_time: order_info.make_order_time,
              order_id: order_info.id,
              store_id: order_info.store,
              order_price: order_info.total_price,
             // order_food_list: order_info.food_list,
              order_note: order_info.note,
              order_delivery_information_address: order_info.delivery_information.address,
              order_delivery_information_phone: order_info.delivery_information.phone
            };
            that.current_order_info = info;
            var food = order_info.food_list;
            if (that.order_food_info.length == 0) {
              for (var i = 0; i < food.length; i++) {
                var food_data = {
                  count: food[i].count,
                  name: food[i].food.name,
                  star: food[i].food.average_star,
                  id: food[i].food.id,
                  stock: food[i].food.stock,
                  price: food[i].food.price,
                  description: food[i].food.description,
                  food_review_list: food[i].food.food_review_list
                };
                if (food[i].food.images[0]) food_data.image = "../api/" + food[i].food.images[0].path;
                for (var i = 0; i < food_data.food_review_list.length; i++) {
                  var newDate = new Date();
                  newDate.setTime(parseInt(food_data.food_review_list[i].created_time)*1000 + 3600000*8);
                  var time = newDate.toLocaleString();
                  food_data.food_review_list[i].created_time = time;
                }
                that.order_food_info.push(food_data);
              }
            }
            $.ajax({
              url: "../api/store/" + that.current_order_info.store_id,
              async: false,
              type: "GET",
              error: function(xhr, status) {
                alert(JSON.parse(xhr.responseText).message);
              },
              success: function(data) {
                var list = data.data.store;
                var info = {
                  store_id: list.id,
                  store_name: list.name,
                  store_phone: list.phone,
                  store_address: list.address,
                  total_orders_number: list.total_orders_num,
                  average_star: list.average_star,
                  complaint_rate: Math.round(parseFloat(list.complaint_rate)*100)/100,
                  order_review_list: list.order_review_list
                };
                if (list.images[0]) info.bussiness_image = "../api/" + list.images[0].path;
                that.store_info = info;
              }
            });
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
    },
    watch: {
      'order_food_info': function() {
        var order_food_info = this.order_food_info;
        for (var i in order_food_info) {
          new Foundation.Reveal($("#food" + order_food_info[i].id), {});
        }
      }
    }
  }
</script>

<template>
  <div class="row orderdetail small-up-1 medium-up-2">
    <div class="column">
      <div class="row">
        <div class="column">
          <img class="thumbnail" :src="store_info.bussiness_image" />
        </div>
        <div class="column align-middle ">
          <h4>{{store_info.store_name}}</h4>
          <div>
            <i v-for="n in store_info.average_star" class="fi-star gold"></i><i v-for="n in (5-store_info.average_star)" class="fi-star gray"></i>
          </div>
          <div>投诉率：{{store_info.complaint_rate * 100}}%</div>
          <div>月销售量{{store_info.total_orders_number}}单</div>
          <div><i class="fi-telephone"></i>{{store_info.store_phone}}</div>
          <div><i class="fi-marker"></i> {{store_info.store_address}}</div>
        </div>
      </div>
      <div class="row">
      	<div class="column medium-6">
      	  <div class="callout small">
      	    <div>收货地址：{{current_order_info.order_delivery_information_address}}</div>
      	  </div>
      	</div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>收货人电话：{{current_order_info.order_delivery_information_phone}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>总计：<i class="fi-yen"></i>{{current_order_info.order_price}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>状态：{{current_order_info.status}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <div v-if="current_order_info.status == '配送中'" class="button complete" data-open="complete">完成订单</div>
          <div class="button complain" data-open="complain">投诉</div>
        </div>
      </div>
  	</div>
  	<div class="column">
  	<template v-for="food in order_food_info" >
  	  <div class="callout small">
  	  <a :data-open="'food' + food.id">
  	    <div class="row">
          <div class="column align-middle"><img :src="food.image" /></div>
  	      <div class="column align-middle ">{{food.name}}</div>
  	      <div class="column align-middle ">{{food.count}}份</div>
  	      <div class="column align-middle "><i class="fi-yen"></i> {{food.price}}/份</div>
        </div>
      </a>
      </div>

      <!--弹出食物详情窗口-->
      <div class="reveal" :id="'food' + food.id" data-reveal>
        <div class="row">
          <div class="column">
            <img :src="food.image" class="reveal_img" />
          </div>
          <div class="column">
            <div class="row">{{food.name}}</div>
            <div class="row">
              <i v-for="n in food.star" class="fi-star gold"></i><i v-for="n in (5-food.star)" class="fi-star gray"></i>
            </div>
            <div class="row price"><i class="fi-yen"></i> {{food.price}}</div>
            <div class="row count_detail">剩余<span class="item_count">{{food.stock}}</span>份</div>
            <div class="row">
              <strong>描述：</strong>{{food.description}}
            </div>
            <div class="button margin-button" v-if="current_order_info.status == '配送中'" v-on:click="openComment">评价该食物</div>
          </div>
        </div>

        <!--弹出评论食物窗口-->
        <form method="post" action="./" v-if="isShow" class="margin-button">
          <div>
            您的评分是：{{foodgrade}} 分
            <template v-for="n in 5">
              <i class="fi-star gray grade-star" v-bind:class="n+''" v-on:click="getFoodGrade(food.id, n)" v-on:mouseover="hoverFoodGrade(food.id, n)"></i>
            </template>
          </div>
    	    <textarea :id="'food_comment_text' + food.id" name="content" placeholder="Enter your comments on this order"></textarea>
    	    <input class="button expanded" class="comment_button" type="submit" value="提交评价" v-on:click="submit_food_comment($event, food.id)" data-close></input>
        </form>
        <button class="close-button" data-close aria-label="Close modal" type="button" v-on:click="resetIsShow">
          <span aria-hidden="true">&times;</span>
        </button>

        <!--显示食物评价列表-->
        <ul class="show_comments accordion margin-button" data-accordion data-multi-expand="true">
          <li v-for="comment in food.food_review_list" v-bind:class="[$index==0 ? 'is-active':'']" class="accordion-item" data-accordion-item>
            <a class="accordion-title">
              <span>{{comment.customer}}</span>
              <i v-for="n in comment.star" class="fi-star gold"></i><i v-for="n in (5-comment.star)" class="fi-star gray"></i>
              <span>{{comment.created_time}}</span>
            </a>
            <div class="description accordion-content" data-tab-content>{{comment.content}}</div>
          </li>
        </ul>
      </div>
      </template>
    </div>

    <!--弹出评论窗口-->
    <div class="reveal" id="comment" data-reveal>
      <form method="post" action="./">
        <div>
          您的评分是：{{grade}} 分
          <template v-for="n in 5">
            <i class="fi-star gray grade-star" v-bind:class="n+''" :id="'star-'+n" v-on:click="getGrade(n)" v-on:mouseover="hoverGrade(n)"></i>
          </template>
        </div>
        <label>配送时间/分钟
          <input id="delivery_time" type="number" name="delivery_time" required="required"></input>分钟
        </label>
        <textarea id="comment_text" name="comment" placeholder="Enter your comments on this order"></textarea>
        <input class="button expanded" id="comment_button" type="submit" value="提交评价" v-on:click="submit_order_comment($event, current_order_info.order_id, current_order_info.store_id)"></input>
      </form>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <!--弹出投诉窗口-->
    <div class="reveal" id="complain" data-reveal>
      <form method="post" action="./">
      	<label>投诉原因：
      	  <textarea id="complain_text" name="complain" placeholder="Enter your complain reasons here."></textarea>
      	</label>
      	<input class="button expanded" id="complain_button" type="submit" value="提交投诉" v-on:click="submit_complaint_message($event, current_order_info.store_id)" data-close></input>
      </form>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <!--弹出完成订单窗口，其中可以选择确认收货和评价订单-->
    <div class="reveal" id="complete" data-reveal>
      <div class="button" id="complete_button" v-on:click="completeOrder(current_order_info.order_id)" data-close>确认收货</div>
      <div class="button" id="comment_button" :data-open="comment">评价</div>
      <div class="button expanded" data-close>手滑点错了</div>
    </div>
<!--  </template>-->
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

  .orderdetail {
    margin-top: 20px;
  }

  .complete {
    margin-right: 10px;
  }

  .margin-button {
    margin-top: 10px;
  }
</style>