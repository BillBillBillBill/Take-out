<script>
  export default {
  	name: "Orbitimages",
    props: ['currentid'],
    data: function() {
      return {
        store_info: {},
        review_list: []
      }
    },
    ready: function() {
      var that = this;
      function reloadPage() {
        $(document).foundation();
        $.ajax({
          url: "../api/store/" + that.currentid,
          async: false,
          type: "GET",
          error: function(xhr, status) {
            alert("Error: " + status);
          },
          success: function(data) {
            var list = data.data.store;
            console.log(list);
            var info = {
              store_id: list.id,
              store_name: list.name,
              store_phone: list.phone,
              store_address: list.address,
              total_orders_number: list.total_orders_num,
              average_star: list.average_star,
              complaint_rate: list.complaint_rate
            };
            if (list.images[0]) info.bussiness_image = "../api/" + list.images[0].path;
            that.store_info = info;

            if (that.review_list.length == 0) {
              var list_ = data.data.store.order_review_list;
              for (var i = 0; i < list_.length; i++) {
                var newDate = new Date();
                newDate.setTime(parseInt(list_[i].created_time)*1000);
                var time = newDate.toLocaleString();
                var info_ = {
                  customer: list_[i].customer,
                  star: list_[i].star,
                  created_time: time,
                  content: list_[i].content,
                };
                that.review_list.push(info_);
              }
            }
          }
        });
      }
      reloadPage();
      $(window).load(function() {
        reloadPage();
        new Foundation.Accordion($(".accordion"), {});
      });
      $(window).unload(function() {
        reloadPage();
        new Foundation.Accordion($(".accordion"), {});
      });
    }
  }
</script>

<template>
<div class="orbit" role="region" aria-label="The special foods!" data-orbit>
  <ul class="orbit-container">
    <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
    <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
    <li class="is-active orbit-slide">
      <img class="orbit-image" src="../images/pic1.jpg" alt="Food">
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic2.jpg" alt="Food">
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic3.jpg" alt="Food">
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic4.jpg" alt="Food">
    </li>
    <figcaption class="orbit-caption1" data-open="showBussinessInfo">
      <div>{{store_info.store_name}}</div>
      <div>
        <i v-for="n in store_info.average_star" class="fi-star gold"></i><i v-for="n in (5-store_info.average_star)" class="fi-star gray"></i>
      </div>
      <div>投诉率：{{store_info.complaint_rate * 100}}%</div>
      <div>月销售量{{store_info.total_orders_number}}单</div>
      <div><i class="fi-telephone"></i>{{store_info.store_phone}}</div>
      <div><i class="fi-marker"></i> {{store_info.store_address}}</div>
    </figcaption>
    <div class="reveal" id="showBussinessInfo" data-reveal>
      <div class="row small-up-2">
        <div class="column">
          <img class="thumbnail" :src="store_info.bussiness_image">
        </div>
        <div class="column align-middle">
          <h4>{{store_info.store_name}}</h4>
          <div>
            <i v-for="n in store_info.average_star" class="fi-star gold"></i><i v-for="n in (5-store_info.average_star)" class="fi-star gray"></i>
          </div>
          <div>投诉率：{{store_info.complaint_rate * 100}}%</div>
          <div>月销售量{{store_info.total_orders_number}}单</div>
          <div><i class="fi-telephone"></i> {{store_info.store_phone}}</div>
          <div><i class="fi-marker"></i> {{store_info.store_address}}</div>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <ul class="show_comments accordion" data-accordion data-multi-expand="true">
            <template v-for="comment in review_list">
              <li class="accordion-item is-active" data-accordion-item>
                <a class="accordion-title">
                  <span>{{comment.customer}}</span>
                  <i v-for="n in comment.star" class="fi-star gold"></i><i v-for="n in (5 - comment.star)" class="fi-star gray"></i>
                  <span>{{comment.created_time}}</span>
                </a>
                <div class="accordion-content" data-tab-content>
                  <div>{{comment.content}}</div>
                </div>
              </li>
            </template>
          </ul>
        </div>
      </div>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  </ul>
  <nav class="orbit-bullets">
    <button class="is-active" data-slide="0"><span class="show-for-sr">First slide details.</span><span class="show-for-sr">Current Slide</span></button>
    <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
    <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
    <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
  </nav>
</div>
</template>

<style lang="sass">
  // Import
  @import "../variables.scss";

  // Style
  * {
    box-sizing:border-box;
    -moz-box-sizing:border-box; /* Firefox */
    -webkit-box-sizing:border-box; /* Safari */
  }

  .orbit-container {
    height: 200px;
  }

  .orbit-caption1 {
    position: absolute;
    bottom: 4%;
    left: 40px;
    padding: 1rem;
    color: #fefefe;
    background-color: rgba(10, 10, 10, 0.5);
  }

  figcaption {
    cursor: hand;
    cursor: pointer;
  }

</style>