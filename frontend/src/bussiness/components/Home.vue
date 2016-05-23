<script>
  //import Sortbar from './Sortbar.vue'
  export default {
    name: "Home",

    props: ['foods', 'searchText'],
   /* data: function() {
      return {
      	sortpara: ''
      }
    }*/
    methods: {
      isValidate: function(event) {
      	var foodname = $("#food_name").val();
      	if (foodname == "") return false;
      	return true;
      },
      isAddfoodValidate: function(event) {
        return true;
      }
    },
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div>
  	<div class="row small-up-1 medium-up-2 large-up-4 bussiness-home">
  	  <template v-for="food in foods | filterBy searchText in 'name'">
  	  	<div class="column">
  	  	  <img class="thumbnail" :src="food.picture" />
  	  	  <div class="row food_detail">
  	  	  	<div class="column">{{food.name}}</div>
  	  	  	<div class="column-4"><i class="fi-yen"></i> {{food.price}}</div>
  	  	  	<div class="column amount">货存{{food.amount}}份</div>
  	  	  </div>
  	  	  <div class="button expanded" :data-open="food.id">修改信息</div>
  	  	</div>
  	  	<div class="reveal" :id="food.id" data-reveal>
  	  	  <form method="post" action="./">
  	  	  	<img :src="food.picture" />
  	  	  	<label>更改食物图片：
  	  	  	  <input type="file" id="food_image" name="foodimage"></input>
  	  	  	</label>
  	  	  	<label>食物名称：
  	  	  	  <input type="text" id="food_name" name="foodname" :value="food.name"></input>
  	  	  	</label>
  	  	  	<label>食物价格：
  	  	  	  <i class="fi-yen"></i> <input type="number" id="food_price" name="foodprice" :value="food.price"></input>
  	  	  	</label>
  	  	  	<label>食物货存：件
  	  	  	  <input type="number" id="id_amount" name="foodamount" :value="food.amount"></input>
  	  	  	</label>
  	  	  	<div id="submit_modify_food_info">
  	  	  	  <input class="button expanded" type="submit" value="确认修改食物信息" v-on:click="isValidate($event)"></input>
  	  	  	</div>
  	  	  </form>
  	  	  <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
  	  	</div>
        <div class="button add_food_button" data-open="addfood">添加菜式</div>
        <div class="reveal" id="addfood" data-reveal>
          <form method="post" action="./">
            <label>添加食物图片：
              <input type="file" id="addfood_image" name="addfoodimage" required="required"></input>
            </label>
            <label>添加食物名称：
              <input type="text" id="addfood_name" name="addfoodname" required="required" placeholder="Add Food Name"></input>
            </label>
            <label>添加食物价格：
              <input type="number" id="addfood_price" name="addfoodprice" required="required" placeholder="Add Food Price"></input>
            </label>
            <label>添加货存信息/件
              <input type="number" id="addfood_amount" name="addfoodamount" required="required" placeholder="Add Food Amount"></input>
            </label>
            <div id="submit_addfood_info">
              <input class="button expanded" type="submit" value="确认添加菜式" v-on:click="isAddfoodValidate($event)"></input>
            </div>
          </form>
          <button class="close-button" data-close aria-label="Close modal" type="button">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
  	  </template>
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
</style>
