var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var sass        = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('sass', function() {
    return gulp.src(['willmill/static/scss/bootstrap.scss',
                     'willmill/static/scss/style.scss'])
        .pipe(sass({
			includePaths: ['node_modules/bootstrap/scss']
		}))
        .pipe(autoprefixer({
            browsers: ['defaults'],
            cascade: false
        }))
        .pipe(gulp.dest('willmill/static/css'))
        .pipe(browserSync.stream());
});

gulp.task('js', function() {
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js',
                     'node_modules/jquery/dist/jquery.min.js',
                     'node_modules/popper.js/dist/umd/popper.min.js'])
        .pipe(gulp.dest("willmill/static/js/lib"))
        .pipe(browserSync.stream());
});

gulp.task('watch', ['sass'], function() {
    gulp.watch(['willmill/static/scss/*.scss'], ['sass']);
});


gulp.task('default', ['sass', 'js', 'watch']);
