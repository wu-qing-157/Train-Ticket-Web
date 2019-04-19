static/login-bundle.js static/login-bundle.css: nodejs/login/app.js nodejs/login/app.scss
    (cd nodejs/login && npm run build)
    cp nodejs/login/login-bundle.* .

static/register-bundle.js static/register-bundle.css: nodejs/register/app.js nodejs/register/app.scss
    (cd nodejs/register && npm run build)
    cp nodejs/register/register-bundle.* .

