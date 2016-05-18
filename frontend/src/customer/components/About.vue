<script>
  import QuoteService from '../services/quote'

  export default {
    name: "About",
    data: function() {
      return {
        username: '我是谁',
        mypicture: '../images/flower.jpg',
        default_address: '慎思园7号520',
        default_tel: '18819481246',
        resetInfo: false
      }
    },
    methods: {
      changeResetState: function() {
        this.resetInfo = true;
      },
      isValidate: function(event) {
        var address = $("#default_address").val();
        var tel = $("#default_tel").val();
        var username = $("#username").val();
        var picture = $("#mypicture").val();
        if (address == "" || tel == "") {
          return false;
        }
        var tel_reg = /^[1-9][0-9]{10}$/;
        if (tel_reg.test(tel)) {
          this.default_address = address;
          this.default_tel = tel;
          this.username = username;
          this.mypicture = picture;
          return true;
        } else alert("You should enter a valid telphone number.");
        event.preventDefault();
        return false;
      }
    },
    ready: function() {
      $(document).foundation();
    }

    /*data: function(){
      return {
        about: ""
      }
    },

    ready: function() {
      QuoteService.getQuote(this).then(function(response){
        this.$set('about', response.data[0].content);
      }, function(response){
        console.log(response);
      });
    }*/
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 my-info align-center ">
    <div class="column picture-column">
      <img class="my-picture" :src="mypicture" alt="my own picture"/>
    </div>
    <div class="column">
      <h4>{{username}}</h4>
      <div>我的默认收货地址：{{default_address}}</div>
      <div>我的收货人联系电话：{{default_tel}}</div>
      <div class="button" v-on:click="changeResetState">修改个人信息</div>
      <form method="post" action="./" v-if="resetInfo">
        <label>昵称：
          <input type="text" id="username" name="username" :value="username"></input>
        </label>
        <label>头像：
          <input type="file" id="mypicture" name="mypicture"></input>
        </label>
        <label>默认收货地址：
          <input type="text" id="default_address" name="default_address" :value="default_address"></input>
        </label>
        <label>默认收货人联系电话：
          <input type="tel" id="default_tel" name="default_tel" :value="default_tel"></input>
        </label>
        <div id="submit_info_button">
          <input class="button" type="submit" v-on:click="isValidate($event)" value="确认修改信息"></input>
        </div>
      </form>
    </div>
  </div>
</template>

