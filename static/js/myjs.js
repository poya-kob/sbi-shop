function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');

function sendComment(sender, post_id, comment_id) {
    var ev = $(sender).closest(".comment-reply-wrap").find("textarea").val();

    if (ev !== "") {
        $.ajax({
            headers: {
                'X-CSRFToken': csrftoken
            },
            url: "/blog/comment/" + post_id + "/",
            method: "POST",
            data: {
                comment_id: comment_id,
                comment_text: ev,
                action: "reply"
            },
            success: function (data) {
                try {
                    data = jQuery.parseJSON(data);
                }catch(e) {}

                var comment = data[0];
                var user = data[1];


                var html = '<li><ul><li>' +
                    '<div className="comment_box">'+
                    '<div className="comment_image">'+
                    '<img src="/static/images/user.png" alt="image">'+
                    '</div><div className="comment_text"><div className="comment_header">'+
                    '<div className="comment_name">'+
                    '<h5>{name}</h5> <span>{date}</span></div></div><p>{comment}</p>'+
                    '</div></div></li></ul></li>';

                html = html.replace("{name}",user.fields.username);
                html = html.replace("{date}",comment.fields.created);
                html = html.replace("{comment}",comment.fields.body);

                $(sender).closest("ul").find("ul").append(html);
                $(".comment-reply-wrap").remove();
            },
            error: function () {
                alert("error");
            }
        });
    }
    return false;
}

$(document).ready(function () {
    $(".comment-reply").click(function () {
        var post_id = $(this).data("post-id");
        var comment_id = $(this).data("comment-id");
        var html = "<div class='comment-reply-wrap'>";
        html += "<textarea name='reply[" + comment_id + "]' class ='comment-reply-editor'></textarea> ";
        html += "<button type='button' onclick='return sendComment(this," + post_id + "," + comment_id + ")'>"
            + "ارسل</button<";
        html += "</div>";
        $(this).closest(".comment_box").find(".comment_text:first").after(html);
        return false;
    });
});