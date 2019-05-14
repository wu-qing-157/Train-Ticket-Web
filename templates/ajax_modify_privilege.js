{% if fail %}
    show_dialog('Oops...', '授予管理员权限失败', '╮(╯-╰)╭', '');
    document.getElementById('grant-button').disabled = false;
{% else %}
    $.getScript("/ajax_query_profile?user_id={{ user_id }}");
    show_dialog('( •̀ ω •́ )y', '授予用户 {{ user_id }} 管理员权限成功', 'b（￣▽￣）d', '');
{% endif %}