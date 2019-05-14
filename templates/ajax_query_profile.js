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
    document.getElementById('name').oninput();
    document.getElementById('email').oninput();
    document.getElementById('phone').oninput();
    document.getElementById('new_password').oninput();
    document.getElementById('grant-button').disabled = true;
{% else %}
    document.getElementById('id-info').innerText = '{{ user_id }}';
    document.getElementById('name-info').innerText = '{{ name }}';
    document.getElementById('email-info').innerText = '{{ email }}';
    document.getElementById('phone-info').innerText = '{{ phone }}';
    document.getElementById('administrator-info').innerText = '{% if administrator %} 管理员 {% else %} 普通用户 {% endif %}';
    document.getElementById('modify-status').innerText = '将修改用户 {{ user_id }} 的用户信息';
    document.getElementById('grant-status').innerText = {% if administrator %} '用户 {{ user_id }} 已经是管理员'
{% else %} '将授予用户 {{ user_id }} 管理员权限' {% endif %};
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
    document.getElementById('name').oninput();
    document.getElementById('email').oninput();
    document.getElementById('phone').oninput();
    document.getElementById('grant-button').disabled = {% if administrator %} true {% else %} false {% endif %};
{% endif %}