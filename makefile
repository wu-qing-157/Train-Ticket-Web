all: static/login-bundle.js static/login-bundle.css static/register-bundle.js static/register-bundle.css static/main_page-bundle.js static/main_page-bundle.css static/account-bundle.js static/account-bundle.css

static/login-bundle.js static/login-bundle.css: nodejs/login/app.js nodejs/login/app.scss
	(cd nodejs/login && npm run build)
	cp nodejs/login/login-bundle.* static

static/register-bundle.js static/register-bundle.css: nodejs/register/app.js nodejs/register/app.scss
	(cd nodejs/register && npm run build)
	cp nodejs/register/register-bundle.* static

static/main_page-bundle.js static/main_page-bundle.css: nodejs/main_page/app.js nodejs/main_page/app.scss
	(cd nodejs/main_page && npm run build)
	cp nodejs/main_page/main_page-bundle.* static

static/account-bundle.js static/account-bundle.css: nodejs/account/app.js nodejs/account/app.scss
	(cd nodejs/account && npm run build)
	cp nodejs/account/account-bundle.* static
