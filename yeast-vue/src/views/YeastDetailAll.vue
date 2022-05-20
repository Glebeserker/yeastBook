<template>
    <div class='yeast-detail-wrapper'>
        <section class="hero mb-6">
            <div class='hero-body has-text-centered'>
                <p class='title mb-6'>
                    {{ yeast.name }}
                </p>
            </div>
        </section>

        <div class = 'columns is-multiline'>
            <div class = 'column is-one-third'>
                <div class='box has-text-centered'>
                    <h2 class='subtitle'>General Information:</h2>
                    <p>{{ yeast.gen_info }}</p>
                </div>
            </div>
            <div class='column is-two-thirds'></div>
            <div class='column is-full'>
                <div class='box has-text-centered'>
                    <h3 class='subtitle'>Secondary Information:</h3>
                    <p>{{ yeast.sec_info }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'YeastCompDetail',
    data() {
        return {
            yeast: {}
        }
    },
    mounted() {
        this.getYeast()
    },
    methods: {
        getYeast() {
            const firstSlug = this.$route.params.slug
            axios
            .get(`http://127.0.0.1:8000/api/v1/${firstSlug}/`)
            .then(response => {
                this.yeast = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }   
}
</script>