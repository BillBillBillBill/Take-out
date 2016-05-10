var gulp = require('gulp');
var webpack = require('webpack-stream');
var watch = require('gulp-watch');
var batch = require('gulp-batch');
//var connect = require('gulp-connect');
var copy = require('gulp-copy');
var runSeq = require('run-sequence');
//var watch = require('gulp-watch');
var server = require('gulp-server-livereload');

// Run webpack
gulp.task('webpack', function() {
  gulp.src('src/customer/main.js')
    .pipe(webpack( require('./customer_webpack.config.js') ))
    .pipe(gulp.dest('dist/customer/js/'))
  gulp.src('src/bussiness/main.js')
    .pipe(webpack( require('./bussiness_webpack.config.js') ))
    .pipe(gulp.dest('dist/bussiness/js/'))
  gulp.src('src/admin/main.js')
    .pipe(webpack( require('./admin_webpack.config.js') ))
    .pipe(gulp.dest('dist/admin/js/'))
});

// Run the webserver
gulp.task('webserver_customer', function() {
  gulp.src('dist/customer')
    .pipe(server({
      livereload: {
        enable: true,
        port: 35729
      },
      port: 8080
    }));
});

gulp.task('webserver_bussiness', function() {
  gulp.src('dist/bussiness')
    .pipe(server({
      livereload: {
        enable: true,
        port: 35730
      },
      port: 8081
    }));
});

gulp.task('webserver_admin', function() {
  gulp.src('dist/admin')
    .pipe(server({
      livereload: {
        enable: true,
        port: 35731
      },
      port: 8082
    }));
});

// Copy index.html file
gulp.task('build.index', function() {
  gulp.src('src/customer/index.html')
    .pipe(gulp.dest('dist/customer/'));
  gulp.src('src/bussiness/index.html')
    .pipe(gulp.dest('dist/bussiness/'));
  gulp.src('src/admin/index.html')
    .pipe(gulp.dest('dist/admin/'))
});

// Copy foundation.min.js file
gulp.task('build.js', function() {
  gulp.src('node_modules/foundation-sites/dist/foundation.min.js')
    .pipe(gulp.dest('dist/customer/'));
  gulp.src('node_modules/jquery/dist/jquery.min.js')
    .pipe(gulp.dest('dist/customer'));
});

// Copy images
gulp.task('build.img', function() {
  gulp.src('src/customer/images/*.{jpg,png,gif}')
    .pipe(gulp.dest('dist/customer/images/'));
  gulp.src('src/bussiness/images/*.{jpg,png,gif}')
    .pipe(gulp.dest('dist/bussiness/images/'));
  gulp.src('src/admin/images/*.{jpg,png,gif}')
    .pipe(gulp.dest('dist/admin/images/'));
});

// Watch changes in index.html file && main.js file
gulp.task('watch', function() {
  gulp.watch(['src/**/index.html'], ['build.index']);
  gulp.watch(['src/**/main.js'], ['webpack']);
});

// Default task
gulp.task('default', function(callback) {
  runSeq(['webpack', 'build.index', 'build.js', 'build.img', 'watch'], 'webserver_customer', 'webserver_bussiness', 'webserver_admin');
});