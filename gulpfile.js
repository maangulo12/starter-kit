var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var execute     = require('child_process').exec;

gulp.task('runserver', function() {
    var proc = execute('python3 server.py');
});

gulp.task('default', ['runserver'], function() {
  browserSync.init({
    proxy: 'localhost:5000'
  });

  gulp.watch(['frontend/*.*', 'frontend/**/*.*'], browserSync.reload);
});