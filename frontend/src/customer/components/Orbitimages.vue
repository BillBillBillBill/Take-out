<script>
  export default {
  	name: "Orbitimages"
  }
</script>

<template>
<div class="orbit" role="region" aria-label="The special foods!" data-orbit>
  <ul class="orbit-container">
    <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
    <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
    <li class="is-active orbit-slide">
      <img class="orbit-image" src="../images/pic1.jpg" alt="Food">
      <figcaption class="orbit-caption">The first food.</figcaption>
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic2.jpg" alt="Food">
      <figcaption class="orbit-caption">The second food.</figcaption>
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic3.jpg" alt="Food">
      <figcaption class="orbit-caption">The third food.</figcaption>
    </li>
    <li class="orbit-slide">
      <img class="orbit-image" src="../images/pic4.jpg" alt="Food">
      <figcaption class="orbit-caption">The fouth food.</figcaption>
    </li>
  </ul>
  <nav class="orbit-bullets">
    <button class="is-active" data-slide="0"><span class="show-for-sr">First slide details.</span><span class="show-for-sr">Current Slide</span></button>
    <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
    <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
    <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
  </nav>
</div>
</template>