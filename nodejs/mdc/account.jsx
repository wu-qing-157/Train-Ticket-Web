import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";

window.account_init = function () {
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
    window.new_password_repeat_text_field = new MDCTextField(document.getElementById('new_password_repeat-text-field'));
    new MDCTextFieldHelperText(document.getElementById('new_password_repeat-helper-text'));
    new MDCRipple(document.getElementById('modify-reset-button'));
    new MDCRipple(document.getElementById('modify-button'));
    const start_edit_button = new MDCRipple(document.getElementById('start-edit'));
    start_edit_button.unbounded = true;
    new MDCRipple(document.getElementById('verify-edit'));
};