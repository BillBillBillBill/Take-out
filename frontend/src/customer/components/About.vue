<script>
  import QuoteService from '../services/quote'

  export default {
    name: "About",
    props: ['isLog'],
    data: function() {
      return {
        nickname: localStorage.customer_nickname,
        resetInfo: false,
        resetInfo_: false,
        delivery_information_list: [],
        showflag: false
      }
    },
    methods: {
      changeResetState: function() {
        if (this.resetInfo) this.resetInfo = false;
        else {
          this.resetInfo = true;
          this.resetInfo_ = false;
        }
      },
      changeResetState_: function() {
        if (this.resetInfo_) this.resetInfo_ = false;
        else {
          this.resetInfo_ = true;
          this.resetInfo = false;
        }
      },
      submit_nickname: function(event) {
        var that = this;
        var name = $("#nickname").val();
        if (name != "")
          $.ajax({
            url: "../api/customer/" + localStorage.customer_id,
            type: "PUT",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify({nickname: name}),
            processData: false,
            error: function(xhr, status) {
              alert("Error: " + status);
            },
            success: function(data) {
              localStorage.customer_nickname = name;
              that.nickname = localStorage.customer_nickname;
              that.resetInfo = false;
              window.location.reload();
            }
          });
        event.preventDefault();
        return false;
      },
      submit_password: function(event) {
        var that = this;
        var password = $("#password").val();
        var password_ = $("#password_").val();
        if (password_ === password)
          $.ajax({
            url: "../api/customer/" + localStorage.customer_id,
            type: "PUT",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify({password: password}),
            processData: false,
            error: function(xhr, status) {
              alert("Error: " + status);
            },
            success: function(data) {
             // that.personal_info.nickname = $("#nickname").val();
              that.resetInfo_ = false;
              localStorage.customer_token = "";
              localStorage.customer_id = "";
              localStorage.customer_nickname = "";
              that.isLog = false;
              window.location.href = "#!/login";
            }
          });
        else alert("You should enter the same password twice.");
        event.preventDefault();
        return false;
      },
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
      show_flag: function() {
        if (this.showflag) this.showflag = false;
        else this.showflag = true;
      },
      submit_add_delivery: function(event) {
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
            that.showflag = false;
          }
        });
        event.preventDefault();
        return false;
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/customer/" + localStorage.customer_id,
          async: false,
          type: "GET",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var info = data.data.customer;
            that.nickname = info.nickname;
          }
        });
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
  <div class="row small-up-1 medium-up-2 my-info align-center container">
    <div class="column">
      <h4>昵称：{{nickname}}</h4>
      <div class="button" v-on:click="changeResetState">修改昵称</div>
      <div class="button" v-on:click="changeResetState_">修改密码</div>
      <form method="put" v-if="resetInfo">
        <label>昵称：
          <input type="text" id="nickname" name="nickname" :value="nickname" required="required"></input>
        </label>
        <div id="submit_nickname_reset">
          <input class="button" type="submit" v-on:click="submit_nickname($event)"></input>
        </div>
      </form>
      <form method="put" v-if="resetInfo_">
        <label>修改密码：
          <input type="password" id="password" name="password" placeholder="输入新密码" required="required"></input>
        </label>
        <label>确认密码：
          <input type="password" id="password_" placeholder="重新输入一次密码" required="required"></input>
        </label>
        <div id="submit_password_reset">
          <input class="button" type="submit" v-on:click="submit_password($event)"></input>
        </div>
      </form>
    </div>
    <div class="column">
      <h4>收货信息</h4>
      <template v-for="information in delivery_information_list">
        <div class="callout small">
          <div class="row">
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
      <i class="fi-plus" v-on:click="show_flag"></i>
      <form method="POST" action="./" v-if="showflag">
        <label>收货人：
          <input type="text" id="add_receiver" name="receiver" required="required" placeholder="Enter the receiver"></input>
        </label>
        <label>收货地址：
          <input type="text" id="add_address" name="address" required="required" placeholder="Enter the address"></input>
        </label>
        <label>收货人联系电话：
          <input type="tel" id="add_phone" name="phone" required="required" placeholder="Enter the phone"></input>
        </label>
        <div id="submit_add_delivery">
          <input type="submit" class="button" v-on:click="submit_add_delivery($event)" value="确认添加"></input>
        </div>
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

  i:hover {
    cursor: hand;
    cursor: pointer;
  }

  .my-info {
    margin-top: 20px;
  }
  .my-picture {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 1px solid $grey2;
  }
</style>