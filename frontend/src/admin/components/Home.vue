<script>
  export default {
    name: "Home",
    props: ['bussiness', 'searchText'],
    methods: {
      cancelBussiness: function(id) {
      	alert("成功注销该商家");
      }
    },
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 large-up-4" id="admin-home">
  	<template v-for="item in bussiness | filterBy searchText in 'title' 'id'">
  	  <div class="column">
  	  	<div class="row admin-item" small-2>
  	  	  <div class="column">
  	  	  	<img :src="item.picture">
  	  	  	<label>投诉率
  	  	  	  <div class="progress progress-row alert" role="progressbar" tabindex="0" :aria-valuenow="item.count" aria-valuemin="0" :aria-valuetext="item.count + ' percent'" aria-valuemax="100">
  	  	  	  	<span class="progress-meter" :style="'width:' + item.count+'%'">
  	  	  	  	  <p class="progress-meter-text">{{item.count}}%</p>
  	  	  	  	</span>
  	  	  	  </div>
  	  	  	</label>
  	  	  </div>
  	  	  <div class="column">
  	  	  	<div class="row">
  	  	  	  {{item.title}}
  	  	  	</div>
  	  	  	<div class="row">
  	  	  	  <i class="fi-telephone"></i> {{item.number}}
  	  	  	</div>
  	  	  	<div class="row">
  	  	  	  <div class="button cancel-button" v-on:click="cancelBussiness(item.id)">注销该商家</div>
  	  	  	</div>
  	  	  </div>
  	  	</div>
  	  </div>
  	</template>
  </div>
</template>

<style lang="sass">
  // Import
  @import "../variables.scss";

  // Styles
  #admin-home {
  	border: 1px solid rgb(169, 169, 169);
  }
  .admin-item {
  	padding-top: 15px;
  	padding-bottom: 20px;
  	color: black;
  }
  .gold {
  	color: gold;
  }
  .gray {
  	color: $grey3;
  }
  .cancel-button {
  	border-radius: 3px;
  }
  .progress-row {
  	margin: 0;
  }
  label {
  	font-size: 12px;
  	color: $grey2;
  }
</style>
