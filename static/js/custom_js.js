
function showCommentForm() {
    var x = document.getElementById("replyComment");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function set_comment_parent_id(comment_id) {
  var element = document.getElementById('comment_parent_id')
  element.value = comment_id;
}

$(document).ready(function() {
    $('.hover').on('touchstart touchend', function(e) {
        e.preventDefault();
        $(this).toggleClass('hover_effect');
    });
});
