<script>
  import Sortbar from './Sortbar.vue'

  export default {
    name: "Home",
    components: {
      'sortbar': Sortbar
    },
    props: ['business', 'searchText'],
    data: function() {
      return {
        sortpara: ''
      }
    }
  }
</script>

<template>
<div>
  <div class="row small-up-1 medium-up-2 large-up-4">
    <sortbar :sortpara.sync="sortpara"></sortbar>
  </div>
  <div class="row small-up-1 medium-up-2 large-up-4" id="customer-home">
    <template v-for="item in business | filterBy searchText | orderBy sortpara -1">
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
                {{item.star}}
              </div>
              <div class="row">
                {{item.number}}
              </div>
              <div class="row">
                月售{{item.count}}单
              </div>
            </div>
          </div>
        </a>
      </div>
    </template>
  </div>
</div>
</template>
