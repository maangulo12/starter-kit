var gulp        = require('gulp');
var execute     = require('child_process').exec;
var browserSync = require('browser-sync').create();
var tsc         = require('gulp-typescript');
var tscConfig   = require('./tsconfig.json');

// Run the server
gulp.task('runserver', function() {
    var proc = execute('python3 server.py');
    // For non-linux, use this
    // var proc = execute('python server.py');
});

// Compile the typescript files
gulp.task('ts-compile', function() {
  return gulp
    .src('frontend/src/**/*.ts')
    .pipe(tsc(tscConfig.compilerOptions))
    .pipe(gulp.dest('frontend/www/build'));
});

// Copy the HTML templates
gulp.task('cp-templates', function () {
    return gulp
      .src('frontend/src/**/*.html')
      .pipe(gulp.dest('frontend/www/build'));
});

// Default run command
gulp.task('default', ['runserver', 'cp-templates', 'ts-compile'], function() {
  browserSync.init({ proxy: 'localhost:5000' });

  // Watchers
  gulp.watch(['frontend/src/**/*.html'], ['cp-templates']);
  gulp.watch(['frontend/src/**/*.ts'], ['ts-compile']);
  gulp.watch(['frontend/**/*.*'], browserSync.reload);
});