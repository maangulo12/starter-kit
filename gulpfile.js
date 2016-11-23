'use strict';

var gulp        = require('gulp');
var execute     = require('child_process').exec;
var sass        = require('gulp-sass');
var concat      = require('gulp-concat');
var tsc         = require('gulp-typescript');
var tscConfig   = require('./tsconfig.json');
var browserSync = require('browser-sync').create();

// Run the server
gulp.task('runserver', function() {
  var proc = execute('python3 server.py');
  // For non-linux, use this
  // var proc = execute('python server.py');
});

// Copy the HTML templates
gulp.task('html-copy', function() {
  return gulp
    .src('frontend/src/**/*.html')
    .pipe(gulp.dest('frontend/www/build'));
});

// Compile the SASS files 
gulp.task('sass-compile', function() {
  return gulp
    .src('frontend/src/**/*.scss')
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(concat('all.min.css'))
    .pipe(gulp.dest('frontend/www/build'));
});

// Compile the TypeScript files
gulp.task('ts-compile', function() {
  return gulp
    .src('frontend/src/**/*.ts')
    .pipe(tsc(tscConfig.compilerOptions))
    .pipe(gulp.dest('frontend/www/build'));
});

// Default run command
gulp.task('default', ['runserver', 'html-copy', 'sass-compile', 'ts-compile'], function() {
  browserSync.init({ proxy: 'localhost:5000' });

  // Watchers
  gulp.watch('frontend/src/**/*.html', ['html-copy']);
  gulp.watch('frontend/src/**/*.scss', ['sass-compile']);
  gulp.watch('frontend/src/**/*.ts',   ['ts-compile']);
  gulp.watch('frontend/**/*.*', browserSync.reload);
});