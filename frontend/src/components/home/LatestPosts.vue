<template>
<div>
    <h2><span class="text-warning me-3"><BIconJournalCode /></span>Latest Posts</h2>
    <LoadingAnimation  :visible="loading_api" />
    <div class="" v-if="latest_posts && !(loading_api)">
        <div class="mx-5 text-start" v-for="post in latest_posts" :key="post.id">
            <router-link class="h4" :to="`/post/${post.meta.slug}`">{{post.title}}</router-link>
            <span class="ms-2 text-muted"><BIconClock /></span>
            <span class="ms-1 text-warning fw-bold">{{timeSince(post.meta.first_published_at)}}</span><br>
            <p class="lead">{{post.intro}}<router-link class="ms-1" :to="`/post/${post.meta.slug}`">more</router-link>
            </p>
        </div>
    </div>
    <div v-if="!(latest_posts)">
        <p class="lead">Service Unavailable.</p>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import utils from '../../utils'
import { BIconJournalCode, BIconClock } from 'bootstrap-icons-vue'
import LoadingAnimation from '../LoadingAnimation.vue'

export default{
    name: 'Latest Posts',
    components: { BIconJournalCode, BIconClock, LoadingAnimation },
    data() {
        return {
            latest_posts: null,
            loading_api: false
        }
    },
    mounted() {
        this.get_latest_posts()
    },
    methods: {
        timeSince: utils.timeSince,
        get_latest_posts(){
            this.loading_api = true
            axios
            .get('/api/v2/pages?type=blog.BlogPage&fields=intro&order=-first_published_at')
            .then(response => {
                let posts = response.data.items
                this.latest_posts = posts.length > 5 ? posts.slice(0,6) : posts
            })
            .catch(error => {
                console.log(error)

            })
            this.loading_api = false
        },
    }
}
</script>