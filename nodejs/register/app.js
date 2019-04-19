import {MDCTextField} from '@material/textfield'
import {MDCRipple} from '@material/ripple/index';
import {MDCDialog} from '@material/dialog'

window.register_init = function () {
    new MDCTextField(document.querySelector('.id'));
    new MDCTextField(document.querySelector('.password'));
    new MDCTextField(document.querySelector('.password-repeat'));
    new MDCTextField(document.querySelector('.name'));
    new MDCTextField(document.querySelector('.email'));
    new MDCTextField(document.querySelector('.phone'));
    new MDCRipple(document.querySelector('.register-button'));
    new MDCRipple(document.querySelector('.register-reset-button'));
    new MDCRipple(document.querySelector('.jump-login-button'));
};

window.register_info_init = function() {
    window.register_info_dialog = new MDCDialog(document.querySelector('.register-info-dialog'));
};

// new MDCRipple(document.querySelector('.foo-button'));
// new MDCFloatingLabel(document.querySelector('.mdc-floating-label'));
// new MDCLineRipple(document.querySelector('.mdc-line-ripple'));