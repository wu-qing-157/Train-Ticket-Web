import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";
import {MDCRipple} from "@material/ripple/component";
import React, {useState} from "react";
import {KeyboardDatePicker, MuiPickersUtilsProvider} from "@material-ui/pickers";
import DateFnsUtils from "@date-io/date-fns";
import {MDCMenu} from "@material/menu/component";
import ReactDOM from "react-dom";

function QueryDatePicker() {
    const [selectedDate, handleDateChange] = useState(new Date());

    return (
        <MuiPickersUtilsProvider utils={DateFnsUtils}>
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

window.account_manage_init = function () {
    window.input_text_field = new MDCTextField(document.getElementById('input-text-field'));
    new MDCTextFieldHelperText(document.getElementById('input-helper-text'));
    window.id_text_field = new MDCTextField(document.getElementById('id-text-field'));
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'));
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'));
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'));
    window.email_text_field = new MDCTextField(document.getElementById('email-text-field'));
    new MDCTextFieldHelperText(document.getElementById('email-helper-text'));
    window.phone_text_field = new MDCTextField(document.getElementById('phone-text-field'));
    new MDCTextFieldHelperText(document.getElementById('phone-helper-text'));
    window.new_password_text_field = new MDCTextField(document.getElementById('new_password-text-field'));
    new MDCTextFieldHelperText(document.getElementById('new_password-helper-text'));
    new MDCRipple(document.getElementById('modify-button'));
    window.train_id_text_field = new MDCTextField(document.getElementById('train_id-text-field'));
    new MDCTextFieldHelperText(document.getElementById('train_id-helper-text'));
    window.depart_text_field = new MDCTextField(document.getElementById('depart-text-field'));
    window.depart_menu = new MDCMenu(document.getElementById('depart-menu'));
    window.arrive_text_field = new MDCTextField(document.getElementById('arrive-text-field'));
    window.arrive_menu = new MDCMenu(document.getElementById('arrive-menu'));
    ReactDOM.render(<QueryDatePicker/>, document.getElementById('date-picker'));
    window.kind_text_field = new MDCTextField(document.getElementById('kind-text-field'));
    new MDCTextFieldHelperText(document.getElementById('kind-helper-text'));
    window.num_text_field = new MDCTextField(document.getElementById('num-text-field'));
    new MDCTextFieldHelperText(document.getElementById('num-helper-text'));
    new MDCRipple(document.getElementById('buy-ticket-button'))
};