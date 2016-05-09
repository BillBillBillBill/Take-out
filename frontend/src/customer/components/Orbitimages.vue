<script>
  export default {
  	name: "Orbitimages",
    props: ['bussinessDetail']
  }
</script>

<template>
<div class="orbit" role="region" aria-label="The special foods!" data-orbit>
  <ul class="orbit-container">
    <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
    <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
    <li class="is-active orbit-slide">
      <img class="orbit-image" src="../images/pic1.jpg" alt="Food">
     <!-- <figcaption class="orbit-caption1">The first food.</figcaption>-->
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic2.jpg" alt="Food">
     <!-- <figcaption class="orbit-caption1">The second food.</figcaption>-->
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic3.jpg" alt="Food">
     <!-- <figcaption class="orbit-caption1">The third food.</figcaption>-->
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic4.jpg" alt="Food">
      <!--<figcaption class="orbit-caption1">The fouth food.</figcaption>-->
    </li>
    <figcaption class="orbit-caption1" data-open="showBussinessInfo">
      <div>{{bussinessDetail.title}}</div>
      <div>
        <i v-for="n in bussinessDetail.star" class="fi-star yellow"></i><i v-for="n in (5-bussinessDetail.star)" class="fi-star gray"></i>
      </div>
      <div>月销售量{{bussinessDetail.count}}单</div>
      <div><i class="fi-telephone"></i>{{bussinessDetail.number}}</div>
      <div><i class="fi-marker"></i> {{bussinessDetail.address}}</div>
    </figcaption>
    <div class="reveal" id="showBussinessInfo" data-reveal>
      <div class="row small-up-2">
        <div class="column">
          <img class="thumbnail" :src="bussinessDetail.picture">
        </div>
        <div class="column align-middle">
          <h4>{{bussinessDetail.title}}</h4>
          <div>
            <i v-for="n in bussinessDetail.star" class="fi-class yellow"></i><i v-for="n in (5-bussinessDetail.star)" class="fi-star gray"></i>
          </div>
          <div>月销售量{{bussinessDetail.count}}单</div>
          <div><i class="fi-telephone"></i> {{bussinessDetail.number}}</div>
          <div><i class="fi-marker"></i> {{bussinessDetail.address}}</div>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <ul class="show_comments accordion" data-accordion data-multi-expand="true">
            <li v-for="comment in bussinessDetail.comments" v-bind:class="[$index==0 ? 'is-active':'']" class="accordion-item" data-accordion-item>
              <a class="accordion-title">
                <span>{{comment.user}}</span>
                <i v-for="n in comment.star" class="fi-star yellow"></i><i v-for="n in (5-comment.star)" class="fi-star gray"></i>
                <span>{{comment.date}}</span>
              </a>
              <div class="description accordion-content" data-tab-content>{{comment.description}}</div>
            </li>
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