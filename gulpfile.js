var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var sass        = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('sass', function() {
    return gulp.src(['blog/blog/static/scss/bootstrap.scss',
                     'blog/blog/static/scss/style.scss'])
        .pipe(sass({
			includePaths: ['node_modules/bootstrap/scss']
		}))
        .pipe(autoprefixer({
            browsers: ['defaults'],
            cascade: false
        }))
        .pipe(gulp.dest('blog/blog/static/css'))
        .pipe(browserSync.stream());
});

gulp.task('js', function() {
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js',
                     'node_modules/jquery/dist/jquery.min.js'])
        .pipe(gulp.dest("blog/blog/static/js/lib"))
        .pipe(browserSync.stream());
});

gulp.task('watch', ['sass'], function() {
    gulp.watch(['blog/blog/static/scss/*.scss'], ['sass']);
});


gulp.task('default', ['sass', 'js', 'watch']);
