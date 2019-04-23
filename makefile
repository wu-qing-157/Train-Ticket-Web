all: static/mdc-bundle.css static/mdc-bundle.js

static/mdc-bundle.css static/mdc-bundle.js: nodejs/mdc/app.scss nodejs/mdc/app.js
	(cd nodejs/mdc && npm run build)
	cp nodejs/mdc/mdc-bundle.* static
