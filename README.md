# Привествую это RPL
**RPL** - *это Язык Программирования Романа (Roman's Programing language).*
Очень простой и пока-что есть простые функции...

## Команды RPL
**load** <имя файла без расширения>
*Команда загружает data-файл из выбраной дериктории или в локальной
Этот файл содержит сохранёные переменые и библеотеки*

**save** <имя файла без расширения>
*Команда сохроняет data-файл в выбраную дерикторию или в локальную
Этот файл содержит сохранёные переменые и библеотеки*

**text** 'Любой текст';
*Выводит текст в консоль
в одну строку*

**textln** 'Любой текст';
*Выводит текст в консоль
в столбик*

**vartext** <имя переменой>;
*Выводит переменую из data
в одну строку*

**vartextln** <имя переменой>;
*Выводит переменую из data
в столбик*

**dirdata**
*Выводит data*

**cwin**
*Очищает консоль*

**cdata**
*Очищает data*

**varstr** <имя переменой>=Любой текст;
*Создаёт строчную переменую и загружает в data*

**varint** <имя переменой>=<Любое челочисловое значение>;
*Создаёт челочисловую переменую и загружает в data*

**varfloat** <имя переменой>=<Любое нечелочисловое значение>;
*Создаёт нечелочисловую переменую и загружает в data*

**del** <имя переменой>;
*Удаляет переменую из data*

**sleep** <число(чельное или нечельное) или имя переменой>;
*Программа запывает на указаный промежуток времени*

**exit**
*Закрытие программы*