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
        sortpara: ''
      }
    },
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
<div>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <sortbar :sortpara.sync="sortpara"></sortbar>
  </div>
  <div class="row small-up-1 medium-up-2 large-up-4" id="customer-home">
    <template v-for="item in bussiness | filterBy searchText in 'title' | orderBy sortpara -1">
      <div class="column">
        <a v-link="{name: 'detail', params: {bussinessId: item.id}}">
          <div class="row customer-item" small-2>
            <div class="column">
              <img :src="item.picture" />
            </div>
            <div class="column">
              <div class="row">
                {{item.title}}
              </div>
              <div class="row">
                <i v-for="n in item.star" class="fi-star gold"></i>
                <i v-for="n in (5-item.star)" class="fi-star gray"></i>
              </div>
              <div class="row">
                月售<span class="item_count">{{item.count}}</span>单
              </div>
              <div class="row">
                <i class="fi-telephone"></i> {{item.number}}
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
