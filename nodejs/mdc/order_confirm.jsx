import {MDCSelect} from '@material/select/component'
import {MDCTextField} from "@material/textfield/component";
import {MDCTextFieldHelperText} from "@material/textfield/index";

window.order_confirm_init = function () {
    window.kind_select = new MDCSelect(document.getElementById('kind-select'));
    window.num_text_field = new MDCTextField(document.getElementById('num-text-field'));
    window.num_helper_text = new MDCTextFieldHelperText(document.getElementById('num-helper-text'));
    kind_select.listen('MDCSelect:change', () => {
        document.getElementById('num-helper-text').innerText = '数量不能超过余票（' + window.left_num[kind_select.selectedIndex] + '张）';
        document.getElementById('num-label').innerText = '数量（余' + window.left_num[kind_select.selectedIndex] + '）张';
        document.getElementById('num').setAttribute('max', '' + window.left_num[kind_select.selectedIndex]);
        document.getElementById('num').oninput(null);
        document.getElementById('num').focus();
    })
};