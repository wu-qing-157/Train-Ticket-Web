{% if not_exsit %}
document.getElementById('hint').innerText = '没有找到该车次，您可以填写以下内容来新增车次 {{ train_id }}';
document.getElementById('train-manage-button-icon').innerText = 'check';
document.getElementById('train-manage-button-label').innerText = '添加车次';
document.getElementById('train-id').value = '{{ train_id }}';
document.getElementById('request-type').value = 'add';
{% else %}
{% if sold %}
document.getElementById('hint').innerText = '以下为车次 {{ train_id }} 的信息（该车次已开售，任何修改均无法提交）';
document.getElementById('train-manage-button-icon').innerText = 'cancel';
document.getElementById('train-manage-button-label').innerText = '车次已开售';
{% else %}
document.getElementById('hint').innerText = '以下为车次 {{ train_id }} 的信息';
document.getElementById('train-manage-button-icon').innerText = 'check';
document.getElementById('train-manage-button-label').innerText = '提交修改';
{% endif %}
document.getElementById('train-id').value = '{{ train_id }}';
document.getElementById('request-type').value = 'modify';
set_dimension({{ stations|length }}, {{ kinds|length }});
name_text_field.value = '{{ name }}';
catalog_text_field.value = '{{ catalog }}';
{% for j in range(0, kinds|length) %}
kind_text_field[{{ j }}].value = '{{ kinds[j] }}';
{% endfor %}
{% for i in range(0, stations|length) %}
station_text_field[{{ i }}].value = '{{ stations[i].name }}';
arrive_text_field[{{ i }}].value = '{{ stations[i].arrive }}';
depart_text_field[{{ i }}].value = '{{ stations[i].depart }}';
stopover_text_field[{{ i }}].value = '{{ stations[i].stopover }}';
{% for j in range(0, kinds|length) %}
price_text_field[{{ i }}][{{ j }}].value = '{{ stations[i].prices[j] }}';
{% endfor %}
{% endfor %}
set_dimension({{ stations|length }}, {{ kinds|length }});
{% endif %}
document.getElementById('hint').classList.remove('hidden');