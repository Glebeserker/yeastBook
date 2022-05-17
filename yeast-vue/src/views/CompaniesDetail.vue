<template>
    <div class='companies-detail'>
        <section class="hero is-small mb-6">
            <div class="hero-body has-text-centered">
                <p class="title mb-6">{{ companyDetail.name }}</p>
            </div>
        </section>
        <div class="columns is-multiline">
            <YeastBox v-for="yeast in companyDetail.yeasts"
            v-bind:key="yeast.id"
            v-bind:yeast="yeast" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import YeastBox from '@/components/YeastBox'

export default {
    name: 'CompaniesDetail',
    components: {
        YeastBox
    },
    data() {
        return {
            companyDetail: {
                yeasts: []
            }
        }
    },
    mounted() {
        this.getCompanyDetails()
    },
    methods: {
        getCompanyDetails(){
            const companySlug = this.$route.params.company_slug
            axios
            .get(`http://127.0.0.1:8000/api/v1/companies/${companySlug}`)
            .then(response => {
                this.companyDetail = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }    
}
</script>