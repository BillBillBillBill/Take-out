<script>
  export default {
    name: "Navbar",
    props: ['searchText', 'adminInfo', 'isLog'],
    data: function() {
      return {
        username: localStorage.admin_nickname
      }
    },
    methods: {
      resetLogout: function() {
        localStorage.admin_token = "";
        localStorage.admin_nickname = "";
        localStorage.admin_id = "";
        this.isLog = false;
        this.username = "";
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        if (!localStorage.admin_token) {
          that.username = "";
          that.isLog = false;
          window.location.href = "#!/login";
        } else {
          that.isLog = true;
          that.username = localStorage.admin_nickname;
          $.ajax({
            url: "../api/admin/" + localStorage.admin_id,
            async: false,
            type: "GET",
            error: function(message) {
              alert("Error: " + message);
            },
            success: function(data) {
              that.adminInfo = data.data.admin;
            }
          });
        }
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
        <li><a v-link="{name: 'add'}">添加商家</a></li>
      </ul>
    </div>
    <div class="top-bar-right">
      <ul class="menu">
        <li><input type="search" placeholder="Search" v-model="searchText"></li>
        <li>
          <template v-if="isLog">
            <ul class="dropdown menu" data-dropdown-menu>
              <li>
                <i class="fi-torso"></i> {{adminInfo.nickname}}
                <ul class="menu">
                  <li><a v-link="{name: 'login'}" v-on:click="resetLogout">退出</a></li>
                  <li><a v-link="{name: 'login'}" v-on:click="resetLogout">更换账户</a></li>
                </ul>
              </li>
            </ul>
          </template>
          <template v-else>
            <ul class="menu">
              <li>
                <a v-link="{name: 'login'}"><i class="fi-torso"></i> 登录/注册</a>
              </li>
            </ul>
          </template>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>
