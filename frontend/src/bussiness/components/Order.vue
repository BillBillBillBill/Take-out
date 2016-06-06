<script>
  export default {
    name: "Order",
    props: ['searchText'],

    data: function() {
      return {
        order_list: []
      }
    },
    methods: {
      changeMouseOverStyle: function() {
        $(event.target).addClass("mouseoverstyle");
      },
      resetMouseLeaveStyle: function() {
        $(event.target).removeClass("mouseoverstyle");
      },
      handle_order: function(action, order_id) {
        var that = this;
        var info = {
          action: action,
        };
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
            for (var i = 0; i < that.order_list.length; i++) {
              if (that.order_list[i].order_id == order_id) {
                if (action == "accept") that.order_list[i].order_status = "已接单";
                else if (action == "close") that.order_list[i].order_status = "已关闭";
                else that.order_list[i].order_status = "配送中";
                break;
              }
            }
          }
        });
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
          headers: {'Authorization-Token': localStorage.bussiness_token},
          dataType: "json",
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            if (that.order_list.length == 0) {
              var list = data.data.order_list;
              console.log(list);
              for (var i = 0; i < list.length; i++) {
                var info = {
                  order_status: list[i].status,
                  //order_date: list[i].make_order_time,
                  //order_note: list[i].note,
                  //order_total_price: list[i].total_price,
                  //order_food_list: list[i].food_list,
                  order_id: list[i].id,
                  order_store_id: list[i].store,
                  order_price: list[i].total_price,
                  order_phone: list[i].delivery_information.phone,
                  order_receiver: list[i].delivery_information.receiver,
                  order_address: list[i].delivery_information.address
                };
                var newDate = new Date();
                newDate.setTime(parseInt(list[i].make_order_time)*1000 + 3600000*8);
                info.order_date = newDate.toLocaleString();
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
    }
  }
</script>

<template>
  <div>
    <div class="row small-up-1 medium-up-2 large-up-4">
      <template v-for="order in order_list | filterBy searchText in 'order_date' 'order_status' 'order_receiver' 'order_address' 'order_phone'">
        <div class="column order-info" v-on:mouseenter="changeMouseOverStyle" v-on:mouseleave="resetMouseLeaveStyle">
          <a v-link="{name: 'detail', params: {orderId:order.order_id}}">
          <div class="row">
            <div class="column">
              订单日期：{{order.order_date}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              收货人姓名：{{order.order_receiver}}
            </div>
          </div>
          <div class="row">
            <div class="column">
            收货人地址：{{order.order_address}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              收货人联系电话：{{order.order_phone}}
            </div>
          </div>
          <div class="row">
            <div class="column">
              订单总价：<i class="fi-yen"></i> {{order.order_price}}
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
                <div class="button receive-reject" v-on:click="handle_order('accept', order.order_id)">接单</div>
                <div class="button receive-reject" v-on:click="handle_order('close', order.order_id)">拒单</div>
              </template>
              <div v-if="order.order_status == '已接单'" class="button delivery" v-on:click="handle_order('transport', order.order_id)">配送</div>
            </div>
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

  .order-info {
    padding-left: 20px;
    padding-right: 20px;
    margin-top: 20px;
  }

  .receive-reject {
    margin-right: 10px;
  }

  .mouseoverstyle {
    border-left: 3px solid $grey2;
  }
</style>
