<template>
    <div class="yeast-company">
        <div class='box'>
            <div class="columns is-multiline">
                <div class="column is-full"><h1 class='title'>{{ yeast.name }}</h1></div>
                <div class='column is-three-quarters'>
                    <h2>General Info: \n</h2>
                    <h3>{{ yeast.gen_info }}</h3>
                    <h2>More Detail:</h2>
                    <h3>{{ yeast.sec_info }}</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'YeastCompany',
    data() {
        return {
            yeast: []
        }
    },
    mounted() {
        this.getYeastCompany()
    },
    methods: {
        getYeastCompany(){
            const yeastSlug = this.$route.params.yeast_slug
            const companySlug = this.$route.params.company_slug
            axios
            .get(`http://127.0.0.1:8000/companies/${companySlug}/${yeastSlug}/`)
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