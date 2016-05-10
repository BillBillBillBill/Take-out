var webpack = require('webpack')

module.exports =  {
  devtool: 'cheap-module-eval-source-map',
  entry: [
    './src/bussiness/main.js'
  ],
  output: {
    path: "/dist/bussiness/js",
    publicPath: "/dist/bussiness/",
    filename: "app.js"
  },
  watch: true,
  module: {
    loaders: [
      {
        test: /\.js$/,
        // excluding some local linked packages.
        // for normal use cases only node_modules is needed.
        exclude: /node_modules|vue\/src|vue-router\//,
        loader: 'babel'
      },
      {
        test: /\.scss$/,
        loaders: ['style', 'css', 'sass']
      },
      {
        test: /\.css$/,
        loaders: ['style', 'css']
      },
      {
        test: /\.vue$/,
        loader: 'vue'
      },
      {
        test:/\.jpg$/,
        loader: 'url-loader',
        query: {mimetype: 'image/jpg'}
      }
    ]
  },
  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime']
  },
  resolve: {
    modulesDirectories: ['node_modules']
  },
  debug: true
}
