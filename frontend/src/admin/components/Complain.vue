<script>
  //import QuoteService from '../services/quote'

  export default {
    name: "Complain",
    props: ['searchText'],

    data: function(){
      return {
        complaint_list: []
      }
    },
    methods: {
      handle_complaint: function(complaint_id, status) {
        var that = this;
        $.ajax({
          url: "../api/complaint/" + complaint_id,
          async: false,
          type: "PUT",
          headers: {'Authorization-Token': localStorage.admin_token},
          contentType: "application/json;charset=utf-8",
          processData: false,
          data: JSON.stringify({status: status}),
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            for (var i = 0; i < that.complaint_list.length; i++) {
              if (that.complaint_list[i].id == complaint_id) {
                if (status == 'I') that.complaint_list[i].status = "Ignored";
                else that.complaint_list[i].status = "Resolved";
                break;
              }
            }
          }
        });
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/complaint",
          async: false,
          type: "GET",
          headers: {'Authorization-Token': localStorage.admin_token},
          dataType: "json",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            console.log("success");
            var list = data.data.complaint_list;
            if (that.complaint_list.length == 0) {
              for (var i = 0; i < list.length; i++) {
                var info = {
                  id: list[i].id,
                  status: list[i].status,
                  customer: list[i].customer,
                  content: list[i].content,
                  store: list[i].store
                }
                var newDate = new Date();
                newDate.setTime(parseInt(list[i].created_time)*1000);
                info.created_time = newDate.toLocaleString();
                that.complaint_list.push(info);
              }
            }
          }
        });
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
  <div class="row small-up-1 medium-up-2 large-up-3 complain-page">
    <template v-for="item in complaint_list | filterBy searchText in 'customer' 'content' 'created_time'">
      <div class="column">
        <div class="callout small">
          <div class="row">
            <div class="column small-7">
              <div class="row"><div class="column">被投诉商家：{{item.store}}</div></div>
              <div class="row"><div class="column">投诉顾客：{{item.customer}}</div></div>
              <div class="row"><div class="column">投诉日期：{{item.created_time}}</div></div>
              <div class="row"><div class="column">投诉原因：{{item.content}}</div></div>
            </div>
            <div class="column" v-if="item.status == 'Processing'">
              <div class="row">
                <div class="column shrink check-btn">
                  <div class="button border-btn" v-on:click="handle_complaint(item.id, 'R')">审核通过</div>
                </div>
              </div>
              <div class="row">
                <div class="column shrink check-btn">
                  <div class="button border-btn" v-on:click="handle_complaint(item.id, 'I')">审核失败</div>
                </div>
              </div>
            </div>
            <div class="column" v-else>
              <div class="row">
                <div class="column shrink check-btn">
                  <div class="button border-btn">已处理</div>
                </div>
              </div>
            </div>
          </div>
        </div> 
      </div>
    </template>
  </div>
</template>

<style lang="sass">
  // Imports
  @import "../variables.scss";

  // Styles
  .complain-page {
    margin: 20px;
  }
  .check-btn {
    text-align: right;
  }
  .border-btn {
    border-radius: 15px;
  }

</style>
