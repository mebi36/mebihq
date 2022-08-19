<template>
    <div class="vw-100">
        <div class="row pt-5">
            <div class="col">
                <img src="../assets/building.svg" alt="" class="img-fluid">
            </div>
            <div class="col align-self-center">
                <div>
                    <h1 class="fw-bold">Welcome to MebiHQ</h1>
                    <p class="h4">Trove of exciting knowledge gathered from varied aspects of learning and life.</p>
                </div>
            </div>
        </div>
        <div class="row bg-secondary bg-opacity-10 mt-5">
            <div class="container">
                <div class="p-2">
                    <h2>Latest Posts</h2>
                    <div><LatestPosts /></div>
                </div>
                
            </div>
        </div>
    </div>
</template>
<script>
import LatestPosts from '../components/home/LatestPosts.vue'

export default {
    components: {LatestPosts}
}
</script>
<style>
</style>