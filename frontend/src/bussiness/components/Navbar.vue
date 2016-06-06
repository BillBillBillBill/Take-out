<script>
  export default {
    name: "Navbar",
    props: ['searchText', 'bussinessInfo', 'isLog'],
    data: function() {
      return {
        username: localStorage.bussiness_nickname
      }
    },
    methods: {
      resetLogout: function() {
        localStorage.bussiness_token = "";
        localStorage.bussiness_nickname = "";
        localStorage.bussiness_id = "";
        this.isLog = false;
        this.username = "";
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        if (!localStorage.bussiness_token) {
          that.username = "";
          that.isLog = false;
          window.location.href = "#!/login";
        } else {
          that.isLog = true;
          that.username = localStorage.bussiness_nickname;
          $.ajax({
            url: "../api/seller/" + localStorage.bussiness_id,
            async: false,
            type: "GET",
            error: function(xhr, status) {
              alert(JSON.parse(xhr.responseText).message);
            },
            success: function(data) {
              that.bussinessInfo = data.data.seller;
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
          <li class="menu-text">商家版</li>
          <li><a v-link="{name: 'home'}">首页</a></li>
          <li><a v-link="{name: 'order'}">所有订单</a></li>
          <li><a v-link="{name: 'about'}">个人中心</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search" v-model="searchText"></li>
          <li>
            <template v-if="isLog">
              <ul class="dropdown menu" data-dropdown-menu>
                <li>
                  <i class="fi-torso"></i> {{bussinessInfo.nickname}}
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
