<script>
  export default {
  	name: 'Register',
  	props: ['adminIfno', 'isLog'],
    methods: {
      submit_register: function(event) {
        var that = this;
        var username = $("#username").val();
        var password = $("#password").val();
        var nickname = $("#nickname").val();
        var account_type = "admin";
        var data = {
          username: username,
          password: password,
          nickname: nickname,
          account_type: account_type
        };
        $.ajax({
          url: "../api/admin",
          async: false,
          type: "POST",
          //heardes: {'HTTP_AUTHORIZATION_TOKEN': 'your accessToken'},
          contentType: 'application/json',
          dataType: "json",
          processData: false,
          data: JSON.stringify(data),
          error: function(message) {
            alert("Error: " + message);
          },
          success: function(data) {
            //console.log("success");
            localStorage.admin_token = data.data.token;
            localStorage.admin_id = data.data.id;
            that.isLog = true;
            $.ajax({
              url: "../api/admin/" + localStorage.admin_id,
              async: false,
              type: "GET",
              error: function(message) {
                alert("Error: " + message);
              },
              success: function(data) {
                that.adminInfo = data.data.admin;
                localStorage.admin_nickname = that.adminInfo.nickname;
              }
            });
            window.location.href = "#!/home";
          }
        });
        event.preventDefault();
        return false;
      }
    }
  }
</script>

<template>
  <div class="register-container">
  	<h3>注册</h3>
  	<form method="post" action="./" class="register-form">
  	  <div class="input-form">
  	  	<span class="fi-torso span-img"></span>
  	  	<input id="username" class="input-span" name="username" type="text" placeholder="Please enter your username."></input>
  	  </div>
  	  <div class="input-form">
  	  	<span class="fi-lock span-img"></span>
  	  	<input id="password" class="input-span" name="password" type="password" placeholder="Please enter your password."></input>
  	  </div>
      <div class="input-form">
        <span class="fi-skull span-img"></span>
        <input id="nickname" class="input-span" name="nickname" type="text" placeholder="Please enter your nickname."></input>
      </div>
  	  <input id="register_submit" class="button expanded" type="submit" value="注册" v-on:click="submit_register($event)"></input>
  	</form>
  	<a v-link="{name: 'login'}" class="login-link">已有账号?登录</a>
    <div class="enter-row">
      <!--<a href="http://localhost:8081/#!/register" class="enter-link">商家版</a>-->
      <a href="http://localhost:8080/#!/register" class="enter-link">顾客版</a>
      <a class="enter-link">管理员版</a>
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

  .register-container {
  	margin: 50px auto;
  	width: 300px;
  	height: 290px;
  	border: 1px solid $grey2;
  }

  h3 {
  	padding: 10px;
  	padding-bottom: 0;
  }

  .register-form {
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

  .login-link {
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