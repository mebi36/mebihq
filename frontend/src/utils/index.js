const utils = {
    timeSince(datetimeString){
        var today = new Date()
        const date = new Date(datetimeString)
        var dateDiff = today - date
        console.log(dateDiff)
        var years = parseInt(dateDiff / (365 * 24 * 60 * 60 * 1000))
        var months = parseInt(dateDiff / (30 * 24 * 60 * 60 * 1000))
        var days = parseInt(dateDiff / (24 * 60 * 60 * 1000))
        var hours = parseInt(dateDiff / (60 * 60 * 1000))
        var minutes = parseInt(dateDiff / (60 * 1000))

        if(years >= 1){
            if (years == 1){
                return '1 year ago'
            }
            return ''+years+' years ago'
        }else if(months >= 1){
            if(months == 1){
                return '1 month ago'
            }
            return ''+months+' months ago'
        }else if(days >= 1){
            if(days == 1){
                return '1 day ago'
            }
            return '' + days + ' days ago'
        }else if(hours >= 1){
            if(hours == 1){
                return '1 hour ago'
            }
            return '' + hours + ' hours ago'
        }else if(minutes >= 1){
            if(minutes == 1){
                return 'a few moments ago'
            }
            return '' + minutes + ' minutes ago'
        }
    }
}

export default utils