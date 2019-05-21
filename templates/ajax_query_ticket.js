{% if error_info %}
document.getElementById('query-ticket-error-info').classList.remove('hidden');
document.getElementById('query-ticket-error-info').innerText = '{{ error_info }}';
{% else %}
window.target_table = document.getElementById('ticket-table');
function new_row(from0, from1, from2, name, to0, to1, to2, price, id, inner) {
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
        '        <button class="material-icons mdc-icon-button" id="' + id + '" onclick="location.href=\'order?'
        + 'train=' + id +
        '&name=' + name +
        '&from0=' + from0 +
        '&from1=' + from1 +
        '&from2=' + from2 +
        '&to0=' + to0 +
        '&to1=' + to1 +
        '&to2=' + to2 +
        '&price=' + inner + '\'">\n' +
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
target_table.appendChild(new_row('{{ item.from_ }}', '{{ item._from_date }}', '{{ item._from_time }}', '{{ item.name }}',
    '{{ item.to }}', '{{ item.to_date }}', '{{ item.to_time }}', '{{ item.ticket_info() }}', '{{ item.id_ }}',
    '{{ item.ticket_info_inner() }}'));
{% endfor %}
{% for item in ticket_list %}
process_icon_button('{{ item.id_ }}');
{% endfor %}
{% endif %}