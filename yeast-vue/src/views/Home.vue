<template>
  <div class="home">
    <div class='column is-fourth-fifths is-offset-one-fifth'>
        <router-link to='/all-products'><h3>ALL PRODUCTS</h3></router-link>
    </div>
    <div class='columns'>
        <div class="column is-half">
            <router-link to='/styles'>LOOK BY STYLE</router-link>
        </div>
        <div class='column is-half'>
            <router-link to='/companies'>LOOK BY COMPANY</router-link>
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
