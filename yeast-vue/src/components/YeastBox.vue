<template>
    <div class="column is-one-third">
        <div class="box">
            <h3 class='subtitle'>{{ yeast.name }}</h3>
            <router-link v-bind:to='yeast.return_absolute_url' class="button is-dark mt-4">View Yeast</router-link>
        </div>
    </div>  
</template>

<script>
export default {
    name: 'YeastBox',
    props: {
        yeast: Object
    }
}
</script>