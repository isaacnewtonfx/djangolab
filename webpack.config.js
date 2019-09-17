/* global __dirname, process */
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const { CleanWebpackPlugin } = require('clean-webpack-plugin')


module.exports = (env, argv) => {

    return {

        watch : argv.mode == "development" ? true : false,

        context: path.join(__dirname, 'react', 'src'),

        entry: {
            main: 'index',
        },
        output: {
            path: path.resolve('./react/dist/'),
            publicPath: '/static/dist/',
            filename: '[name]-[chunkhash].js',
        },
        module: {
            rules: [
            {
                test: /\.js?$/,
                exclude: /node_modules/,
                use: [
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
                    // ManifestStaticFilesStorage reuse.
                    name: '[path][name].[md5:hash:hex:12].[ext]',
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
            new CleanWebpackPlugin(),
            new ExtractTextPlugin({
                filename: '[name]-[md5:contenthash:hex:20].css',
                allChunks: true,
            }),
            new BundleTracker({
                filename: './webpack-stats.json',
            }),
            new webpack.HashedModuleIdsPlugin(),
        ],
    }

}