// edit
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', (e) => {
            const postDiv = e.target.parentElement;
            postDiv.querySelector('.post-content').style.display = 'none';
            postDiv.querySelector('.edit-content').style.display = 'block';
            postDiv.querySelector('.edit-button').style.display = 'none';
            postDiv.querySelector('.save-button').style.display = 'block';
        });
    });

    document.querySelectorAll('.save-button').forEach(button => {
        button.addEventListener('click', (e) => {
            const postDiv = e.target.parentElement;
            const postId = postDiv.dataset.postId;
            const newContent = postDiv.querySelector('.edit-content').value;
            fetch('/edit_post', {
                method: 'POST',
                body: JSON.stringify({
                    post_id: postId,
                    content: newContent
                })
            })
            .then(response => response.json())
            .then(result => {
                postDiv.querySelector('.post-content').textContent = newContent;
                postDiv.querySelector('.post-content').style.display = 'block';
                postDiv.querySelector('.edit-content').style.display = 'none';
                postDiv.querySelector('.edit-button').style.display = 'block';
                postDiv.querySelector('.save-button').style.display = 'none';
            });
        });
    });
});




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
// follow unfollow
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
// likes
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
                document.querySelector('.like-count[data-post-id="' + postId + '"]').textContent = data.like_count;
                //document.querySelector('.like-count').textContent = data.like_count;
            }).catch(function(error) {
                console.log('Error: ', error);
            });
        });
    });
});