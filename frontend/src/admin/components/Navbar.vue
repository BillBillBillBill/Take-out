<script>
  export default {
    name: "Navbar",
    props: ['searchText']
  }
</script>

<template>
<div class="top-bar">
  <div class="top-bar-title" data-hide-for="medium">
    <span data-responsive-toggle="responsive-menu" data-hide-for="medium">
      <button class="menu-icon dark" type="button" data-toggle></button>
    </span>
  </div>
  <div id="responsive-menu">
    <div class="top-bar-left">
      <ul class="menu">
        <li class="menu-text">Admin</li>
        <li><a v-link="{name: 'home'}">所有商家</a></li>
        <li><a v-link="{name: 'complain'}">所有投诉</a></li>
        <li><a v-link="{name: 'about'}">添加商家</a></li>
      </ul>
    </div>
    <div class="top-bar-right">
      <ul class="menu">
        <li><input type="search" placeholder="Search" v-model="searchText"></li>
        <!--<li><button type="button" class="button">Search</button></li>-->
      </ul>
    </div>
  </div>
</div>
</template>
