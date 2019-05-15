import {MDCTopAppBar} from '@material/top-app-bar/index'
import {MDCDrawer} from "@material/drawer"
import {MDCTextField} from '@material/textfield'
import {MDCRipple} from '@material/ripple/index'
import {MDCDialog} from '@material/dialog'
import {MDCTextFieldHelperText} from '@material/textfield/helper-text'
import {MDCMenu} from '@material/menu';

window.account_init = function () {
    window.id_text_field = new MDCTextField(document.getElementById('id-text-field'))
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'))
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'))
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'))
    window.email_text_field = new MDCTextField(document.getElementById('email-text-field'))
    new MDCTextFieldHelperText(document.getElementById('email-helper-text'))
    window.phone_text_field = new MDCTextField(document.getElementById('phone-text-field'))
    new MDCTextFieldHelperText(document.getElementById('phone-helper-text'))
    window.new_password_text_field = new MDCTextField(document.getElementById('new_password-text-field'))
    new MDCTextFieldHelperText(document.getElementById('new_password-helper-text'))
    window.new_password_repeat_text_field = new MDCTextField(document.getElementById('new_password_repeat-text-field'))
    new MDCTextFieldHelperText(document.getElementById('new_password_repeat-helper-text'))
    new MDCRipple(document.getElementById('modify-reset-button'))
    new MDCRipple(document.getElementById('modify-button'))
    const start_edit_button = new MDCRipple(document.getElementById('start-edit'))
    start_edit_button.unbounded = true
    new MDCRipple(document.getElementById('verify-edit'))
}

window.account_manage_init = function () {
    window.input_text_field = new MDCTextField(document.getElementById('input-text-field'))
    new MDCTextFieldHelperText(document.getElementById('input-helper-text'))
    window.id_text_field = new MDCTextField(document.getElementById('id-text-field'))
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'))
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'))
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'))
    window.email_text_field = new MDCTextField(document.getElementById('email-text-field'))
    new MDCTextFieldHelperText(document.getElementById('email-helper-text'))
    window.phone_text_field = new MDCTextField(document.getElementById('phone-text-field'))
    new MDCTextFieldHelperText(document.getElementById('phone-helper-text'))
    window.new_password_text_field = new MDCTextField(document.getElementById('new_password-text-field'))
    new MDCTextFieldHelperText(document.getElementById('new_password-helper-text'))
    new MDCRipple(document.getElementById('modify-button'))
}

window.register_init = function () {
    new MDCTextField(document.getElementById('id-text-field'))
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'))
    new MDCTextField(document.getElementById('password-text-field'))
    new MDCTextFieldHelperText(document.getElementById('password-helper-text'))
    new MDCTextField(document.getElementById('password_repeat-text-field'))
    new MDCTextFieldHelperText(document.getElementById('password_repeat-helper-text'))
    window.name_text_field = new MDCTextField(document.getElementById('name-text-field'))
    new MDCTextFieldHelperText(document.getElementById('name-helper-text'))
    window.email_text_field = new MDCTextField(document.getElementById('email-text-field'))
    new MDCTextFieldHelperText(document.getElementById('email-helper-text'))
    window.phone_text_field = new MDCTextField(document.getElementById('phone-text-field'))
    new MDCTextFieldHelperText(document.getElementById('phone-helper-text'))
    new MDCRipple(document.getElementById('register-button'))
    new MDCRipple(document.getElementById('register-reset-button'))
    new MDCRipple(document.getElementById('jump-login-button'))
}

window.register_info_init = function () {
    window.register_info_dialog = new MDCDialog(document.getElementById('register-info-dialog'))
}

window.login_init = function () {
    window.id_text_field = new MDCTextField(document.getElementById('id-text-field'))
    new MDCTextFieldHelperText(document.getElementById('id-helper-text'))
    window.password_text_field = new MDCTextField(document.getElementById('password-text-field'))
    new MDCTextFieldHelperText(document.getElementById('password-helper-text'))
    new MDCRipple(document.getElementById('login-button'))
    new MDCRipple(document.getElementById('jump-register-button'))
}

window.login_info_init = function () {
    window.login_info_dialog = new MDCDialog(document.getElementById('login-info-dialog'))
}

window.base_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'))
    appBar.setScrollTarget(document.getElementById('main-content'))
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'))
    appBar.listen('MDCTopAppBar:nav', function () {
        window.drawer.open = !window.drawer.open
    })
}

window.base_info_init = function () {
    window.base_info_dialog = new MDCDialog(document.getElementById('base-info-dialog'))
    window.show_dialog = function (title, content, button_label, redirect) {
        document.getElementById('alert-dialog-title-text').innerText = title
        document.getElementById('alert-dialog-content-text').innerText = content
        document.getElementById('alert-dialog-button-label').innerText = button_label
        if (redirect !== '') {
            document.getElementById('alert-dialog-button').onclick = function () {
                location.href = redirect
            }
        }
        base_info_dialog.open()
    }
}

window.verify_init = function () {
    window.verify_dialog = new MDCDialog(document.getElementById('verify-dialog'))
    const text_field = new MDCTextField(document.getElementById('verify_password-text-field'))
    new MDCTextFieldHelperText(document.getElementById('verify_password-helper-text'))
    verify_dialog.listen('MDCDialog:opened', function () {
        text_field.layout()
    })
    const verify_operation = document.getElementById('verify-operation')
    const verify_warning = document.getElementById('verify-warning')
    window.show_verify = function (operation, warning) {
        verify_operation.innerText = operation
        verify_warning.innerText = warning
        verify_dialog.open()
    }
}

window.main_page_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'))
    appBar.setScrollTarget(document.getElementById('main-content'))
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'))
    appBar.listen('MDCTopAppBar:nav', function () {
        window.drawer.open = !window.drawer.open
    })
    const refresh_button = new MDCRipple(document.getElementById('refresh'))
    refresh_button.unbounded = true
}

window.order_init = function () {
    window.depart_text_field = new MDCTextField(document.getElementById('depart-text-field'))
    window.depart_menu = new MDCMenu(document.getElementById('depart-menu'))
}

window.new_menu_item = function (name, input, inputDOM, menu) {
    const new_item = document.createElement('li')
    new_item.setAttribute('role', 'menuitem')
    new_item.onclick = function () {
        input.value = name
        inputDOM.oninput()
        menu.open = false
    }
    new_item.classList.add('mdc-list-item')
    new_item.innerHTML = '<span class="mdc-list-item__text">' + name + '</span>'
    return new_item
}

window.level0 = []
window.level1 = []
window.level2 = []
window.station_suggest_init_cnt = 0

window.station_suggest_init = function () {
    if (station_suggest_init_cnt == 2) return
    window.station_suggest_init_cnt = 0
    const http0 = new XMLHttpRequest()
    http0.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ret = this.responseText
            if (ret.charAt(ret.length - 1) === '\n')
                ret = ret.substring(0, ret.length - 1)
            ret.split('\n').forEach(function (value) {
                level0.push(value.split(' '))
            })
            station_suggest_init_cnt++
        }
    }
    http0.open('GET', 'station_list_0', true)
    http0.send()
    const http2 = new XMLHttpRequest()
    http2.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ret = this.responseText
            if (ret.charAt(ret.length - 1) === '\n')
                ret = ret.substring(0, ret.length - 1)
            ret.split('\n').forEach(function (value) {
                level2.push(value.split(' '))
            })
            station_suggest_init_cnt++
        }
    }
    http2.open('GET', 'station_list_2', true)
    http2.send()
}

function add_station_suggest(keyword, input, inputDOM, menu, menuDOM) {
    const menu_item_max = 15
    var cnt = 0
    var i
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) >= 0) {
            menuDOM.appendChild(new_menu_item(level0[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && level0[i][1].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level0[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && !(level0[i][1].startsWith(keyword)) && level0[i][2].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level0[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) >= 0) {
            menuDOM.appendChild(new_menu_item(level2[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && level2[i][1].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level2[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && !(level2[i][1].startsWith(keyword)) && level2[i][2].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level2[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && level0[i][1].indexOf(keyword) > 0 && level0[i][2].indexOf(keyword) < 0) {
            menuDOM.appendChild(new_menu_item(level0[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && level2[i][1].indexOf(keyword) > 0 && level2[i][2].indexOf(keyword) < 0) {
            menuDOM.appendChild(new_menu_item(level2[i][0], input, inputDOM, menu))
            cnt++
            if (cnt == menu_item_max) return
        }
}

window.update_station_suggest = function (input, inputDOM, menu, menuDOM) {
    const keyword = input.value.toLowerCase()
    menuDOM.innerHTML = ''
    add_station_suggest(keyword, input, inputDOM, menu, menuDOM)
    menu.initialize()
    menu.open = true
}