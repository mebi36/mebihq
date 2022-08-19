import { createWebHistory, createRouter } from "vue-router"

import PostItem from "@/views/PostItem.vue"
import PostListing from "@/views/PostListing.vue"
import Home from "@/views/Home.vue"
import NProgress from "nprogress"
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
        path: "/post/:slug",
        name: "PostItem",
        component: PostItem,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeResolve((to) => {
    if(to.name){
        NProgress.start()
    }
    return true
})
router.afterEach(() => {
    NProgress.done()
})

export default router