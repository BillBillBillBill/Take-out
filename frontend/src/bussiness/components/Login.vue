<script>
  export default {
  	name: 'Login',
    props: ['bussinessInfo', 'isLog'],
  	methods: {
      submit_login: function(event) {
        var that = this;
        var username = $("#username").val();
        var password = $("#password").val();
        var data = {
          username: username,
          password: password
        };
        $.ajax({
          url: "../api/api-token-auth/bussiness",
          async: false,
          type: "POST",
          contentType: 'application/json',
          dataType: "json",
          processData: false,
          data: JSON.stringify(data),
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            //console.log("success");
            localStorage.bussiness_token = data.data.token;
            var token = localStorage.bussiness_token;
            var info = token.split("$");
            localStorage.bussiness_id = info[2];
            that.isLog = true;
            $.ajax({
              url: "../api/seller/" + localStorage.bussiness_id,
              async: false,
              type: "GET",
              error: function(xhr, status) {
                alert("Error: " + status);
              },
              success: function(data) {
                //console.log("success");
                that.bussinessInfo = data.data.seller;
                localStorage.bussiness_nickname = that.bussinessInfo.nickname;
                localStorage.bussiness_store_id = that.bussinessInfo.store;
                console.log(localStorage.bussiness_nickname);
              }
            });
            window.location.href = "#!/home";
          }
        });
        event.preventDefault();
        return false;
      }
    },
  	ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div class="login-container">
  	<h3>登录</h3>
  	<form method="post" action="./" class="login-form">
  	  <div class="input-form">
  	  	<span class="fi-torso span-img"></span>
  	  	<input id="username" class="input-span" name="username" type="text" placeholder="Please enter your username."></input>
  	  </div>
  	  <div class="input-form">
  	  	<span class="fi-lock span-img"></span>
  	  	<input id="password" class="input-span" name="password" type="password" placeholder="Please enter your password."></input>
  	  </div>
  	  <input id="login_submit" class="button expanded" type="submit" value="登录" v-on:click="submit_login($event)"></input>
  	</form>
  	<a v-link="{name: 'register'}" class="register-link">新用户注册</a>
  	<div class="enter-row">
      <a class="enter-link">商家版</a>
      <a href="http://localhost:8080/#!/login" class="enter-link">顾客版</a>
      <a href="http://localhost:8082/#!/login" class="enter-link">管理员版</a>
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

  .login-container {
  	margin: 50px auto;
  	width: 300px;
  	height: 290px;
  	border: 1px solid $grey2;
  }

  h3 {
  	padding: 10px;
  	padding-bottom: 0;
  }

  .login-form {
  	padding: 10px;
  	position: relative;
  }

  .input-span {
  	padding-left: 30px;
  }

  .span-img {
  	position: absolute;
  	padding-left: 5px;
  	padding-right: 5px;
  	background-color: $grey3;
  	left: 16px;
  	margin-top: 7.5px;
  }

  .register-link {
  	padding-right: 10px;
  	float: right;
  	font-size: 12px;
  	margin-top: -10px;
  }

  .enter-row {
  	padding: 10px;
  	text-align: center;
  }

  .enter-link {
  	font-size: 12px;
  	padding: 10px;
  	text-decoration: underline;
  }
</style>