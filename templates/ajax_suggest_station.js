{% if empty %}
{% else %}
document.getElementById('{{ which }}').classList.remove('hidden');
var result_html = '';
{% for item in ret %}
result_html += '<button class="mdc-button" onclick="document.getElementById("{{ target_input }}"").value = "{{ item }}; station_suggest_dialog.close()"><span class="mdc-button__label">{{ item }}</span></button>';
{% endfor %}
document.getElementById('{{ which }}-button').innerHTML = result_html;
{% endif %}