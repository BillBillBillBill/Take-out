<script>
  export default {
  	name: 'Login',
    props: ['adminInfo', 'isLog'],
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
          url: "../api/api-token-auth/admin",
          async: false,
          type: "POST",
          contentType: 'application/json',
          dataType: "json",
          processData: false,
          data: JSON.stringify(data),
          error: function(xhr) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            //console.log("success");
            localStorage.admin_token = data.data.token;
            var token = localStorage.admin_token;
            var info = token.split("$");
            localStorage.admin_id = info[2];
            that.isLog = true;
            $.ajax({
              url: "../api/admin/" + localStorage.admin_id,
              async: false,
              type: "GET",
              error: function(xhr) {
                alert(JSON.parse(xhr.responseText).message);
              },
              success: function(data) {
                //console.log("success");
                that.adminInfo = data.data.admin;
                localStorage.admin_nickname = that.adminInfo.nickname;
                console.log(localStorage.admin_nickname);
              }
            });
            window.location.href = "#!/complain";
          }
        });
        event.preventDefault();
        return false;
      }
    }
  }
</script>

<template>
  <div class="login-container">
  	<h3>管理员登录</h3>
  	<form method="post" action="api/api-token-auth/admin" class="login-form">
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
  	height: 270px;
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