import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";
import {MDCRipple} from "@material/ripple/component";
import {MDCDialog} from "@material/dialog/component";

window.register_init = function () {
    new MDCTextField(document.getElementById('id-text-field'));
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'));
    new MDCTextField(document.getElementById('password-text-field'));
    new MDCTextFieldHelperText(document.getElementById('password-helper-text'));
    new MDCTextField(document.getElementById('password_repeat-text-field'));
    new MDCTextFieldHelperText(document.getElementById('password_repeat-helper-text'));
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'));
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'));
    window.email_text_field = new MDCTextField(document.getElementById('email-text-field'));
    new MDCTextFieldHelperText(document.getElementById('email-helper-text'));
    window.phone_text_field = new MDCTextField(document.getElementById('phone-text-field'));
    new MDCTextFieldHelperText(document.getElementById('phone-helper-text'));
    new MDCRipple(document.getElementById('register-button'));
    new MDCRipple(document.getElementById('register-reset-button'));
    new MDCRipple(document.getElementById('jump-login-button'));
};

window.register_info_init = function () {
    window.register_info_dialog = new MDCDialog(document.getElementById('register-info-dialog'));
};