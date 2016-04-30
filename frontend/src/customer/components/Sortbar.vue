<script>
  export default {
    name: "Sortbar",
    props: ['sortpara'],
    data: function() {
      return {
      	menus: [
      	  {
      	  activeflag: true,
      	  content: "默认排序",
      	  sortparam: ''},
      	  {
      	  activeflag: false,
      	  content: "销量高",
      	  sortparam: 'count'},
      	  {
      	  activeflag: false,
      	  content: "评价好",
      	  sortparam: 'star'}
      	]
      }
    },
    methods: {
      	sortBy: function(sortparam) {
      	  for (var i = 0; i < this.menus.length; i++) {
      	    if (this.menus[i].sortparam != sortparam) this.menus[i].activeflag = false;
      	    else this.menus[i].activeflag = true;
      	  }
      	  this.sortpara = sortparam;
      	}
    }
  }
</script>

<template>
  <div id="sort-bar">
  	<ul class="menu">
  	  <li v-for="menu in menus" v-bind:class="{active: menu.activeflag}" v-on:click="sortBy(menu.sortparam)"><a>{{menu.content}}</a></li>
  	</ul>
  </div>
</template>