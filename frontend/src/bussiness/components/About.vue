<script>
  export default {
    name: "About",
    props: ['isLog'],
    data: function() {
      return {
        nickname: localStorage.bussiness_nickname,
        resetInfo: false,
        resetInfo_: false
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
            url: "../api/seller/" + localStorage.bussiness_id,
            type: "PUT",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify({nickname: name}),
            processData: false,
            error: function(xhr, status) {
              alert("Error: " + status);
            },
            success: function(data) {
              localStorage.bussiness_nickname = name;
              that.nickname = localStorage.bussiness_nickname;
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
            url: "../api/seller/" + localStorage.bussiness_id,
            type: "PUT",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify({password: password}),
            processData: false,
            error: function(xhr, status) {
              alert("Error: " + status);
            },
            success: function(data) {
              console.log("success");
              that.resetInfo_ = false;
              localStorage.bussiness_token = "";
              localStorage.bussiness_id = "";
              localStorage.bussiness_nickname = "";
              that.isLog = false;
              window.location.href = "#!/login";
            }
          });
        else alert("You should enter the same password twice.");
        event.preventDefault();
        return false;
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/seller/" + localStorage.bussiness_id,
          async: false,
          type: "GET",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var info = data.data.seller;
            that.nickname = info.nickname;
            console.log(info.username);
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
  <div class="row bussiness-info">
    <div class="align-center">
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

  .bussiness-info {
    margin-top: 20px;
  }

  .align-center {
    padding: 10px;
    margin: auto;
  }
</style>