import {MDCTopAppBar} from '@material/top-app-bar/index'
import {MDCDrawer} from "@material/drawer"
import {MDCTextField} from '@material/textfield'
import {MDCRipple} from '@material/ripple/index'
import {MDCDialog} from '@material/dialog'
import {MDCTextFieldHelperText} from '@material/textfield/helper-text'
import $ from 'jquery'

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

window.station_suggest_init = function () {
    $.get('station_list', function (data) {
        window.station_list = []
        data.split('\n').forEach(function (value) {
            station_list.push(value.split(' '))
        })
        console.log('full list')
    })
    /*
    $.get('level0_station_list', function (data) {
        window.level0_station_list = []
        data.split('\n').forEach(function (value) {
            level0_station_list.add(value.split(' '))
        })
        console.log('level0')
    })
    $.get('level1_station_list', function (data) {
        window.level1_station_list = []
        data.split('\n').forEach(function (value) {
            level1_station_list.add(value.split(' '))
        })
        console.log('level1')
    })
    */
    window.station_suggest_dialog = new MDCDialog(document.getElementById('station-suggest-dialog'))
    window.exsit_station_suggest_button = []
    for (const item in ['chinese-button', 'full-spell-button', 'simple-spell-button', 'level0-button', 'level1-button'])
        for (var i = 0; i < 5; i++) {
            exsit_station_suggest_button.add(new MDCRipple(document.getElementById(item + '__' + i)))
            document.getElementById(item + '__' + i).classList.add('hidden')
        }
    station_suggest_dialog.listen('MDCDialog:opened', function () {
        exsit_station_suggest_button.forEach(function (value) {
            value.layout()
        })
    })
    window.open_station_suggest = function (station_suggest_target_) {
        station_suggest_dialog.open()
        window.station_suggest_target = station_suggest_target_
    }
    window.suggest_station = function () {
        const keyword = document.getElementById('station-suggest-input').value;
        document.getElementById('chinese-button').classList.remove('hidden')
        var cnt
        var i
        cnt = 0
        for (const item in station_list)
            if (item[0].indexOf(keyword) >= 0) {
                document.getElementById('chinese-button__' + cnt).value = item[0]
                document.getElementById('chinese-button__' + cnt).classList.remove('hidden')
                cnt++
                if (cnt >= 5)
                    break
            }
        for (i = cnt; i < 5; i++) document.getElementById('chinese-button__' + cnt).classList.add('hidden')
        if (cnt == 0) document.getElementById('chinese-button').classList.add('hidden')
        document.getElementById('full-spell-button').classList.remove('hidden')
        cnt = 0
        for (const item in station_list)
            if (item[1] === keyword) {
                document.getElementById('full-spell-button__' + cnt).value = item[0]
                document.getElementById('full-spell-button__' + cnt).classList.remove('hidden')
                cnt++
                if (cnt >= 5)
                    break
            }
        if (cnt < 5) for (const item in station_list)
            if (item[1].startsWith(keyword)) {
                document.getElementById('full-spell-button__' + cnt).value = item[0]
                document.getElementById('full-spell-button__' + cnt).classList.remove('hidden')
                cnt++
                if (cnt >= 5)
                    break
            }
        for (i = cnt; i < 5; i++) document.getElementById('full-spell-button__' + cnt).classList.add('hidden')
        if (cnt == 0) document.getElementById('full-spell-button').classList.add('hidden')
        document.getElementById('simple-spell-button').classList.remove('hidden')
        cnt = 0
        for (const item in station_list)
            if (item[1] === keyword) {
                document.getElementById('simple-spell-button__' + cnt).value = item[0]
                document.getElementById('simple-spell-button__' + cnt).classList.remove('hidden')
                cnt++
                if (cnt >= 5)
                    break
            }
        if (cnt < 5) for (const item in station_list)
            if (item[1].startsWith(keyword)) {
                document.getElementById('simple-spell-button__' + cnt).value = item[0]
                document.getElementById('simple-spell-button__' + cnt).classList.remove('hidden')
                cnt++
                if (cnt >= 5)
                    break
            }
        for (i = cnt; i < 5; i++) document.getElementById('simple-spell-button__' + cnt).classList.add('hidden')
        if (cnt == 0) document.getElementById('simple-spell-button').classList.add('hidden')
    }
}

window.verify_init = function () {
    window.verify_dialog = new MDCDialog(document.getElementById('verify-dialog'))
    const text_field = new MDCTextField(document.getElementById('verify_password-text-field'))
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