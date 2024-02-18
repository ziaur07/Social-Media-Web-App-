document.getElementById('followButton').addEventListener('click', function() {
    if (this.value === 'Follow') {
        this.value = 'Unfollow';
    } else {
        this.value = 'Follow';
    }
});