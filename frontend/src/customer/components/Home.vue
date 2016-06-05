<script>
  import Sortbar from './Sortbar.vue'

  export default {
    name: "Home",
    components: {
      'sortbar': Sortbar
    },
    props: ['bussiness', 'searchText'],
    data: function() {
      return {
        sortpara: '',
        storelist: []
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/store",
          async: false,
          type: "GET",
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            if (that.storelist.length == 0) {
              var list = data.data.store_list;
              for (var i = 0; i < list.length; i++) {
                var info = {
                  store_id: list[i].id,
                  store_name: list[i].name,
                  store_phone: list[i].phone,
                  store_address: list[i].address,
                  total_orders_number: list[i].total_orders_num,
                  average_star: list[i].average_star
                };
                if (list[i].images[0]) info.store_image = "../api/" + list[i].images[0].path;
                that.storelist.push(info);
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
    }
  }
</script>

<template>
<div>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <sortbar :sortpara.sync="sortpara"></sortbar>
  </div>
  <div class="row small-up-1 medium-up-2 large-up-4" id="customer-home">
    <template v-for="item in storelist | filterBy searchText in 'store_name' | orderBy sortpara -1">
      <div class="column">
        <a v-link="{name: 'detail', params: {bussinessId: item.store_id}}">
          <div class="row customer-item" small-2>
            <div class="column">
              <img :src="item.store_image" />
            </div>
            <div class="column">
              <div class="row">
                {{item.store_name}}
              </div>
              <div class="row">
                <i v-for="n in item.average_star" class="fi-star gold"></i>
                <i v-for="n in (5-item.average_star)" class="fi-star gray"></i>
              </div>
              <div class="row">
                月售<span class="item_count">{{item.total_orders_number}}</span>单
              </div>
              <div class="row">
                <i class="fi-telephone"></i> {{item.store_phone}}
              </div>
              <div class="row">
                <i class="fi-marker"></i> {{item.store_address}}
              </div>
            </div>
          </div>
        </a>
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

  #customer-home {
    border: 1px solid rgb(169, 169, 169);
  }

  .customer-item {
    padding-top: 15px;
    padding-bottom: 20px;
    color: gray;
  }
</style>
