import {MDCRipple} from "@material/ripple/component";
import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";

window.initialize_button = function (id) {
    new MDCRipple(document.getElementById(id));
};

window.initialize_icon_button = function (id) {
    const button = new MDCRipple(document.getElementById(id));
    button.unbounded = true;
};

window.initialize_text_field = function (id) {
    const text_field = new MDCTextField(document.getElementById(id + '-text-field'));
    new MDCTextFieldHelperText(document.getElementById(id + '-helper-text'));
    return text_field;
};