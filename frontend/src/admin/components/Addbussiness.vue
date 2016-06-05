<script>
  export default {
    name: "Add",
    methods: {
      isValidate: function(psw1, psw2, phone) {
        var error_msg = "";
        var phone_reg = /^[1-9][0-9]{10}$/;
        if (psw1 != psw2) {
          error_msg += "You should enter the same password twice.\n";
        }
        if (!phone_reg.test(phone)) {
          error_msg += "You should enter a valid telephone number.\n";
        }
        if (error_msg == "") return true;
        else {
          alert(error_msg);
          return false;
        }
      },
      submit_register_bussiness: function(event) {
        var username = $("#add_bussiness_name").val();
        var password = $("#add_bussiness_password").val();
        var password_ = $("#add_bussiness_password_again").val();
        var nickname = $("#add_bussiness_nickname").val();
        var account_type = "bussiness";
        var name = $("#add_store_name").val();
        var address = $("#add_store_address").val();
        var announcement = $("#add_store_announcement").val();
        var description = $("#add_store_description").val();
        var phone = $("#add_store_phone").val();
        if (this.isValidate(password,password_,phone)) {
          var bussiness_data = {
            username: username,
            password: password,
            nickname: nickname,
            account_type: account_type
          };
          $.ajax({
            url: "../api/seller",
            async: false,
            type: "POST",
            contentType: "application/json;charset=utf-8",
            dataType: "json",
            processData: false,
            data: JSON.stringify(bussiness_data),
            error: function(xhr, status) {
              alert("Error: " + status);
            },
            success: function(data) {
              console.log("success");
              var newbussiness_id = data.data.id;
              var newbussiness_token = data.data.token;
              var image_flag = false;
              var image_id = "";
              console.log(newbussiness_id);
              console.log(newbussiness_token);
              if ($("#add_store_image").val() != "") {
                image_flag = true;
                var formData = new FormData($("#upload_image_form")[0]);
                $.ajax({
                  url: "../api/upload",
                  async: false,
                  type: "POST",
                  headers: {'Authorization-Token': newbussiness_token},
                  data: formData,
                  contentType: false,
                  processData: false,
                  dataType: "json",
                  error: function(xhr, status) {
                    alert("Error: " + status);
                  },
                  success: function(data) {
                    image_id = data.data.id;
                  }
                });
              }
              var store_data = {
                name: name,
                address: address,
                announcement: announcement,
                description: description,
                phone: phone
              };
              if (image_flag) store_data.image_ids = image_id;
              $.ajax({
                url: "../api/store",
                async: false,
                type: "POST",
                headers: {'Authorization-Token': newbussiness_token},
                contentType: "application/json;charset=utf-8",
                dataType: "json",
                processData: false,
                data: JSON.stringify(store_data),
                error: function(xhr, status) {
                  alert("Error: " + status);
                },
                success: function(data) {
                  console.log("success");
                  var newstore_id = data.data.id;
                  window.location.href = "#!/home";
                }
              });
            }
          });
        }
        event.preventDefault();
        return false;
      }
    }
  }
</script>

<template>
  <div class="row add_info">
    <div class="column small-6 add_info_col">
      <h4>添加商家(注册商家)</h4>
      <form enctype="multipart/form-data" id="upload_image_form">
        <label>商店图片：
          <input type="file" id="add_store_image" name="image"></input>
        </label>
      </form>
      <form method="post" action="../api/seller">
        <label>商家账户名：
          <input type="text" id="add_bussiness_name" placeholder="商家账户名" name="username" required="required"></input>
        </label>
        <label>商家账户密码：
          <input type="password" id="add_bussiness_password" placeholder="商家账户密码" name="password" required="required"></input>
        </label>
        <label>重新输入一次密码：
          <input type="password" id="add_bussiness_password_again" placeholder="重新输入一次密码" required="required"></input>
        </label>
        <label>商家昵称：
          <input type="text" id="add_bussiness_nickname" placeholder="商家昵称" name="nickname" required="required"></input>
        </label>
        <label>商店名称：
          <input type="text" id="add_store_name" placeholder="商店名称" name="name" required="required"></input>
        </label>
        <label>商店地址：
          <input type="text" id="add_store_address" placeholder="商店地址" name="address" required="required"></input>
        </label>
        <label>商店宣告：
          <input type="text" id="add_store_announcement" placeholder="商店宣告" name="announcement" required="required"></input>
        </label>
        <label>商店描述：
          <input type="text" id="add_store_description" placeholder="商店描述" name="description" required="required"></input>
        </label>
        <label>商家联系电话：
          <input type="tel" id="add_store_phone" placeholder="商家联系电话" name="phone" required="required"></input>
        </label>
        <div id="submit_add_info">
          <input type="submit" class="button" v-on:click="submit_register_bussiness($event)" value="确认添加"></input>
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
