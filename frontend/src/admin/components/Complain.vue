<script>
  //import QuoteService from '../services/quote'

  export default {
    name: "Complain",
    props: ['searchText'],

    data: function(){
      return {
        complains: [
        {id: '1',
        userid: 'user1',
        username: 'mame1',
        bussinessid: 'bussiness3',
        bussiness_name: '三饭',
        date: '2015/03/16',
        reason: 'XXXXXXXX'
        },
        {id: '2',
        userid: 'user3',
        username: 'mede3',
        bussinessid: 'bussiness5',
        bussiness_name: '五饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        {id: '3',
        userid: 'user6',
        username: 'mema6',
        bussinessid: 'bussiness9',
        bussiness_name: '九饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        {id: '4',
        userid: 'user2',
        username: 'meme2',
        bussinessid: 'bussiness3',
        bussiness_name: '三饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        {id: '5',
        userid: 'user1',
        username: 'mete1',
        bussinessid: 'bussiness3',
        bussiness_name: '三饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        {id: '6',
        userid: 'user6',
        username: 'meme6',
        bussinessid: 'bussiness8',
        bussiness_name: '八饭',
        date: '2014/03/16',
        reason: 'XXXXXX'
        },
        {id: '7',
        userid: 'user4',
        username: 'meme4',
        bussinessid: 'bussiness6',
        bussiness_name: '六饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        {id: '8',
        userid: 'user7',
        username: 'meme7',
        bussinessid: 'bussiness2',
        bussiness_name: '二饭',
        date: '2015/03/16',
        reason: 'XXXXXX'
        },
        ]
      }
    },
    methods: {
      passCheck: function(id) {
        alert(id + " is Passed");
      },
      failCheck: function(id) {
        alert(id + " is Failed");
      }
    },
    ready: function() {
      $(document).foundation();
    }

    /*ready: function() {
      QuoteService.getQuote(this).then(function(response){
        this.$set('quote', response.data[0].content);
      }, function(response){
        console.log(response);
      });
    }*/
  }
</script>

<template>
  <div class="row small-up-1 medium-up-2 large-up-3 complain-page">
    <template v-for="item in complains | filterBy searchText in 'username' 'bussiness_name' 'date'">
      <div class="column">
        <div class="callout small">
          <div class="row">
            <div class="column small-7">
              <div class="row"><div class="column">被投诉商家：{{item.bussiness_name}}</div></div>
              <div class="row"><div class="column">投诉顾客：{{item.username}}</div></div>
              <div class="row"><div class="column">投诉日期：{{item.date}}</div></div>
              <div class="row"><div class="column">投诉原因：{{item.reason}}</div></div>
            </div>
            <div class="column">
              <div class="row">
                <div class="column shrink check-btn">
                  <div class="button border-btn" v-on:click="passCheck(item.id)">审核通过</div>
                </div>
              </div>
              <div class="row">
                <div class="column shrink check-btn">
                  <div class="button border-btn" v-on:click="failCheck(item.id)">审核失败</div>
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
