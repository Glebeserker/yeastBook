<template>
    <div class='company-view'>
        <div class = 'columns is-multiline'>
            <div class = 'column is-one-third' v-for='company in companies' v-bind:key='company.id'>
                <div class='box'>
                    <router-link v-bind:to='{path: "/companies"+ company.return_absolute_url}'><h3>{{ company.name }}</h3></router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CompaniesView',
    data() {
        return {
            companies: []
        }
    },
    props: {
        company: Object
    },
    components: {},
    mounted() {
        this.getCompany()
    },
    methods: {
        getCompany(){
            axios
            .get('http://127.0.0.1:8000/api/v1/companies')
            .then(response => {
                this.companies = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>