const autoprefixer = require('autoprefixer');

module.exports = [{
    entry: ['./app.scss', './app.js'],
    output: {
        filename: 'mdc-bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: 'mdc-bundle.css'
                        }
                    },
                    {loader: 'extract-loader'},
                    {loader: 'css-loader'},
                    {
                        loader: 'postcss-loader',
                        options: {
                            plugins: function () {
                                return [autoprefixer()];
                            }
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {includePaths: ['./node_modules']}
                    }
                ]
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                query: {
                    presets: ['env']
                }
            }
        ]
    }
}];
