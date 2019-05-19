all: static/mdc-bundle.css static/mdc-bundle.js

static/mdc-bundle.css static/mdc-bundle.js: nodejs/mdc/app.scss nodejs/mdc/*.js nodejs/mdc/*.jsx
	(cd nodejs/mdc && npm run build)
	mv nodejs/mdc/dist/mdc-bundle.* static
