<script>
  import Navbar from './Navbar.vue'

  export default {
    name: "App",

    components: {
      'navbar': Navbar
    },

    data: function() {
      return {
        searchText: '',
        customerInfo: {},
        isLog: false
      }
    }
  }

</script>

<template>
  <div>
    <navbar :search-text.sync="searchText" :customer-info.sync="customerInfo" :is-log.sync="isLog"></navbar>
    <router-view :bussiness.sync="bussiness" :search-text.sync="searchText" :customer-info.sync="customerInfo" :is-log.sync="isLog"></router-view>
  </div>
</template>
