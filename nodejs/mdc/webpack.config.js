const autoprefixer = require('autoprefixer');

module.exports = [{
    entry: ['./app.scss', './account.jsx', './account_manage.jsx', './base.jsx', './login.jsx', './main_page.jsx',
        './mdc_initialize.jsx', './order.jsx', './order_confirm.jsx', './register.jsx', './station_suggest.js',
        './train_manage.jsx'],
    output: {
        filename: 'mdc-bundle.js'
    },
    performance: {
        maxEntrypointSize: 1048576,
        maxAssetSize: 1048576
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
                test: /\.(js|jsx)$/,
                loader: 'babel-loader',
                query: {
                    presets: ['env', 'react']
                }
            }
        ]
    }
}];
