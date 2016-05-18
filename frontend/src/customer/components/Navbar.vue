<script>
  export default {
    name: "Navbar",
    props: ['searchText'],
    data: function() {
      return {
        username: 'lala',
        isLog: true
      }
    },
    methods: {
      resetLogout: function() {
        this.isLog = false;
      }
    }/*,
    ready: function() {
      $(document).foundation();
    }*/
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
        <li class="menu-text">Campus Food</li>
        <li><a v-link="{name: 'home'}">首页</a></li>
        <li><a v-link="{name: 'order'}">我的订单</a></li>
        <li><a v-link="{name: 'about'}">个人中心</a></li>
      </ul>
    </div>
    <div class="top-bar-right">
      <ul class="menu">
        <li><input type="search" placeholder="Search" v-model="searchText"></li>
        <li>
          <ul class="dropdown menu" data-dropdown-menu>
            <li>
              <template v-if="isLog">
                <i class="fi-torso"></i> {{username}}
              </template>
              <template v-else>
                <a v-link="{name: 'login'}"><i class="fi-torso"></i> 登录/注册</a>
              </template>
              <ul class="menu" v-if="isLog">
                <li><a v-link="{name: 'login'}" v-on:click="resetLogout">退出</a></li>
                <li><a v-link="{name: 'login'}" v-on:click="resetLogout">更换账户</a>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>