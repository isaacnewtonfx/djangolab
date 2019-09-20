/* global __dirname, process */
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports =  {

        context: path.join(__dirname, 'reactjs', 'src'),

        entry: {
            main: 'index',
        },
        output: {
            path: path.resolve('./reactjs/dist/'),
            publicPath: '/static/dist/',
            filename: '[name]-[chunkhash].js',
        },
        module: {
            rules: [
            {
                test: /\.js?$/i,
                exclude: /node_modules/,
                use: [
                {
                    loader: 'babel-loader',
                    options: {},  // babel-preset-env etc...
                },
                ],
            },
            {
                test: /\.css$/i,
                use: ExtractTextPlugin.extract({
                fallback: 'style-loader',
                use: 'css-loader',
                }),
            },
            {
                test: /\.s[ac]ss$/i,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'sass-loader']
                  })
              },
            {
                test: /\.(png|woff|woff2|svg|eot|ttf|gif|jpe?g)$/,
                use: [
                {
                    loader: 'url-loader',
                    options: {
                    limit: 1000,
                    name: '[path][name].[md5:hash:hex:12].[ext]',
                    },
                },
                ],
            },
            ],
        },
        resolve: {
            extensions: ['.js', '.jsx'],
            modules: ['reactjs/src/', 'node_modules'],
            alias: {},
        },
        plugins: [
            new CleanWebpackPlugin(),
            new ExtractTextPlugin({
                filename: '[name]-[md5:contenthash:hex:20].css',
                allChunks: true,
            }),
            new BundleTracker({
                filename: './webpack-stats-prod.json',
            }),
            new webpack.HashedModuleIdsPlugin(),
        ],
    }