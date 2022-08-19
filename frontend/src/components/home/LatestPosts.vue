<template>
<div>
    <div class="" v-if="latest_posts">
        <div class="mx-5 text-start" v-for="post in latest_posts" :key="post.id">
            <router-link class="h4" :to="`/post/${post.meta.slug}`">{{post.title}}</router-link>
            <span class="ms-3 text-warning fw-bold">{{timeSince(post.meta.first_published_at)}}</span><br>
            <p class="lead">{{post.intro}}<router-link :to="`/post/${post.meta.slug}`">more</router-link>
            </p>
        </div>
    </div>
    <div v-else>
        <p class="lead">Service Unavailable.</p>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import utils from '../../utils'
export default{
    name: 'Latest Posts',
    data() {
        return {
            latest_posts: null
        }
    },
    mounted() {
        this.get_latest_posts()
    },
    methods: {
        timeSince: utils.timeSince,
        get_latest_posts(){
            axios
            .get('/api/v2/pages?type=blog.BlogPage&fields=intro&order=-first_published_at')
            .then(response => {
                let posts = response.data.items
                this.latest_posts = posts.length > 5 ? posts.slice(0,6) : posts
            })
            .catch(error => {
                console.log(error)
            })

        },
    }
}
</script>