var webpack = require('webpack')

module.exports =  {
  devtool: 'cheap-module-eval-source-map',
  entry: [
    './src/admin/main.js'
  ],
  output: {
    path: "/dist/admin/js",   // 打包输出的路径
    publicPath: "/dist/admin/",   // html引用路径
    filename: "app.js"    // 打包后的名字
  },
  watch: true,
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        // excluding some local linked packages.
        // for normal use cases only node_modules is needed.
        exclude: /node_modules|vue\/src|vue-router\//,
        loader: 'babel'
        /*query: {
          presets: ['es2015'],  // 转码规则es2015
          // the 'transform-runtime' plugin tells babel to require the runtime
          // instead of inlining it.
          plugins: ['transform-runtime'],
          // read from the cache to avoid needing to run the potentially expensive
          // Babel recompilation process on each run.
          cacheDirectory: true
        }*/
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
        test: /\.jpg$/,
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
