<script>
  import Orbitimages from './Orbitimages.vue'

  export default {
  	name: "Detail",
    props: ['searchText'],

  	components: {
  	  'orbitimages': Orbitimages
  	},

    data: function() {
      return {
        delivery_information_list: [],
        showflag: false,
        currentid: this.$route.params.bussinessId,
        shopping_cart: [],
        total: 0,
        food_list: [],
        current_food: {},
        current_food_review: []
      }
    },
    methods: {
      //将食物添加到购物车
      addFood: function(food_id, name, price, count) {
        var that = this;
        var isFind = false;
        for (var i = 0; i < that.shopping_cart.length; i++) {
          if (that.shopping_cart[i].food_id == food_id) {
            that.shopping_cart[i].count += count;
            that.total += parseInt(price)*parseInt(count);
            isFind = true;
            break;
          }
        }
        if (!isFind) {
          var temp = {
            food_id: food_id,
            count: count,
            food_name: name,
            price: price
          };
          that.total += price*count;
          that.shopping_cart.push(temp);
        }
      },

      //获取收货信息列表
      getDeliveryInfo: function() {
        var that = this;
        $.ajax({
          url: "../api/delivery_information",
          async: false,
          type: "GET",
          headers: {'Authorization-Token': localStorage.customer_token},
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var list = data.data.delivery_information_list;
            if (that.delivery_information_list.length == 0) {
              for (var i = 0; i < list.length; i++) {
                var info = {
                  id: list[i].id,
                  address: list[i].address,
                  phone: list[i].phone,
                  receiver: list[i].receiver
                };
                that.delivery_information_list.push(info);
              }
              console.log(that.delivery_information_list[0]);
            }
          }
        });
      },

      //删除指定的一条收货信息
      deleteDelivery_info: function(id) {
        var that = this;
        $.ajax({
          url: "../api/delivery_information/" + id,
          type: "DELETE",
          headers: {'Authorization-Token': localStorage.customer_token},
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var length = that.delivery_information_list.length;
            for (var i = 0; i < length; i++) {
              if (that.delivery_information_list[i].id == id) {
                that.delivery_information_list.splice(i, 1);
                break;
              }
            }
          }
        });
      },

      //控制是否显示新增收货信息的表单
      show_flag: function() {
        if (this.showflag) this.showflag = false;
        else this.showflag = true;
      },

      //提交确认添加一条收货信息
      submit_add_delivery: function() {
        var that = this;
        var add_data = {
          address: $("#add_address").val(),
          phone: $("#add_phone").val(),
          receiver: $("#add_receiver").val()
        };
        $.ajax({
          url: "../api/delivery_information",
          async: false,
          type: "POST",
          headers: {'Authorization-Token': localStorage.customer_token},
          data: JSON.stringify(add_data),
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            add_data.id = data.data.id;
            that.delivery_information_list.push(add_data);
          }
        });
      },

      //提交订单
      postOrder: function(event) {
        var that = this;
        var delivery_id = $(":checked").val();
        var info = {
          food_list: that.shopping_cart,
          delivery_information_id: delivery_id,
          store_id: that.currentid
        };
        $.ajax({
          url: "../api/order",
          async: false,
          type: "POST",
          headers: {'Authorization-Token': localStorage.customer_token},
          contentType: "application/json;charset=utf-8",
          processData: false,
          data: JSON.stringify(info),
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var order_id = data.data.id;
            console.log(order_id);
            that.shopping_cart = [];
            that.total = 0;
          }
        });
        event.preventDefault();
        return false;
      },

      //检验输入表单内容是否合理
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

      //将表单内容置空
      emptyInput: function() {
        $("#address").val("");
        $("#tel").val("");
      },

      //获取指定食物的详细信息
      getFoodDetail: function(food_id) {
        var that = this;
        var list = that.food_list;
        for (var i = 0; i < list.length; i++) {
          if (list[i].food_id == food_id) {
            var info = {
              food_id: list[i].food_id,
              food_name: list[i].food_name,
              food_description: list[i].food_description,
              food_price: list[i].food_price,
              food_stock: list[i].food_stock,
              food_star: list[i].food_star,
              //food_comments: list[i].food_comments
            };
            that.current_food = info;
            var review = list[i].food_comments;
            console.log(review);
            for (var j = 0; j < review.length; j++) {
              var review_info = {
                customer: review[j].customer,
                star: review[j].star,
                content: review[j].content
              };
              var newDate = new Date();
              newDate.setTime(parseInt(review[j].created_time)*1000 + 3600000*8);
              var time = newDate.toLocaleString();
              review_info.created_time = time;
              that.current_food_review.push(review_info);
            }
            break;
          }
        }
      }
    },

    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        var querydata = {
          store_id: parseInt(that.currentid)
        };
        $.ajax({
          url: "../api/food",
          async: false,
          type: "GET",
          data: querydata,
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            if (that.food_list.length == 0) {
              var list = data.data.food_list;
              for (var i = 0; i < list.length; i++) {
                var info = {
                  food_description: list[i].description,
                  food_comments: list[i].food_review_list,
                  food_price: list[i].price,
                  food_name: list[i].name,
                  food_id: list[i].id,
                  food_stock: list[i].stock,
                  food_star: list[i].average_star,
                };
                if (list[i].images[0]) info.food_image = "../api/" + list[i].images[0].path;
                that.food_list.push(info);
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
      'food_list': function() {
        var food_list = this.food_list;
        for (var i in food_list) {
          new Foundation.Reveal($("#food" + food_list[i].food_id), {});
        }
      },
      'current_food': function() {
        new Foundation.Accordion($("#food_review_accordion"), {});
      },
    }
  }
</script>

<template>
<div>
  <orbitimages :currentid="currentid"></orbitimages>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <template v-for="item in food_list | filterBy searchText in 'food_name'">
      <div class="column">

        <!--查看特定食物详情-->
        <div class="reveal" :id='"food"+ item.food_id' data-reveal>
          <div class="row">
            <div class="column">
              <img :src="item.food_image" class="reveal_img" />
            </div>
            <div class="column">
              <div class="row">{{current_food.food_name}}</div>
              <div class="row">
                <i v-for="n in current_food.food_star" class="fi-star gold"></i><i v-for="n in (5-current_food.food_star)" class="fi-star gray"></i>
              </div>
              <div class="row price"><i class="fi-yen"></i> {{current_food.food_price}}</div>
              <div class="row count_detail">剩余<span class="item_count">{{current_food.food_stock}}</span>份</div>
              <div class="row">
                <strong>描述：</strong>{{current_food.food_description}}
              </div>
            </div>
          </div>
          <!--将食物加入购物车按钮-->
          <div class="button expanded margin-button" data-open="order_again" v-on:click="addFood(current_food.food_id, current_food.food_name, current_food.food_price, 1)">加入购物车</div>
          <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
          <!--食物评价列表-->
          <ul id="food_review_accordion" class="show_comments accordion" data-accordion data-multi-expand="true">
             <li v-for="comment in current_food_review"  class="accordion-item is-active" data-accordion-item>
               <a class="accordion-title">
                <span>{{comment.customer}}</span>
                <i v-for="n in comment.star" class="fi-star gold"></i><i v-for="n in (5 - comment.star)" class="fi-star gray"></i>
                <span>{{comment.created_time}}</span>
               </a>
               <div class="description accordion-content" data-tab-content>{{comment.content}}</div>
             </li>
          </ul>
        </div>

        <!--食物信息-->
        <a :data-open='"food"+ item.food_id' v-on:click="getFoodDetail(item.food_id)">
        <img :src="item.food_image" class="thumbnail food_image"></a>
        <div class="row food_detail">
          <div class="column">{{item.food_name}}</div>
          <div class="column-6">
            <i v-for="n in item.food_star" class="fi-star gold"></i><i v-for="n in (5-item.food_star)" class="fi-star gray"></i>
          </div>
          <div class="column price"><i class="fi-yen"></i> {{item.food_price}}</div>
        </div>
        <div class="button expanded" data-open="order_again" v-on:click="addFood(item.food_id, item.food_name, item.food_price, 1)">加入购物车</div>

      </div>
    </template>

    <!--下单/确认下单按钮-->
    <div class="button order_button" data-open="addorder" v-on:click="getDeliveryInfo">去下单</div>
    <div class="reveal" id="order_again" data-reveal>
      <h2>成功加入购物车</h2>
      <div class="button expanded" data-close aria-label="Close modal">继续挑选食物</div>
      <div class="button expanded" data-open="addorder" v-on:click="getDeliveryInfo">完成啦~去下单</div>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <!--弹出下单窗口-->
    <form class="reveal" id="addorder" method="post" action="./" data-reveal>

      <div>
        <!--显示所有收货信息-->
        <template v-for="information in delivery_information_list">
          <div class="callout small">
            <div class="row">
              <div class="column small-1">
                <input type="radio" name="delivery_info" :value="information.id" v-if="$index == 0" checked="checked"></input>
                <input type="radio" name="delivery_info" :value="information.id" v-else></input>
              </div>
              <div class="column">
                <div class="row">
                  <div class="column">收货人：{{information.receiver}}</div>
                </div>
                <div class="row">
                  <div class="column">收货地址：{{information.address}}</div>
                </div>
                <div class="row">
                  <div class="column">收货人联系电话：{{information.phone}}</div>
                </div>
              </div>
              <div class="column align-middle small-2">
                <i class="fi-minus" v-on:click="deleteDelivery_info(information.id)"></i>
              </div>
            </div>
          </div>
        </template>

        <!--新增一个收货信息-->
        <i class="fi-plus" v-on:click="show_flag"></i>
        <div v-if="showflag">
          <label>收货人：
            <input type="text" id="add_receiver" name="receiver" required="required" placeholder="Enter the receiver"></input>
          </label>
          <label>收货地址：
            <input type="text" id="add_address" name="address" required="required" placeholder="Enter the address"></input>
          </label>
          <label>收货人联系电话：
            <input type="tel" id="add_phone" name="phone" required="required" placeholder="Enter the phone"></input>
          </label>
          <div class="button" v-on:click="submit_add_delivery">确认添加</div>
        </div>
      </div>


      <div>
        <!--显示订单中的食物列表-->
        <ul id="order_list">
          <li class="row order_head">
            <span class="column">食物名称</span>
            <span class="column">数量/份</span>
            <span class="column">单价/元</span>
            <span class="column">总价/元</span>
          </li>
          <template v-for="food in shopping_cart">
            <li class="row">
              <span class="column">{{food.food_name}}</span>
              <span class="column">{{food.count}}</span>
              <span class="column"><i class="fi-yen"></i> {{food.price}}</span>
              <span class="column">{{food.count}}x{{food.price}}={{food.count*food.price}}</span>
            </li>
          </template>
          <li class="row">
            <span class="column small-3 order_head">合计:</span>
            <span class="column small-3 small-offset-6"><i class="fi-yen"></i> {{total}}</span>
          </li>
        </ul>
      </div>

      <!--提交订单按钮-->
      <div id="submit_button">
        <input class="button expanded" type="submit" v-on:click="postOrder($event)" value="提交订单" data-close></input>
      </div>

      <!--关闭下单窗口-->
      <button class="close-button" data-close aria-label="Close modal" type="button" v-on:click="emptyInput()">
        <span aria-hidden="true">&times;</span>
      </button>

    </form>
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

.food_detail {
  margin-bottom: 10px;
}

.food_detail_ {
  margin-top: 10px;
  margin-bottom: 10px;
}

.price {
  text-align: right;
}

.count_detail {
  text-align: right;
}

.item_count {
  color: $black;
  font-weight: bold;
}

#order_list {
  margin: 0;
}

.order_head {
  font-weight: bold;
  margin: 0;
  color: $grey2;
}

.order_button {
  position: fixed;
  margin: 0;
  bottom: 0;
  right: 0;
}

#submit_button {
  margin-top: 10px;
}

img.reveal_img {
  height: 150px;
}

.margin-button {
  margin-top: 10px;
}

</style>