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

// Copy js file
gulp.task('build.js', function() {
  gulp.src('src/customer/foundation.min.js')
    .pipe(gulp.dest('dist/customer/js'));
  gulp.src('src/customer/jquery.min.js')
    .pipe(gulp.dest('dist/customer/js'));
  gulp.src('src/bussiness/foundation.min.js')
    .pipe(gulp.dest('dist/bussiness/js'));
  gulp.src('src/bussiness/jquery.min.js')
    .pipe(gulp.dest('dist/bussiness/js'));
  gulp.src('src/bussiness/lrz.bundle.js')
    .pipe(gulp.dest('dist/bussiness/js'));
  gulp.src('src/admin/foundation.min.js')
    .pipe(gulp.dest('dist/admin/js'));
  gulp.src('src/admin/jquery.min.js')
    .pipe(gulp.dest('dist/admin/js'));
  gulp.src('src/admin/lrz.bundle.js')
    .pipe(gulp.dest('dist/admin/js'));
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

// Copy css file
gulp.task('build.css', function() {
  gulp.src('src/customer/foundation.min.css')
    .pipe(gulp.dest('dist/customer/css'));
  gulp.src('src/bussiness/foundation.min.css')
    .pipe(gulp.dest('dist/bussiness/css'));
  gulp.src('src/admin/foundation.min.css')
    .pipe(gulp.dest('dist/admin/css'));
});

// Copy foundation.icons
gulp.task('build.icons', function() {
	gulp.src('src/customer/foundation-icons/*')
	  .pipe(gulp.dest('dist/customer/foundation-icons/'));
	gulp.src('src/bussiness/foundation-icons/*')
	  .pipe(gulp.dest('dist/bussiness/foundation-icons'));
	gulp.src('src/admin/foundation-icons/*')
	  .pipe(gulp.dest('dist/admin/foundation-icons'));
});

// Watch changes in index.html file && main.js file
gulp.task('watch', function() {
  gulp.watch(['src/**/index.html'], ['build.index']);
  gulp.watch(['src/**/main.js'], ['webpack']);
});

// Default task
gulp.task('default', function(callback) {
  runSeq(['webpack', 'build.index', 'build.js', 'build.img', 'build.css', 'build.icons', 'watch'], 'webserver_customer', 'webserver_bussiness', 'webserver_admin');
});