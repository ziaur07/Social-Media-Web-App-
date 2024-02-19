document.getElementById('followButton').addEventListener('click', function() {
    if (this.value === 'Follow') {
        this.value = 'Unfollow';
    } else {
        this.value = 'Follow';
    }
});


document.querySelectorAll('.like-button').forEach(function(button){
    button.addEventListener('click', function() {
       var postId = this.datasset.postid;

    });
});

fetch ('/like_post',{
    method: 'POST',
    body: JSON.stringify({
        postId: postId
    })
}).then(function(response) {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error('Error: ' + response.statusText);
    }

}).then(function(data){

}).catch(function(error){
    console.log('Error: ', error);
});

document.querySelector('.post[data-post-id="' + postId + '"] .like-count').textContent = data.like_count;