import {MDCDialog} from "@material/dialog/component";
import {MDCTopAppBar} from "@material/top-app-bar/component";
import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";
import {MDCDrawer} from "@material/drawer/component";

window.base_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', function () {
        window.drawer.open = !window.drawer.open
    });
};

window.base_info_init = function () {
    window.base_info_dialog = new MDCDialog(document.getElementById('base-info-dialog'));
    window.show_dialog = function (title, content, button_label, redirect) {
        document.getElementById('alert-dialog-title-text').innerText = title;
        document.getElementById('alert-dialog-content-text').innerText = content;
        document.getElementById('alert-dialog-button-label').innerText = button_label;
        if (redirect !== '') {
            document.getElementById('alert-dialog-button').onclick = function () {
                location.href = redirect
            }
        }
        base_info_dialog.open()
    };
};

window.verify_init = function () {
    window.verify_dialog = new MDCDialog(document.getElementById('verify-dialog'));
    const text_field = new MDCTextField(document.getElementById('verify_password-text-field'));
    new MDCTextFieldHelperText(document.getElementById('verify_password-helper-text'));
    verify_dialog.listen('MDCDialog:opened', function () {
        text_field.layout()
    });
    const verify_operation = document.getElementById('verify-operation');
    const verify_warning = document.getElementById('verify-warning');
    window.show_verify = function (operation, warning) {
        verify_operation.innerText = operation;
        verify_warning.innerText = warning;
        verify_dialog.open()
    };
};