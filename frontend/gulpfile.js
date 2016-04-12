var gulp = require('gulp');
var webpack = require('webpack-stream');
var watch = require('gulp-watch');
var batch = require('gulp-batch');
var connect = require('gulp-connect');
var copy = require('gulp-copy');
var runSeq = require('run-sequence');

// Run webpack
gulp.task('webpack', function(){
  gulp.src('src/customer/main.js')
    .pipe(webpack( require('./customer_webpack.config.js') ))
    .pipe(gulp.dest('dist/customer/js/'))
    .pipe(connect.reload());
  gulp.src('src/bussiness/main.js')
    .pipe(webpack( require('./bussiness_webpack.config.js') ))
    .pipe(gulp.dest('dist/bussiness/js/'))
    .pipe(connect.reload());
  gulp.src('src/admin/main.js')
    .pipe(webpack( require('./admin_webpack.config.js') ))
    .pipe(gulp.dest('dist/admin/js/'))
    .pipe(connect.reload());
});

// Run the webserver
gulp.task('webserver_customer', function() {
  connect.server({
    port: 8080,
    livereload: {port: 35750},
    root: 'dist/customer'
  });
});

gulp.task('webserver_bussiness', function() {
  connect.server({
    port: 8081,
    livereload: {port: 35751},
    root: 'dist/bussiness'
  });
});

gulp.task('webserver_admin', function() {
  connect.server({
    port: 8082,
    livereload: {port: 35752},
    root: 'dist/admin'
  });
});

// Copy index.html file
gulp.task('build.index', function(){
  gulp.src('./src/customer/index.html')
    .pipe(gulp.dest('./dist/customer/'));
  gulp.src('./src/bussiness/index.html')
    .pipe(gulp.dest('./dist/bussiness/'));
  gulp.src('./src/admin/index.html')
    .pipe(gulp.dest('./dist/admin/'));
});

// Default task
gulp.task('default', function(callback) {
    runSeq('webserver_customer', 'webserver_bussiness', 'webserver_admin', ['webpack', 'build.index'], callback);
});
