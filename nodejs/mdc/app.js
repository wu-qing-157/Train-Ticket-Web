import {MDCTopAppBar} from '@material/top-app-bar/index';
import {MDCDrawer} from "@material/drawer";
import {MDCTextField} from '@material/textfield';
import {MDCRipple} from '@material/ripple/index';
import {MDCDialog} from '@material/dialog';
import {MDCFormField} from '@material/form-field';
import {MDCCheckbox} from '@material/checkbox';
import {MDCTextFieldHelperText} from '@material/textfield/helper-text';

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
};

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

window.base_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', () => {
        window.drawer.open = !window.drawer.open;
    });
};

window.base_info_init = function () {
    window.base_info_dialog = new MDCDialog(document.getElementById('base-info-dialog'));
    window.show_dialog = (title, content, button_label, redirect) => {
        document.getElementById('alert-dialog-title-text').innerText = title;
        document.getElementById('alert-dialog-content-text').innerText = content;
        document.getElementById('alert-dialog-button-label').innerText = button_label;
        if (redirect !== '') {
            document.getElementById('alert-dialog-button').onclick = () => {
                location.href = redirect;
            };
        }
        base_info_dialog.open();
    };
};

window.verify_init = function () {
    window.verify_dialog = new MDCDialog(document.getElementById('verify-dialog'));
    const text_field = new MDCTextField(document.getElementById('verify_password-text-field'));
    verify_dialog.listen('MDCDialog:opened', () => {
        text_field.layout();
    });
    const verify_operation = document.getElementById('verify-operation');
    const verify_warning = document.getElementById('verify-warning');
    window.show_verify = function (operation, warning) {
        verify_operation.innerText = operation;
        verify_warning.innerText = warning;
        verify_dialog.open();
    }
};

window.main_page_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', () => {
        window.drawer.open = !window.drawer.open;
    });
    const refresh_button = new MDCRipple(document.getElementById('refresh'));
    refresh_button.unbounded = true;
};