window.target = '{{ user_id }}';
input_text_field.disabled = false;
{% if not_exist %}
document.getElementById('id-info').innerText = '{{ user_id }}（用户不存在）';
document.getElementById('name-info').innerHTML = '<i class="material-icons">clear</i>';
document.getElementById('email-info').innerHTML = '<i class="material-icons">clear</i>';
document.getElementById('phone-info').innerHTML = '<i class="material-icons">clear</i>';
document.getElementById('administrator-info').innerHTML = '<i class="material-icons">clear</i>';
document.getElementById('modify-status').innerText = '查询的用户不存在';
document.getElementById('grant-status').innerText = '查询的用户不存在';
document.getElementById('buy-ticket-status').innerText = '查询的用户不存在';
name_text_field.disabled = true;
email_text_field.disabled = true;
phone_text_field.disabled = true;
new_password_text_field.disabled = true;
document.getElementById('modify-button').disabled = true;
id_text_field.value = '{{ user_id }}'
name_text_field.value = '';
email_text_field.value = '';
phone_text_field.value = '';
new_password_text_field.value = '';
document.getElementById('name').oninput(null);
document.getElementById('email').oninput(null);
document.getElementById('phone').oninput(null);
document.getElementById('new_password').oninput(null);
document.getElementById('grant-button').disabled = true;
document.getElementById('buy-ticket-button').disabled = true;
document.getElementById('ticket-hint').innerText = '';
document.getElementById('ticket-table').innerHTML = '';
{% else %}
document.getElementById('id-info').innerText = '{{ user_id }}';
document.getElementById('name-info').innerText = '{{ name }}';
document.getElementById('email-info').innerText = '{{ email }}';
document.getElementById('phone-info').innerText = '{{ phone }}';
document.getElementById('administrator-info').innerText = '{% if administrator %} 管理员 {% else %} 普通用户 {% endif %}';
document.getElementById('modify-status').innerText = '将修改用户 {{ user_id }} 的用户信息';
document.getElementById('buy-ticket-status').innerText = '将为用户 {{ user_id }} 添加车票';
document.getElementById('grant-status').innerText = '{% if administrator %}用户 {{ user_id }} 已经是管理员{% else %}将授予用户 {{ user_id }} 管理员权限{% endif %}';
name_text_field.disabled = false;
email_text_field.disabled = false;
phone_text_field.disabled = false;
new_password_text_field.disabled = false;
document.getElementById('modify-button').disabled = false;
id_text_field.value = '{{ user_id }}';
name_text_field.value = '{{ name }}';
email_text_field.value = '{{ email }}';
phone_text_field.value = '{{ phone }}';
new_password_text_field.value = '';
document.getElementById('name').oninput(null);
document.getElementById('email').oninput(null);
document.getElementById('phone').oninput(null);
{% if administrator %}
document.getElementById('grant-button').disabled = true;
{% else %}
document.getElementById('grant-button').disabled = false;
{% endif %}
document.getElementById('buy-ticket-button').disabled = false;
{% if empty %}
document.getElementById('ticket-hint').innerText = '用户 {{ user_id }} 没有已订购的车票';
document.getElementById('ticket-table').innerHTML = ''
{% else %}
document.getElementById('ticket-hint').innerText = '以下为用户 {{ user_id }} 订购的车票';
window.new_row = function (i, train_id, name, from0, from1, from2, to0, to1, to2, kind, num) {
    const ret = document.createElement('tr');
    ret.innerHTML =
        '<td>\n' +
        '    <span class="mdc-typography--body1">' + from0 + '</span>\n' +
        '    <br>\n' +
        '    <span class="mdc-typography--body1">' + from1 + '' + from2 + '</span>\n' +
        '</td>\n' +
        '<td>\n' +
        '    <span class="mdc-typography--body1">' + name + '</span>\n' +
        '</td>\n' +
        '<td>\n' +
        '    <span class="mdc-typography--body1">' + to0 + '</span>\n' +
        '    <br>\n' +
        '    <span class="mdc-typography--body1">' + to1 + ' ' + to2 + '</span>\n' +
        '</td>\n' +
        '<td>\n' +
        '    <span class="mdc-typography--body1">' + kind + num + '张</span>\n' +
        '</td>\n' +
        '<td class="icon-button-td">\n' +
        '    <form action="" method="post" name="refund" id="refund-form-' + i + '">\n' +
        '        <input type="hidden" name="refund_ticket">\n' +
        '        <input type="hidden" name="train_id" value="' + train_id + '">\n' +
        '        <input type="hidden" name="from" value="' + from0 + '">\n' +
        '        <input type="hidden" name="to" value="' + to0 + '">\n' +
        '        <input type="hidden" name="date" value="' + from1 + '">\n' +
        '        <input type="hidden" name="kind" value="' + kind + '">\n' +
        '        <input type="hidden" name="num" value="' + num + '">\n' +
        '    </form>\n' +
        '    <button onclick="document.getElementById(\'refund-form-' + i + '\').submit();" class="material-icons mdc-icon-button" id="refund-button-' + i + '">cancel\n' +
        '    </button>\n' +
        '</td>'
    return ret;
};
{% for i in range(0, tickets|length) %}
document.getElementById('ticket-table').appendChild(new_row({{ i }}, '{{ tickets[i].train_id }}',
    '{{ tickets[i].name }}', '{{ tickets[i].from0 }}', '{{ tickets[i].from1 }}', '{{ tickets[i].from2 }}',
    '{{ tickets[i].to0 }}', '{{ tickets[i].to1 }}', '{{ tickets[i].to2 }}', '{{ tickets[i].kind }}',
    '{{ tickets[i].num }}'));
initialize_icon_button('refund-button-' + {{ i }});
{% endfor %}
{% endif %}
{% endif %}