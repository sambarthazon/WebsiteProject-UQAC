function like(postId) {
    const likeCount = document.getElementById(`likes-count-${postId}`); // Counter of likes
    const likeButton = document.getElementById(`like-button-${postId}`); // Button of likes
  
    fetch(`/like-post/${postId}`, { method: "POST" }) // Actions on the post which have this post id
      .then((res) => res.json())
      .then((data) => {
        likeCount.innerHTML = data["likes"];
        if (data["liked"] === true) { // If post is liked
          likeButton.className = "fas fa-thumbs-up";
        } else { // If post wasn't liked
          likeButton.className = "far fa-thumbs-up";
        }
      })
      .catch((e) => alert("Could not like post."));
  }