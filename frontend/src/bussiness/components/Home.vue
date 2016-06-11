<script>
  export default {
    name: "Home",

    props: ['bussinessInfo', 'searchText'],
    data: function() {
      return {
      	food_list: []
      }
    },
    methods: {
      isValidate: function(event, id) {
        var that = this;
        var name = $("#food_name"+id).val();
        var description = $("#food_description"+id).val();
        var price = $("#food_price"+id).val();
        var stock = $("#food_stock"+id).val();
        var food_data = {
          name: name,
          description: description,
          price: price,
          stock: stock
        };
        $.ajax({
          url: "../api/food/" + id,
          async: false,
          type: "PUT",
          headers: {'Authorization-Token': localStorage.bussiness_token},
          contentType: "application/json;charset=utf-8",
          data: JSON.stringify(food_data),
          processData: false,
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            var list = that.food_list;
            for (var i = 0; i < list.length; i++) {
              if (list[i].food_id == id) {
                list[i].food_name = name;
                list[i].food_description = description;
                list[i].food_price = price;
                list[i].food_stock = stock;
                break;
              }
            }
          }
        });
      	event.preventDefault();
        return false;
      },
      isAddfoodValidate: function(event) {
        var that = this;
        var image_flag = false;
        var image_id = "";
        if ($("#addfood_image").val() != "") {
          image_flag = true;
          var formData = new FormData($("#upload_image_form")[0]);
          $.ajax({
            url: "../api/upload",
            async: false,
            type: "POST",
            headers: {'Authorization-Token': localStorage.bussiness_token},
            data: formData,
            contentType: false,
            processData: false,
            dataType: "json",
            error: function(xhr, status) {
              alert(JSON.parse(xhr.responseText).message);
            },
            success: function(data) {
              image_id = data.data.id;
            }
          });
        }
        var name = $("#addfood_name").val();
        var description = $("#addfood_description").val();
        var price = $("#addfood_price").val();
        var stock = $("#addfood_stock").val();
        var food_data = {
          name: name,
          description: description,
          price: price,
          stock: stock
        };
        if (image_flag) food_data.image_ids = image_id;
        $.ajax({
          url: "../api/food",
          type: "POST",
          headers: {'Authorization-Token': localStorage.bussiness_token},
          contentType: "application/json;charset=utf-8",
          dataType: "json",
          processData: false,
          data: JSON.stringify(food_data),
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
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
        console.log("store_id: " + localStorage.bussiness_store_id);
        var querydata = {store_id: parseInt(localStorage.bussiness_store_id)};
        $.ajax({
          url: "../api/food",
          async: false,
          type: "GET",
          data: querydata,
          dataType: "json",
          error: function(xhr, status) {
            alert(JSON.parse(xhr.responseText).message);
          },
          success: function(data) {
            console.log("success");
            console.log("length: " + that.food_list.length);
            if (that.food_list.length == 0) {
              var list = data.data.food_list;
              for (var i = 0; i < list.length; i++) {
                var info = {
                  food_description: list[i].description,
                  food_comments: list[i].food_review_list,
                  food_price: list[i].price,
                  food_name: list[i].name,
                  food_id: list[i].id,
                  food_stock: list[i].stock,
                  food_star: list[i].average_star,
                };
                if (list[i].images[0]) info.food_image = "../api/" + list[i].images[0].path;
                that.food_list.push(info);
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
    },
    watch: {
      'food_list': function() {
        var food_list = this.food_list;
        for (var i in food_list) {
          new Foundation.Reveal($("#food" + food_list[i].food_id), {});
        }
      }
    }
  }
</script>

<template>
  	<div class="row small-up-1 medium-up-2 large-up-4 bussiness-home">
  	  <template v-for="item in food_list | filterBy searchText in 'food_name'">
  	  	<div class="column">
  	  	  <img style="height: 200px" width="100%" :src="item.food_image"/>
  	  	  <div class="row food_detail">
  	  	  	<div class="column">{{item.food_name}}</div>
  	  	  	<div class="column-4"><i class="fi-yen"></i> {{item.food_price}}</div>
  	  	  	<div class="column amount">货存{{item.food_stock}}份</div>
  	  	  </div>
  	  	  <div class="button expanded" :data-open='"food" + item.food_id'>修改信息</div>
  	  	</div>
  	  	<div class="reveal" :id='"food" + item.food_id' data-reveal>
  	  	  <form method="post" action="./">
  	  	  	<img :src="item.food_image" class="reveal_img" />
  	  	  	<label>食物名称：
  	  	  	  <input type="text" :id='"food_name" + item.food_id' name="name" :value="item.food_name" required="required"></input>
  	  	  	</label>
            <label>食物描述：
              <input type="text" :id='"food_description" + item.food_id' name="descripiton" :value="item.food_description" required="required"></input>
            </label>
  	  	  	<label>食物价格：
  	  	  	  <i class="fi-yen"></i> <input type="number" :id='"food_price" + item.food_id' name="price" :value="item.food_price" required="required"></input>
  	  	  	</label>
  	  	  	<label>食物货存：件
  	  	  	  <input type="number" :id='"food_stock" + item.food_id' name="stock" :value="item.food_stock" required="required"></input>
  	  	  	</label>
  	  	  	<div id="submit_modify_food_info">
  	  	  	  <input class="button expanded" type="submit" value="确认修改食物信息" v-on:click="isValidate($event, item.food_id)" data-close></input>
  	  	  	</div>
  	  	  </form>
  	  	  <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
  	  	</div>
      </template>
        <div class="reveal" id="addfood" data-reveal>
          <form enctype="multipart/form-data" id="upload_image_form">
            <label>添加食物图片：
              <input type="file" id="addfood_image" name="image" required="required"></input>
            </label>
          </form>
          <form method="post">
            <label>添加食物名称：
              <input type="text" id="addfood_name" name="name" required="required" placeholder="Add Food Name"></input>
            </label>
            <label>添加食物描述：
              <input type="text" id="addfood_description" name="description" required="required" placeholder="Add Food Description"></input>
            </label>
            <label>添加食物价格：
              <input type="number" id="addfood_price" name="price" required="required" placeholder="Add Food Price"></input>
            </label>
            <label>添加货存信息/件
              <input type="number" id="addfood_stock" name="stock" required="required" placeholder="Add Food Amount"></input>
            </label>
            <div id="submit_addfood_info">
              <input class="button expanded" type="submit" value="确认添加菜式" v-on:click="isAddfoodValidate($event)" data-close></input>
            </div>
          </form>
          <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

      <div class="button add_food_button" data-open="addfood">添加菜式</div>
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

  .add_food_button {
    position: fixed;
    margin: 0;
    bottom: 0;
    right: 0;
  }

  .bussiness-home {
    margin-top: 20px;
  }

  .amount {
    text-align: right;
  }

  .reveal_img {
    height: 150px;
  }
</style>
