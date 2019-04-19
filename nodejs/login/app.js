import {MDCTextField} from '@material/textfield'
import {MDCRipple} from '@material/ripple/index';
import {MDCDialog} from '@material/dialog'

window.login_init = function () {
    console.log('Train Ticket');
    new MDCTextField(document.querySelector('.id'));
    new MDCTextField(document.querySelector('.password'));
    new MDCRipple(document.querySelector('.login-button'));
    new MDCRipple(document.querySelector('.login-reset-button'));
    new MDCRipple(document.querySelector('.jump-register-button'));
};

window.login_info_init = function () {
    window.login_info_dialog = new MDCDialog(document.querySelector('.login-info-dialog'));
};