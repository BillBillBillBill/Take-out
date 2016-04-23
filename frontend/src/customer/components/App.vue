<script>
  import Navbar from './Navbar.vue'

  export default {
    name: "App",

    components: {
      'navbar': Navbar
    }
  }

</script>

<template>
  <div>
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>
