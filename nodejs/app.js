import {MDCTextField} from '@material/textfield'
import {MDCFormField} from '@material/form-field';
import {MDCCheckbox} from '@material/checkbox';
import {MDCRipple} from '@material/ripple/index';
import {MDCDialog} from '@material/dialog'

window.input_init = function () {
    console.log('Train Ticket');
    new MDCTextField(document.querySelector('.username'));
    new MDCTextField(document.querySelector('.password'));
    // const checkbox_remember_username = new MDCCheckbox(document.querySelector('.remember-username'));
    // const form_field_remember_username = new MDCFormField(document.querySelector('.remember-username-form'));
    // form_field_remember_username.input = checkbox_remember_username;
    new MDCRipple(document.querySelector('.login-button'));
    new MDCRipple(document.querySelector('.login-reset-button'));
    new MDCRipple(document.querySelector('.jump-register-button'));
};

window.register_init = function () {
    new MDCTextField(document.querySelector('.password'));
    new MDCTextField(document.querySelector('.password-repeat'));
    new MDCTextField(document.querySelector('.email'));
    new MDCTextField(document.querySelector('.phone'));
    new MDCRipple(document.querySelector('.register-button'));
    new MDCRipple(document.querySelector('.register-reset-button'));
    new MDCRipple(document.querySelector('.jump-login-button'));
};

window.login_info_init = function () {
    window.login_info_dialog = new MDCDialog(document.querySelector('.login-info-dialog'));
};

// new MDCRipple(document.querySelector('.foo-button'));
// new MDCFloatingLabel(document.querySelector('.mdc-floating-label'));
// new MDCLineRipple(document.querySelector('.mdc-line-ripple'));