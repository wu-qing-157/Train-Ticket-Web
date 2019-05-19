import {MDCTopAppBar} from "@material/top-app-bar/component";
import {MDCDrawer} from "@material/drawer/component";
import {MDCRipple} from "@material/ripple/component";

window.main_page_init = function () {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', function () {
        window.drawer.open = !window.drawer.open
    });
    const refresh_button = new MDCRipple(document.getElementById('refresh'));
    refresh_button.unbounded = true;
};