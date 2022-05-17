<template>
  <div id="wrapper">
    <div class = 'column is-full has-text-centered'>
        <figure class = 'image is-inline-block'>
            <router-link to='/'><h1>YeastBook</h1></router-link>
            <img src="@/assets/Yeast-Header.jpg" alt="Header-Image">
        </figure>
    </div>
    <section class='section'>
        <router-view/>
    </section>
  </div>
</template>

<style lang='scss'>
@import '../node_modules/bulma';


</style>
