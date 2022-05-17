<template>
    <div class='all-products'>
        <section class="hero is-small mb-6">
            <div class="hero-body has-text-centered">
                <p class="title mb-6">All Products</p>
            </div>
        </section>
        <div class='columns is-multiline'>
            <YeastBox v-for='yeast in AllProducts'
            v-bind:key = 'yeast.id'
            v-bind:yeast = 'yeast' />
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import YeastBox from '@/components/YeastBox'
export default {
    name: 'All-Products',
    components: {
        YeastBox
    },
    data() {
        return {
            AllProducts: []
        }
    },
    mounted() {
        this.getAllProducts()
    },
    methods: {
        getAllProducts() {
            axios
            .get('http://127.0.0.1:8000/api/v1/all-yeast')
            .then(response => {
                this.AllProducts = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>