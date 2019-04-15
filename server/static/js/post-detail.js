$(document).ready(
    () => {
        $('#comment-form-displayer').click(
            () => {
                $('#comment-form-wrapper').show();
            }
        );
        $('#comment-form-hidder').click(
            () => {
                $('#comment-form-wrapper').hide();
            }
        );
        $('.reply-form-displayer').click(
            function() {
                let fullId = $(this).attr('id');
                let id = fullId.split('__')[1];
                let wrapperId = '#reply-form-wrapper__' + id;
                let editReplyFormId = '#edit-reply-form-wrapper__' + id;
                $(wrapperId).show();
                $(editReplyFormId).hide();
            }
        );
        $('.reply-form-hidder').click(
            function() {
                let fullId = $(this).attr('id');
                let id = fullId.split('__')[1];
                let wrapperId = '#reply-form-wrapper__' + id;
                $(wrapperId).hide();
            }
        );
        $('.edit-reply-form-displayer').click(
            function() {
                let fullId = $(this).attr('id');
                let id = fullId.split('__')[1];
                let wrapperId = '#edit-reply-form-wrapper__' + id;
                let replyFormId = '#reply-form-wrapper__' + id;
                $(wrapperId).show()
                $(replyFormId).hide()
            }
        );
        $('.edit-reply-form-hidder').click(
            function () {
                let fullId = $(this).attr('id');
                let id = fullId.split('__')[1];
                let wrapperId = '#edit-reply-form-wrapper__' + id;
                $(wrapperId).hide();
            }
        )
    }
)