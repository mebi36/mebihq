<template>
    <div class="progress sticky-top" style="height: 0.2rem;" :style="{'width': percentage + '%'}">
        <div class="progress-bar progress-bar-animated bg-primary" style="width: 50%;" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</template>
<script>
export default {
    name: 'ProgressBar',
    data() {
        return {
            percentage: 0
        }
    },
    created() {
        var intval = setInterval(() => {
            if(this.percentage < 80){
                this.percentage += .1;
            }
            else{
                clearInterval(intval);
            }
        })
    }
}
</script>