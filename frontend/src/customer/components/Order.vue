<script>
  export default {
    name: "Order",
    props: ['searchText'],

    data: function() {
      return {
        order_list: [],
        grade: 0
      }
    },
    methods: {
      submit_complete_message: function(order_id) {
        var that = this;
        var info = {
          action: "finish",
        }
        $.ajax({
          url: "../api/order/" + order_id,
          type: "PUT",
          contentType: "application/json;charset=utf-8",
          processData: false,
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(info),
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            for (var i = 0; i < that.order_list.length; i++) {
              if (that.order_list[i].order_id == order_id) {
                that.order_list[i].order_status = "已完成";
                break;
              }
            }
          }
        });
      },
      submit_comment_message: function(event, order_id, store_id) {
        var that = this;
        var delivery_time = $("#delivery_time" + order_id).val();
        var info = {
          action: "finish",
          order_review: {
            delivery_time: delivery_time
          }
        };
        if (that.grade > 0) info.order_review.star = that.grade;
        if ($("#comment_text" + order_id).val() != "") info.order_review.content = $("#comment_text" + order_id).val();
        $.ajax({
          url: "../api/order/" + order_id,
          type: "PUT",
          contentType: "application/json;charset=utf-8",
          processData: false,
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(info),
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            for (var i = 0; i < that.order_list.length; i++) {
              if (that.order_list[i].order_id == order_id) {
                that.order_list[i].order_status = "已完成";
                break;
              }
            }
            that.grade = 0;
            $("#delivery_time" + order_id).val("0");
            $("#comment_text" + order_id).val("");
          }
        });
        event.preventDefault();
        return false;
      },
      submit_complaint_message: function(event, order_id, store_id) {
        var that = this;
        var content = $("#complain_text" + order_id).val();
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
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            $("#complain_text" + order_id).val("");
          }
        });
        event.preventDefault();
        return false;
      },
      hoverGrade: function(id, index) {
        this.changeStarsGrade(id, index);
      },
      getGrade: function(id, index) {
        this.changeStarsGrade(id, index);
      },
      resetStars: function(id) {
        var stars = $("#comment" + id + " .grade-star");
        for (var i = 0; i < stars.length; i++) {
          $(stars[i]).removeClass("gold").addClass("gray");
        }
      },
      changeStarsGrade: function(id, index) {
        var stars = $("#comment" + id + " .grade-star");
        this.resetStars(id);
        for (var i = 0; i <= index; i++) {
          $(stars[i]).removeClass("gray").addClass("gold");
        }
        this.grade = index + 1;
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/order",
          async: false,
          type: "GET",
          headers: {'Authorization-Token': localStorage.customer_token},
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            if (that.order_list.length == 0) {
              var list = data.data.order_list;
              console.log("order_list: " + list);
              for (var i = 0; i < list.length; i++) {
                var info = {
                  order_status: list[i].status,
                  //order_date: list[i].make_order_time,
                  //order_note: list[i].note,
                  //order_total_price: list[i].total_price,
                  //order_food_list: list[i].food_list,
                  order_id: list[i].id,
                  order_store_id: list[i].store,
                  order_phone: list[i].delivery_information.phone,
                  order_receiver: list[i].delivery_information.receiver,
                  order_address: list[i].delivery_information.address
                };
                var newDate = new Date();
                newDate.setTime(parseInt(list[i].make_order_time)*1000 + 3600000*8);
                info.order_date = newDate.toLocaleString();
                $.ajax({
                  url: "../api/store/" + info.order_store_id,
                  async: false,
                  type: "GET",
                  dataType: "json",
                  error: function(xhr, status) {
                    alert("Error: " + status);
                  },
                  success: function(data) {
                    var list = data.data.store;
                    info.order_store_name = list.name;
                    if (list.images[0]) info.order_store_image = "../api/" + list.images[0].path;
                  }
                });
                that.order_list.push(info);
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
    },
    watch: {
      'order_list': function() {
        var order_list = this.order_list;
        for (var i in order_list) {
          new Foundation.Reveal($("#comment" + order_list[i].order_id), {});
          new Foundation.Reveal($("#complain" + order_list[i].order_id), {});
          new Foundation.Reveal($("#complete" + order_list[i].order_id), {});
        }
      }
    }
  }
</script>

<template>
  <div>
    <div class="row small-up-1 medium-up-2 large-up-3">
      <template v-for="item in order_list | filterBy searchText">
        <div class="column">
          <a v-link="{name: 'order_detail', params: {orderId: item.order_id}}">
            <div class="row order_row">
              <div class="column medium-5 align-middle">
                <h4 class="order_head">{{item.order_store_name}}</h4>
                <img :src="item.order_store_image">
              </div>
              <div class="column align-bottom">
                <div class="row">{{item.order_date}}</div>
                <div class="row">收货人地址：{{item.order_address}}</div>
                <div class="row">收货人电话：{{item.order_phone}}</div>
                <div class="row">
                  订单状态：{{item.order_status}}
                </div>
              </div>
            </div>
          </a>
          <div class="row order_row">
            <div class="column">
              <div v-if="item.order_status == '配送中'" class="button complete" :data-open="'complete' + item.order_id">完成订单</div>
              <div class="button complain" :data-open="'complain' + item.order_id">投诉</div>
            </div>
          </div>

          <!--弹出评价订单窗口-->
          <div class="reveal" :id="'comment' + item.order_id" data-reveal>
            <form method="post" action="./">
              <div>
                您的评分是：{{grade}} 分
                <template v-for="n in 5">
                  <i class="fi-star gray grade-star" v-bind:class="n+''" v-on:click="getGrade(item.order_id, n)" v-on:mouseover="hoverGrade(item.order_id, n)"></i>
                </template>
              </div>
              <label>配送时间/分钟
                <input :id="'delivery_time' + item.order_id" type="number" name="delivery_time" required="required"></input>
              </label>
              <textarea :id="'comment_text' + item.order_id" name="content" placeholder="Enter your comments on this order"></textarea>
              <input class="button expanded" class="comment_button" type="submit" value="提交评价" v-on:click="submit_comment_message($event, item.order_id, item.order_store_id)" data-close></input>
            </form>
            <button class="close-button" data-close aria-label="Close modal" type="button">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <!--弹出投诉订单窗口-->
          <div class="reveal" :id="'complain' + item.order_id" data-reveal>
            <form method="post" action="./">
              <label>投诉原因：
                <textarea :id="'complain_text' + item.order_id" name="complain" placeholder="Enter your complain reasons here."></textarea>
              </label>
              <input class="button expanded" class="complain_button" type="submit" value="提交投诉" data-close v-on:click="submit_complaint_message($event, item.order_id, item.order_store_id)"></input>
            </form>
            <button class="close-button" data-close aria-label="Close modal" type="button">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <!--弹出完成订单窗口-->
          <div class="reveal" :id="'complete' + item.order_id" data-reveal>
            <div class="button" class="complete_button" data-close v-on:click="submit_complete_message(item.order_id)">确认收货</div>
            <div class="button" class="comment_button" :data-open="'comment' + item.order_id">评价</div>
            <div class="button expanded" data-close>手滑点错了</div>
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

  .order_row {
    padding: 10px;
  }

  .comment {
    margin-right: 5px;
  }

  .grade-star {
    cursor: hand;
    cursor: pointer;
  }

</style>
