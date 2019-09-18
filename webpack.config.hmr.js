/* global __dirname, process */
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const { CleanWebpackPlugin } = require('clean-webpack-plugin')


module.exports = {

  
        watch : true,
        mode : "development",
        context: path.join(__dirname, 'react', 'src'),

        entry: [
            'webpack-dev-server/client?http://127.0.0.1:3000',
            'webpack/hot/only-dev-server',
            'index'
        ],
        output: {
            path: path.resolve('./react/dist/'),            
            filename: '[name]-[hash].js',
            publicPath: 'http://127.0.0.1:3000/react/dist/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name

        },
        module: {
            rules: [
            {
                test: /\.js?$/,
                exclude: /node_modules/,
                use: [
                    {
                        loader: 'react-hot-loader/webpack',
                        options: {}
                    },
                    {
                        loader: 'babel-loader',
                        options: {},  // babel-preset-env etc...
                    },
                ],
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                fallback: 'style-loader',
                use: 'css-loader',
                }),
            },
            {
                test: /\.(png|woff|woff2|svg|eot|ttf|gif|jpe?g)$/,
                use: [
                {
                    loader: 'url-loader',
                    options: {
                    limit: 1000,
                    name: '[path][name].[hash].[ext]',
                    },
                },
                ],
            },
            ],
        },
        resolve: {
            extensions: ['.js', '.jsx'],
            modules: ['react/src/', 'node_modules'],
            alias: {},
        },
        plugins: [
            new webpack.HotModuleReplacementPlugin(),
            new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
            new CleanWebpackPlugin(),
            new ExtractTextPlugin({
                filename: '[name]-[hash].css',
                allChunks: true,
            }),
            new BundleTracker({
                filename: './webpack-stats.json',
            }),
            new webpack.HashedModuleIdsPlugin(),
        ],

        devServer: {
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
              "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
            },
            disableHostCheck: true
          }
    

}