window.new_menu_item = function (name) {
    const new_item = document.createElement('li');
    new_item.setAttribute('role', 'menuitem');
    new_item.setAttribute('tabindex', '-1');
    new_item.classList.add('mdc-list-item');
    new_item.innerHTML = '<span class="mdc-list-item__text">' + name + '</span>';
    return new_item;
};

window.level0 = [];
window.level1 = [];
window.level2 = [];
window.station_suggest_init_cnt = 0;

window.station_suggest_init = function () {
    if (station_suggest_init_cnt === 2) return;
    window.station_suggest_init_cnt = 0;
    const http0 = new XMLHttpRequest();
    http0.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let ret = this.responseText;
            if (ret.charAt(ret.length - 1) === '\n')
                ret = ret.substring(0, ret.length - 1);
            ret.split('\n').forEach(function (value) {
                level0.push(value.split(' '))
            });
            station_suggest_init_cnt++
        }
    };
    http0.open('GET', 'station_list_0', true);
    http0.send();
    const http2 = new XMLHttpRequest();
    http2.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let ret = this.responseText;
            if (ret.charAt(ret.length - 1) === '\n')
                ret = ret.substring(0, ret.length - 1);
            ret.split('\n').forEach(function (value) {
                level2.push(value.split(' '))
            });
            station_suggest_init_cnt++
        }
    };
    http2.open('GET', 'station_list_2', true);
    http2.send()
};

function add_station_suggest(keyword, input, inputDOM, menu, menuDOM) {
    const menu_item_max = 15;
    let cnt = 0;
    let i;
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) >= 0) {
            menuDOM.appendChild(new_menu_item(level0[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && level0[i][1].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level0[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && !(level0[i][1].startsWith(keyword)) && level0[i][2].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level0[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) >= 0) {
            menuDOM.appendChild(new_menu_item(level2[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && level2[i][1].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level2[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && !(level2[i][1].startsWith(keyword)) && level2[i][2].startsWith(keyword)) {
            menuDOM.appendChild(new_menu_item(level2[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level0.length; i++)
        if (level0[i][0].indexOf(keyword) < 0 && level0[i][1].indexOf(keyword) > 0 && level0[i][2].indexOf(keyword) < 0) {
            menuDOM.appendChild(new_menu_item(level0[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    for (i = 0; i < level2.length; i++)
        if (level2[i][0].indexOf(keyword) < 0 && level2[i][1].indexOf(keyword) > 0 && level2[i][2].indexOf(keyword) < 0) {
            menuDOM.appendChild(new_menu_item(level2[i][0]));
            cnt++;
            if (cnt === menu_item_max) return
        }
    if (cnt === 0) {
        const new_item = new_menu_item('没有建议');
        new_item.classList.add('mdc-list-item--disabled');
        new_item.onclick = function () {
        };
        menuDOM.appendChild(new_item)
    }
}

window.update_station_suggest = function (input, inputDOM, menu, menuDOM) {
    const keyword = input.value.toLowerCase();
    menuDOM.innerHTML = '';
    add_station_suggest(keyword, input, inputDOM, menu, menuDOM);
    menu.setDefaultFocusState(0);
    menu.initialize();
    menu.listen('MDCMenu:selected', function (event) {
        input.value = event.detail.item.firstChild.innerText;
        inputDOM.oninput(null);
        document.body.focus()
    });
    menu.open = true
};