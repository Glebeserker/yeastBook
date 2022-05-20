<template>
    <div class="types-detail">
        <section class='hero is-small mb-6'>
            <div class="hero-body has-text-centered">
                <p class='title mb-6'>{{ typeDetail.name }}</p>
            </div>
        </section>
        <div class="columns is-multiline is-centered">
            <YeastBox v-for="yeast in typeDetail.yeastss"
            v-bind:key="yeast.name"
            v-bind:yeast="yeast" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import YeastBox from '@/components/YeastBox'

export default {
    name: 'TypesDetail',
    components: {
        YeastBox
    },
    data() {
        return {
            typeDetail: {
                yeastss: []
            }
        }
    },
    mounted() {
        this.getTypeDetail()
    },
    methods: {
        getTypeDetail() {
            const typeSlug = this.$route.params.type_slug
            axios
            .get(`http://127.0.0.1:8000/api/v1/types/${typeSlug}`)
            .then( response => {
                this.typeDetail = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>