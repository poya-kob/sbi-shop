function sendComment(sender,post_id,comment_id){
    var ev = $(sender).closest(".comment-reply-wrap").find("textarea").val();

    if(ev !==""){
        $.ajax({
            url:"blog/comment/"+post_id+"/",
            method:"POST",
            data : {
                comment_id:comment_id,
                comment_text : ev,
                action:"reply"
            },
            success : function(data) {
                conseol.log(data);
            },
            error:function() {
                alert("error");
            }
        });
    }
    return false;
}

$(document).ready(function (){
    $(".comment-reply").click(function (){
        var post_id = $(this).data("post-id");
        var comment_id = $(this).data("comment-id");
        var html = "<div class='comment-reply-wrap'>";
        html +="<textarea name='reply["+comment_id+"]' class ='comment-reply-editor'></textarea> ";
        html += "<button type='button' onclick='return sendComment(this,"+post_id+","+comment_id+")'>"
            +"ارسل</button<";
        html += "</div>";
        $(this).closest(".comment_box").find(".comment_text:first").after(html);
        return false;
    });
});