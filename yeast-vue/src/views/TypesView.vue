<template>
    <div class='types-view'>
        <div class = 'columns is-multiline'>
            <div class = 'column is-one-third' v-for='yeast_type in yeast_types' v-bind:key='yeast_type.id'>
                <div class='box'>
                    <router-link v-bind:to='{path: "/types" + yeast_type.return_absolute_url}'><h3>{{ yeast_type.name }}</h3></router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'TypesView',
    data() {
        return {
            yeast_types: []
        }
    },
    props: {
        yeast_type: Object
    },
    components: {},
    mounted() {
        this.getType()
    },
    methods: {
        getType() {
            axios
            .get('http://127.0.0.1:8000/api/v1/types')
            .then(response => {
                this.yeast_types = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>