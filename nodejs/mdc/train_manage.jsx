import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";

window.station_cnt = 60;
window.kind_cnt = 5;

function refresh_input() {
    document.querySelectorAll('input').forEach(function (node) {
        if (!node.disabled && node.oninput !== null) node.oninput(null);
    });
}

window.insert_station = function (index) {
    if (station_cnt >= 60) return;
    document.getElementById('row-' + station_cnt).classList.remove('hidden');
    station_text_field[station_cnt].disabled = false;
    arrive_text_field[station_cnt].disabled = false;
    depart_text_field[station_cnt].disabled = false;
    stopover_text_field[station_cnt].disabled = false;
    for (let j = 0; j < kind_cnt; j++)
        price_text_field[station_cnt][j].disabled = false;
    for (let i = station_cnt - 1; i >= index; i--) {
        station_text_field[i + 1].value = station_text_field[i].value;
        arrive_text_field[i + 1].value = arrive_text_field[i].value;
        depart_text_field[i + 1].value = depart_text_field[i].value;
        stopover_text_field[i + 1].value = stopover_text_field[i].value;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[i + 1][j].value = price_text_field[i][j].value;
    }
    station_text_field[index].value = '';
    arrive_text_field[index].value = '--:--';
    depart_text_field[index].value = '--:--';
    stopover_text_field[index].value = '--:--';
    for (let j = 0; j < kind_cnt; j++)
        price_text_field[index][j].value = '';
    station_cnt++;
    refresh_input();
};

window.delete_station = function (index) {
    if (station_cnt <= 2) return;
    for (let i = index; i + 1 < station_cnt; i++) {
        station_text_field[i].value = station_text_field[i + 1].value;
        arrive_text_field[i].value = arrive_text_field[i + 1].value;
        depart_text_field[i].value = depart_text_field[i + 1].value;
        stopover_text_field[i].value = stopover_text_field[i + 1].value;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[i][j].value = price_text_field[i + 1][j].value;
    }
    document.getElementById('row-' + (station_cnt - 1)).classList.add('hidden');
    station_text_field[station_cnt - 1].disabled = true;
    arrive_text_field[station_cnt - 1].disabled = true;
    depart_text_field[station_cnt - 1].disabled = true;
    stopover_text_field[station_cnt - 1].disabled = true;
    for (let j = 0; j < kind_cnt; j++)
        price_text_field[station_cnt - 1][j].disabled = true;
    station_cnt--;
    refresh_input();
};

window.add_kind = function () {
    if (kind_cnt >= 5) return;
    for (let i = 0; i < station_cnt; i++) {
        price_text_field[i][kind_cnt].disabled = false;
        price_text_field[i][kind_cnt].value = '';
    }
    kind_text_field[kind_cnt].disabled = false;
    document.querySelectorAll('.col-' + kind_cnt).forEach(function (node) {
        node.classList.remove('hidden');
    });
    kind_cnt++;
    refresh_input();
};

window.delete_kind = function (index) {
    if (kind_cnt <= 1) return;
    for (let i = 0; i < station_cnt; i++) {
        for (let j = index; j + 1 < kind_cnt; j++)
            price_text_field[i][j].value = price_text_field[i][j + 1].value;
        price_text_field[i][kind_cnt - 1].disabled = true;
    }
    kind_text_field[kind_cnt - 1].disabled = true;
    document.querySelectorAll('.col-' + (kind_cnt - 1)).forEach(function (node) {
        node.classList.add('hidden');
    });
    kind_cnt--;
    refresh_input();
};

window.set_dimension = function (station, kind) {
    while (station_cnt < station) {
        document.getElementById('row-' + station_cnt).classList.remove('hidden');
        station_text_field[station_cnt].disabled = false;
        arrive_text_field[station_cnt].disabled = false;
        depart_text_field[station_cnt].disabled = false;
        stopover_text_field[station_cnt].disabled = false;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[station_cnt][j].disabled = false;
        station_cnt++;
    }
    while (station_cnt > station) {
        document.getElementById('row-' + (station_cnt - 1)).classList.add('hidden');
        station_text_field[station_cnt - 1].disabled = true;
        arrive_text_field[station_cnt - 1].disabled = true;
        depart_text_field[station_cnt - 1].disabled = true;
        stopover_text_field[station_cnt - 1].disabled = true;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[station_cnt - 1][j].disabled = true;
        station_cnt--;
    }
    while (kind_cnt < station) {
        for (let i = 0; i < station_cnt; i++)
            price_text_field[i][kind_cnt].disabled = false;
        kind_text_field[kind_cnt].disabled = false;
        document.querySelectorAll('.col-' + kind_cnt).forEach(function (node) {
            node.classList.remove('hidden');
        });
        kind_cnt++;
    }
    while (kind_cnt > station) {
        for (let i = 0; i < station_cnt; i++)
            price_text_field[i][kind_cnt - 1].disabled = true;
        kind_text_field[kind_cnt - 1].disabled = true;
        document.querySelectorAll('.col-' + (kind_cnt - 1)).forEach(function (node) {
            node.classList.add('hidden');
        });
        kind_cnt--;
    }
    refresh_input();
};

window.train_manage_init = function () {
    window.input_text_field = new MDCTextField(document.getElementById('input-text-field'));
    new MDCTextFieldHelperText(document.getElementById('input-helper-text'));
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'));
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'));
    window.catalog_text_field = new MDCTextField(document.getElementById('catalog-text-field'));
    new MDCTextFieldHelperText(document.getElementById('catalog-helper-text'));
    initialize_icon_button('add-station-button');
    let i, j;
    window.station_text_field = [];
    window.arrive_text_field = [];
    window.depart_text_field = [];
    window.stopover_text_field = [];
    window.price_text_field = [];
    window.kind_text_field = [];
    for (i = 0; i < 60; i++) {
        initialize_icon_button('delete-station-' + i + '-button');
        initialize_icon_button('insert-station-' + i + '-button');
        station_text_field.push(new MDCTextField(document.getElementById('station-' + i + '-text-field')));
        arrive_text_field.push(new MDCTextField(document.getElementById('arrive-' + i + '-text-field')));
        depart_text_field.push(new MDCTextField(document.getElementById('depart-' + i + '-text-field')));
        stopover_text_field.push(new MDCTextField(document.getElementById('stopover-' + i + '-text-field')));
        const n = [];
        for (j = 0; j < 5; j++)
            n.push(new MDCTextField(document.getElementById('price-' + i + '-' + j + '-text-field')));
        price_text_field.push(n);
    }
    for (j = 0; j < 5; j++) {
        kind_text_field.push(new MDCTextField(document.getElementById('kind-' + j + '-text-field')));
        initialize_icon_button('delete-kind-' + j + '-button');
    }
    initialize_icon_button('add-kind-button');
    set_dimension(2, 2);
};