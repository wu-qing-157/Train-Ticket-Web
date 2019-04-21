import {MDCTopAppBar} from '@material/top-app-bar/index';
import {MDCDrawer} from "@material/drawer";
import {MDCTextField} from '@material/textfield'
import {MDCRipple} from '@material/ripple/index';

window.account_init = function() {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', () => {
        window.drawer.open = !window.drawer.open;
    });
    new MDCTextField(document.querySelector('.id'));
    new MDCTextField(document.querySelector('.old-password'));
    new MDCTextField(document.querySelector('.name'));
    new MDCTextField(document.querySelector('.email'));
    new MDCTextField(document.querySelector('.phone'));
    new MDCTextField(document.querySelector('.new-password'));
    new MDCTextField(document.querySelector('.new-password-repeat'));
    new MDCRipple(document.querySelector('.modify-button'));
    new MDCRipple(document.querySelector('.modify-reset-button'));
};