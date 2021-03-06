{% if error_info %}
document.getElementById('query-ticket-error-info').classList.remove('hidden');
document.getElementById('query-ticket-error-info').innerText = '{{ error_info }}';
{% else %}
{% if transfer %}
document.getElementById('query-ticket-error-info').classList.remove('hidden');
document.getElementById('query-ticket-error-info').innerText = '以下为连续换乘方案';
{% endif %}
window.target_table = document.getElementById('ticket-table');
function new_row(from0, from1, from2, name, to0, to1, to2, price, id) {
    const ret = document.createElement('tbody');
    ret.innerHTML =
        '<tr>\n' +
        '    <td>\n' +
        '        <span class="mdc-typography--body1">' + from0 + '</span>\n' +
        '        <br>\n' +
        '        <span class="mdc-typography--body1">' + from1 + ' ' + from2 + '</span>\n' +
        '    </td>\n' +
        '    <td>\n' +
        '        <span class="mdc-typography--body1">' + name + '</span>\n' +
        '    </td>\n' +
        '    <td>\n' +
        '        <span class="mdc-typography--body1">' + to0 + '</span>\n' +
        '        <br>\n' +
        '        <span class="mdc-typography--body1">' + to1 + ' ' + to2 + '</span>\n' +
        '    </td>\n' +
        '    <td rowspan="2" class="icon-button-td">\n' +
        '        <button class="material-icons mdc-icon-button" id="order-button-' + id + '">\n' +
        '            add_shopping_cart\n' +
        '        </button>\n' +
        '    </td>\n' +
        '</tr>\n' +
        '<tr>\n' +
        '    <td colspan="3">' + price + '</td>\n' +
        '</tr>';
    return ret;
}
{% for item in ticket_list %}
target_table.appendChild(new_row('{{ item.from_ }}', '{{ item.from_date }}', '{{ item.from_time }}', '{{ item.name }}',
    '{{ item.to }}', '{{ item.to_date }}', '{{ item.to_time }}', '{{ item.ticket_info() }}', '{{ item.id_ }}'));
{% endfor %}
{% for item in ticket_list %}
document.getElementById('order-button-{{ item.id_ }}').onclick = function () {
    open('?id={{ item.id_ }}&from={{ item.from_ }}&to={{ item.to }}&date={{ item.from_date }}')
};
initialize_icon_button('order-button-{{ item.id_ }}');
{% endfor %}
{% endif %}