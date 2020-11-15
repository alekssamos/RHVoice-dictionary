RHVoice-dictionary
==================

Словарь в формате поддерживаемом [RHVoice](https://github.com/Olga-Yakovleva/RHVoice) v0.5+

## Установка словаря
Я сделал реструктурезацию,
> теперь в репозитории лежит прямо папка которую можно скопировать по пути  `rhvoice` или `rhvoice_config`,
> Не нужно руками создавать папки `dicts` и `Russian`, Можно добавлять не только русские.

### LINUX
* скопировать папку `dicts` в `/etc/RHVoice/`

### WINDOWS
* `%AppData%\RHVoice\`

### NVDA
* Установочная версия: `%AppData%\nvda\RHVoice-config\`
* Переносная версия: `.\userConfig\RHVoice-config\`

### ANDROID
*  `/sdcard/Android/data/com.github.olga_yakovleva.rhvoice.android/files/`

Примечание: После добавления словарей синтезатор необходимо перезагрузить (закрыть все программы, которые его используют), чтобы новые словари начали действовать.

## Дополнительные инструменты

Более подробное описание инструментов "[/tools](https://github.com/vantu5z/RHVoice-dictionary/tree/master/tools)"

* ### Предварительная обработка текста
    * Ведётся разработка предварительной обработки текста на Питоне "[/tools/preprocessing](https://github.com/vantu5z/RHVoice-dictionary/tree/master/tools/preprocessing)".

* ### Скрипты на Питоне
    * Вспомогательые скрипты.
    * Воспроизведение с помощью `rhvoice_say`.
    * GUI для настройки `rhvoice_say`: `rhvoice_config`.

## Обратная связь
Замечания, предложения, исправления и дополнения всегда приветствуются! <br>
Их можно оставить во вкладке [Issues](https://github.com/vantu5z/RHVoice-dictionary/issues).
