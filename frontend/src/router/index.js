import { createWebHistory, createRouter } from "vue-router"

import PostItem from "@/views/PostItem.vue"
import PostListing from "@/views/PostListing.vue"
import Home from "@/views/Home.vue"

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/posts",
        name: "PostListing",
        component: PostListing,
    },
    {
        path: "/post/:id/:slug",
        name: "PostItem",
        component: PostItem,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router