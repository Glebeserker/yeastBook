<template>
  <div class="home">
    <div class='column is-full '>
      <div class='box has-text-centered'>
        <router-link to='/all-products'><h3 class='subtitle'>ALL PRODUCTS</h3></router-link>
      </div>
    </div>
    <div class='columns'>
        <div class="column ">
          <div class='box has-text-centered'>
            <router-link to='/styles'>LOOK BY STYLE</router-link>
          </div>
        </div>
        <div class='column '>
          <div class='box has-text-centered'>
            <router-link to='/companies'>LOOK BY COMPANY</router-link>
          </div>
        </div>
    </div>
    
  </div>
</template>


<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  }
}
</script>
