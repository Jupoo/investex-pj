//Подключаем библиотеки
var gulp            = require('gulp'), // Подключаем Gulp
    extender        = require('gulp-html-extend'), //Подключаем html Extend
    sass            = require('gulp-sass'), //Подключаем Sass пакет
    autoprefixer    = require('gulp-autoprefixer'),// Подключаем библиотеку для автоматического добавления префиксов
    browserSync     = require('browser-sync'), // Подключаем Browser Sync - Автоматическое обновление страниц по сохранению файлов
    concat          = require('gulp-concat'), // Подключаем gulp-concat (для конкатенации файлов)
    uglify          = require('gulp-uglifyjs'), // Подключаем gulp-uglifyjs (для сжатия JS)
    cssnano         = require('gulp-cssnano'), // Подключаем пакет для минификации CSS
    rename          = require('gulp-rename'), // Подключаем библиотеку для переименования файлов
    del             = require('del'), // Подключаем библиотеку для удаления файлов и папок
    imagemin        = require('gulp-imagemin'), // Подключаем библиотеку для работы с изображениями
    pngquant        = require('imagemin-pngquant'); // Подключаем библиотеку для работы с png
    spritesmith     = require('gulp.spritesmith'); // Подключаем библиотеку для сборки sprite из картинок
    reload          = browserSync.reload;
   


gulp.task('browser-sync', function() { // Создаем таск browser-sync (Автоматическое обновление страниц по сохранению файлов)
    browserSync({ // Выполняем browser Sync
        server: { // Определяем параметры сервера
            baseDir: 'src' // Директория для сервера - src
        },
        notify: false // Отключаем уведомления
    });
});


// Инклуды (включения) в html-верстку
gulp.task('html-extend', function () {
    return gulp.src('src/template/*.html')   // Берем все html файлы из папки template (из корня)
        .pipe(extender({annotations:true, verbose:false})) // Собираем html-файлы
        .pipe(gulp.dest('src'))  //выгружаем в src
        .pipe(reload({stream: true})); // Перезагружаем страницу
});


gulp.task('scss', function() { // Создаем таск scss
    return gulp.src('src/scss/**/*.scss') // Берем все sass файлы из папки sass и дочерних, если таковые будут
        .pipe(sass()) // Преобразуем Sass в CSS посредством gulp-sass
        .pipe(autoprefixer(['last 15 versions', '> 1%', 'ie 8', 'ie 7'], { cascade: true })) // Создаем префиксы
        .pipe(cssnano()) // Сжимаем
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('src/css')) // Выгружаем результат в папку src/css
        .pipe(reload({stream: true})); // Перезагружаем страницу
});


//Сжатие стилей библиотек
gulp.task('css-libs', ['scss'], function() {
    return gulp.src('src/css/libs.css') // Выбираем файл для минификации
        .pipe(cssnano()) // Сжимаем
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('src/css')); // Выгружаем в папку src/css
});


//Сборка и сжатие всех библиотек (перед watch)
gulp.task('scripts', function() {
    return gulp.src([ // Берем все необходимые библиотеки
        'src/libs/jquery/dist/jquery.min.js', // Берем jQuery
        'src/libs/slick/slick.min.js' // Берем Slick
        ])
        .pipe(concat('libs.min.js')) // Собираем их в кучу в новом файле libs.min.js
        .pipe(uglify()) // Сжимаем JS файл
        .pipe(gulp.dest('src/js')) // Выгружаем в папку src/js
        .pipe(reload({stream: true})); // Перезагружаем страницу
});


//Сборка и сжатие всех пользовательских js-файлов
gulp.task('scripts-custom', function() { // Создаем таск scripts-custom
    return gulp.src('src/js/partials/*.js') // Берем все js файлы из папки js/partials
        .pipe(concat('scripts.min.js')) // Собираем их в кучу в новом файле scripts.min.js
        .pipe(uglify()) // Сжимаем JS файл
        .pipe(gulp.dest('src/js')) // Выгружаем результат в папку src/css
        .pipe(reload({stream: true})); // Перезагружаем страницу
});

//Оптимизация изображений
gulp.task('img', function() {
    return gulp.src(['!src/img/sprite/**/*', 'src/img/**/*+(jpg|jpeg|png|gif|svg|JPG|JPEG|PNG|GIF|SVG)']) // Берем все изображения из src
        .pipe(imagemin({ // Сжимаем их с наилучшими настройками
            //optimizationLevel: 3,
            interlaced: true,
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        //.pipe(gulp.dest('build/img')); // Выгружаем на продакшен
});


//Sprite для иконок @2x
gulp.task('sprite', function() {
    var spriteData = 
        gulp.src('src/img/sprite/*.*') // путь, откуда берем картинки для спрайта
            .pipe(spritesmith({
                retinaSrcFilter: ['src/img/sprite/*@2x.*'],//берем картинки с названием @2x на конце для ретины
                imgName: 'sprite.png',//имя спрайта
                retinaImgName: 'sprite@2x.png',//имя спрайта для ретины
                cssName: '_sprite.scss',
                cssFormat: 'scss',
                algorithm: 'binary-tree',
                cssTemplate: 'scss.template.mustache',
                cssVarMap: function(sprite) {
                    sprite.name = 'SPRITE__' + sprite.name
                }
            }));

    spriteData.img.pipe(gulp.dest('src/img/')); // путь, куда сохраняем картинку
    spriteData.css.pipe(gulp.dest('src/scss/')); // путь, куда сохраняем стили
});



//Очищаем папку build
gulp.task('clean', function() {
    return del.sync('build'); // Удаляем папку build перед сборкой
});

//Очищаем папку build
gulp.task('clean-html', function() {
    return del.sync('src/*.html'); // Удаляем все html из корня src
});


//Cборка в папку build - продакшен
gulp.task('build', ['clean', 'clean-html', 'sprite', 'img', 'css-libs', 'scripts', 'scripts-custom', 'html-extend'], function() {
    var buildCss = gulp.src([ // Переносим CSS стили в продакшен
        'src/css/main.min.css',
        'src/css/libs.min.css'
        ])
    .pipe(gulp.dest('build/css'))

    var buildFonts = gulp.src('src/fonts/**/*') // Переносим шрифты в продакшен
    .pipe(gulp.dest('build/fonts'))

    var buildJs = gulp.src('src/js/*.js') // Переносим скрипты JS в продакшен
    .pipe(gulp.dest('build/js'))

    // var buildHtml = gulp.src('src/*.html') // Переносим HTML в продакшен
    // .pipe(gulp.dest('build'));
});


//СЛЕДИМ
gulp.task('watch', ['browser-sync', 'html-extend', 'sprite', 'css-libs', 'scripts', 'scripts-custom'], function() {
    gulp.watch('src/scss/**/*.scss', ['css-libs']); // Наблюдение за sass файлами в папке scss
    gulp.watch('src/template/**/*.html', ['html-extend']);   // Наблюдение за HTML файлами в папке template
    gulp.watch('src/js/partials/**/*.js', ['scripts-custom']);   // Наблюдение за пользовательскими JS файлами в папке js/partials
    gulp.watch('src/img/sprite/*.*', ['sprite']);   // Наблюдение за IMG файлами в папке img
});


gulp.task('default', ['watch']);


//  ИТОГО:
//  gulp - запускает watch-TASK | Отслеживание файлов и сборка в папку src
//  gulp build - запускает build-TASK | Cборка конечного варианта в папку build