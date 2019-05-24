{{ train_id }} {{ name }} {{ catalog }}
{% for item in kinds %}{{ item }} {% endfor %}
{% for item in stations %}
{{ item.name }} {{ item.arrive }} {{ item.depart }} {{ item.stopover }}{% for price in item.prices %} {{ price }}{% endfor %}
{% endfor %}