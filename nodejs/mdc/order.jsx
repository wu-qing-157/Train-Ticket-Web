import React, {useState} from "react";
import {KeyboardDatePicker, MuiPickersUtilsProvider} from "@material-ui/pickers";
import DateFnsUtils from "@date-io/date-fns";
import zhLocale from "date-fns/locale/zh-CN"
import ReactDOM from "react-dom";
import {MDCTextField} from "@material/textfield/component";
import {MDCMenu} from "@material/menu/component";
import {MDCRipple} from "@material/ripple/component";
import {MDCDialog} from "@material/dialog/component";
import {MDCList} from "@material/list/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";

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

window.order_init = function () {
    window.catalog_inner = ['G', 'D', 'Z', 'T', 'K', 'L'];
    window.catalog_display = ['高铁', '动车', '直达', '特快', '快速', '临客'];
    window.depart_text_field = new MDCTextField(document.getElementById('depart-text-field'));
    window.depart_menu = new MDCMenu(document.getElementById('depart-menu'));
    window.arrive_text_field = new MDCTextField(document.getElementById('arrive-text-field'));
    window.arrive_menu = new MDCMenu(document.getElementById('arrive-menu'));
    ReactDOM.render(<QueryDatePicker/>, document.getElementById('date-picker'));
    window.catalog_text_field = new MDCTextField(document.getElementById('catalog-text-field'));
    new MDCTextFieldHelperText(document.getElementById('catalog-helper-text'));
    new MDCRipple(document.getElementById('query-ticket-button'));
    new MDCRipple(document.getElementById('query-transfer-button'));
    window.catalog_dialog = new MDCDialog(document.getElementById('catalog-dialog'));
    window.catalog_list = new MDCList(document.getElementById('catalog-list'));
    catalog_dialog.listen('MDCDialog:opened', function () {
        catalog_list.layout();
    });
    catalog_dialog.listen('MDCDialog:closed', function () {
        catalog_text_field.value = catalog_list.selectedIndex.map(function (index) {
            return catalog_inner[index] + ' ' + catalog_display[index]
        }).join('/');
        document.getElementById('catalog-inner').value = catalog_list.selectedIndex.map(function (index) {
            return catalog_inner[index]
        }).join('');
        document.getElementById('catalog').oninput(null);
    })
};