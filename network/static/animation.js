
document.addEventListener('DOMContentLoaded', function() {
    var csrftoken = getCookie('csrftoken');

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var followButton = document.getElementById('followButton');
    if (followButton) {
        followButton.addEventListener('click', function() {
            if (this.value === 'Follow') {
                this.value = 'Unfollow';
            } else {
                this.value = 'Follow';
            }
        });
    }

    document.querySelectorAll('.like-button').forEach(function(button) {
        button.addEventListener('click', function() {
            var postId = this.dataset.postId;

            fetch('/like_post', {
                method: 'POST',
                body: JSON.stringify({
                    post_id: postId
                }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                }
            }).then(function(response) {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error: ' + response.statusText);
                }
            }).then(function(data) {
                document.querySelector('.like-count').textContent = data.like_count;
            }).catch(function(error) {
                console.log('Error: ', error);
            });
        });
    });
});