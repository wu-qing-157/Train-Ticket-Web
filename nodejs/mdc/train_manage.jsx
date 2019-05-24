import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";
import React, {useState} from "react";
import {KeyboardDatePicker, MuiPickersUtilsProvider} from "@material-ui/pickers";
import DateFnsUtils from "@date-io/date-fns";
import zhLocale from "date-fns/locale/zh-CN";
import ReactDOM from "react-dom";

function QueryDatePicker() {
    const [selectedDate, handleDateChange] = useState(new Date());

    return (
        <MuiPickersUtilsProvider utils={DateFnsUtils} locale={zhLocale}>
            <KeyboardDatePicker
                autoOk
                variant="inline"
                inputVariant="outlined"
                label="出发日期"
                format="yyyy-MM-dd"
                value={selectedDate}
                InputAdornmentProps={{position: "start"}}
                onChange={date => handleDateChange(date)}
            />
        </MuiPickersUtilsProvider>
    );
}

window.station_cnt = 0;
window.kind_cnt = 0;

window.insert_station = function (index) {
    if (station_cnt === 60) return;
    document.getElementById('delete-station-' + station_cnt + '-button').classList.remove('hidden');
    document.getElementById('insert-station-' + station_cnt + '-button').classList.remove('hidden');
    document.getElementById('station-' + station_cnt + '-text-field').classList.remove('hidden');
    document.getElementById('arrive-' + station_cnt + '-text-field').classList.remove('hidden');
    document.getElementById('depart-' + station_cnt + '-text-field').classList.remove('hidden');
    document.getElementById('stopover-' + station_cnt + '-text-field').classList.remove('hidden');
    for (let j = 0; j < kind_cnt; j++)
        document.getElementById('price-' + station_cnt + '-' + j + '-text-field').classList.remove('hidden');
    for (let i = station_cnt - 1; i >= index; i++) {
        station_text_field[i + 1].value = station_text_field[i].value;
        arrive_text_field[i + 1].value = arrive_text_field[i].value;
        depart_text_field[i + 1].value = depart_text_field[i].value;
        stopover_text_field[i + 1].value = stopover_text_field[i].value;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[i + 1][j].value = price_text_field[i][j].value;
    }
    station_text_field[index] = '';
    arrive_text_field[index] = '--:--';
    depart_text_field[index] = '--:--';
    stopover_text_field[index] = '--:--';
    for (let j = 0; j < kind_cnt; j++)
        price_text_field[index][j].value = '';
    station_cnt++;
};

window.delete_station = function (index) {
    if (station_cnt === 2) return;
    for (let i = index; i + 1 < station_cnt; i++) {
        station_text_field[i].value = station_text_field[i + 1].value;
        arrive_text_field[i].value = arrive_text_field[i + 1].value;
        depart_text_field[i].value = depart_text_field[i + 1].value;
        stopover_text_field[i].value = stopover_text_field[i + 1].value;
        for (let j = 0; j < kind_cnt; j++)
            price_text_field[i][j].value = price_text_field[i + 1][j].value;
    }
    document.getElementById('delete-station-' + (station_cnt - 1) + '-button').classList.add('hidden');
    document.getElementById('insert-station-' + (station_cnt - 1) + '-button').classList.add('hidden');
    document.getElementById('station-' + (station_cnt - 1) + '-text-field').classList.add('hidden');
    document.getElementById('arrive-' + (station_cnt - 1) + '-text-field').classList.add('hidden');
    document.getElementById('depart-' + (station_cnt - 1) + '-text-field').classList.add('hidden');
    document.getElementById('stopover-' + (station_cnt - 1) + '-text-field').classList.add('hidden');
    for (let j = 0; j < kind_cnt; j++)
        document.getElementById('price-' + (station_cnt - 1) + '-' + j + '-text-field').classList.add('hidden');
    station_cnt--;
};

window.add_kind = function () {
    if (kind_cnt === 5) return;
    for (let i = 0; i < station_cnt; i++) {
        document.getElementById('price-' + i + '-' + kind_cnt + '-text-field').classList.remove('hidden');
        price_text_field[i][station_cnt].value = '';
    }
    document.getElementById('delete-kind-' + kind_cnt + '-button').classList.remove('hidden');
    document.getElementById('kind-' + kind_cnt + '-text-field').classList.remove('hidden');
    kind_cnt++;
};

window.delete_kind = function (index) {
    if (kind_cnt === 1) return;
    for (let i = 0; i < station_cnt; i++) {
        for (let j = index; j + 1 < kind_cnt; j++)
            price_text_field[i][j].value = price_text_field[i][j + 1].value;
        document.getElementById('price-' + i + '-' + (kind_cnt - 1) + '-text-field').classList.add('hidden');
    }
    document.getElementById('delete-kind-' + (kind_cnt - 1) + '-button').classList.add('hidden');
    document.getElementById('kind-' + (kind_cnt - 1) + '-text-field').classList.add('hidden');
    kind_cnt--;
};

window.set_dimension = function (station, kind) {
    while (station_cnt > station) delete_station(station_cnt - 1);
    while (station_cnt < station) insert_station(station_cnt - 1);
    while (kind_cnt > kind) delete_kind(kind_cnt - 1);
    while (kind_cnt < kind) add_kind();
};

window.train_manage_init = function () {
    window.input_text_field = new MDCTextField(document.getElementById('input-text-field'));
    new MDCTextFieldHelperText(document.getElementById('input-helper-text'));
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'));
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'));
    window.catalog_text_field = new MDCTextField(document.getElementById('catalog-text-field'));
    new MDCTextFieldHelperText(document.getElementById('catalog-helper-text'));
    ReactDOM.render(<QueryDatePicker/>, document.getElementById('date-picker'));
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
};