<script>
  export default {
    name: "About",
    data: function() {
      return {
        bussiness_image: '../images/flower.jpg',
        bussiness_name: '鸡公煲',
        bussiness_address: '新天地三楼',
        bussiness_tel: '18819481246',
        resetInfo: false
      }
    },
    methods: {
      changeResetState: function() {
        this.resetInfo = true;
      },
      isValidate: function(event) {
        var name = $("#bussiness_name").val();
        var address = $("#bussiness_address").val();
        var tel = $("#bussiness_tel").val();
        if (address == "" || tel == "") return false;
        var tel_reg = /^[1-9][0-9]{10}$/;
        if (tel_rg.test(tel)) {
          this.bussiness_name = name;
          this.bussiness_address = address;
          this.bussiness_tel = tel;
          return true;
        } else alert("You should enter a valid telephone number.");
        event.preventDefault();
        return false;
      }
    }
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 align-center bussiness-info">
    <div class="column">
      <img :src="bussiness_image" class="bussiness_image" alt="my bussiness image">
    </div>
    <div class="column">
      <h4>{{bussiness_name}}</h4>
      <div><i class="fi-marker"></i> {{bussiness_address}}</div>
      <div><i class="fi-telephone"></i> {{bussiness_tel}}</div>
      <div class="button" v-on:click="changeResetState">修改商家信息</div>
      <form method="post" action="./" v-if="resetInfo">
        <label>商家名：
          <input type="text" id="bussiness_name" name="bussiness_name" :value="bussiness_name" required="required"></input>
        </label>
        <label>商家图标：
          <input type="file" id="bussiness_image" name="bussiness_image"></input>
        </label>
        <label>商家地址：
          <input type="text" id="bussiness_address" name="bussiness_address" :value="bussiness_address" required="required"></input>
        </label>
        <label>商家联系电话：
          <input type="tel" id="bussiness_tel" name="bussiness_tel" :value="bussiness_tel" required="required"></input>
        </label>
        <div id="submit_info_button">
          <input type="submit" class="button" v-on:click="isValidate($event)" value="确认修改信息"></input>
        </div>
      </form>
    </div>
  </div>
</template>
