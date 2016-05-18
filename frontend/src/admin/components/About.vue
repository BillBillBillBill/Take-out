<script>
  export default {
    name: "About",
    methods: {
      isValidate: function(event) {
        var name = $("#add_bussiness_name").val();
        var address = $("#add_bussiness_address").val();
        var tel = $("#add_bussiness_tel").val();
        if (address == "" || tel == "") return false;
        var tel_reg = /^[1-9][0-9]{10}$/;
        if (tel_rg.test(tel)) return true;
        else alert("You should enter a valid telephone number.");
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
  <div class="row add_info">
    <div class="column small-6 add_info_col">
      <h4>添加商家</h4>
      <form method="post" action="./">
        <label>商家名：
          <input type="text" id="add_bussiness_name" placeholder="商家名称" required="required"></input>
        </label>
        <label>商家地址：
          <input type="text" id="add_bussiness_address" placeholder="商家地址" required="required"></input>
        </label>
        <label>商家联系电话：
          <input type="tel" id="add_bussiness_tel" placeholder="商家联系电话" required="required"></input>
        </label>
        <div id="submit_add_info">
          <input type="submit" class="button" v-on:click="isValidate($event)" value="确认添加"></input>
        </div>
      </form>
    </div>
  </div>
</template>

<style lang="sass">
  // Imports
  @import "../variables.scss";

  // Styles
  .add_info {
    margin-top: 20px;
  }
  .add_info_col {
    margin: auto;
  }
  h4 {
    text-align: center;
  }
</style>
