import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";
import {MDCRipple} from "@material/ripple/component";
import {MDCDialog} from "@material/dialog/component";

window.login_init = function () {
    window.id_text_field = new MDCTextField(document.getElementById('id-text-field'));
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'));
    window.password_text_field = new MDCTextField(document.getElementById('password-text-field'));
    new MDCTextFieldHelperText(document.getElementById('password-helper-text'));
    new MDCRipple(document.getElementById('login-button'));
    new MDCRipple(document.getElementById('jump-register-button'));
};

window.login_info_init = function () {
    window.login_info_dialog = new MDCDialog(document.getElementById('login-info-dialog'));
};