<script>
  export default {
    name: 'Register',
    /*data: function() {
      return {
        username: 'ice'
      }
    }*/
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div class="register-container">
    <h3>商家注册</h3>
    <form method="post" action="./" class="register-form">
      <div class="input-form">
        <span class="fi-torso span-img"></span>
        <input id="username" class="input-span" name="username" type="text" placeholder="Please enter your username."></input>
      </div>
      <div class="input-form">
        <span class="fi-lock span-img"></span>
        <input id="password" class="input-span" name="password" type="password" placeholder="Please enter your password."></input>
      </div>
      <input id="register_submit" class="button expanded" type="submit" value="注册"></input>
    </form>
    <a v-link="{name: 'login'}" class="login-link">已有账号?登录</a>
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
    height: 270px;
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