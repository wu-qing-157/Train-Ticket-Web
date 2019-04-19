import {MDCTopAppBar} from '@material/top-app-bar/index';
import {MDCDrawer} from "@material/drawer";

window.main_page_init = function() {
    const appBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
    appBar.setScrollTarget(document.getElementById('main-content'));
    window.drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
    appBar.listen('MDCTopAppBar:nav', () => {
        window.drawer.open = !window.drawer.open;
    });
};

// new MDCRipple(document.querySelector('.foo-button'));
// new MDCFloatingLabel(document.querySelector('.mdc-floating-label'));
// new MDCLineRipple(document.querySelector('.mdc-line-ripple'));