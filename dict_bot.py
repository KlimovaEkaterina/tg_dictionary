# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5339422481:AAFTnERL1SueKx8FBmcpffaT9QClacOnSrg', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
'новое слово': 'тут его определение',
'регресс': 'Проверить что новый функционал не сломал существующий',
'json': '(англ. JavaScript Object Notation — текстовый формат обмена данными, основанный на JavaScript.\n"ключ": значение\n"строка", число, null, boolean (true/false), {объект}, [массив]\nпример\n{"squadName": "Super hero squad",\n"homeTown": "Metro City",\n"formed": 2016,\n"secretBase": null,\n"active": true,\n"powers": ["Immortality", "Immunity", "Inferno"]\n}',
'деплой': '(от англ to deploy) - развертывать.',
'бэкап': '(от англ. backup – дублирование) – cоздание резервных копий данных с целью их восстановления в случае потери оригинальных данных по каким-либо причинам',
'деплой': '(от англ to deploy) - развертывать.',
'игнорить': '(от англ. to ignore) - игнорировать, пренебрегать, не придавать значения.',
'капча': '(от англ. CAPTCHA - аббревиатура от английских слов «Completely Automatic Public Turing Test to Tell Computers and Humans Apart», что означает «полностью автоматизированный публичный тест Тьюринга для различения компьютеров и людей»).',
'коммент': 'комментарий (к программе, тесту, ошибке, исправлению и др.)',
'коммит': '(от англ. commit - зд. фиксировать) - сохранение, фиксация (в архиве, репозитарии и др.) изменений в программном коде',
'лог': '(от англ. to log - зд. регистрировать в вахтенном журнале) - файл, содержащий информацию о деятельности и об успешности (и об ошибках) прохождения программы.',
'спек': '(от амер. формы англ. слова specification) - спецификация, утвержденный документ, являющийся основой для разработки компьютерной программы и для ее тестирования.',
'фидбэк': '(от англ. feedback - обратная связь) - отзыв, отклик, ответная реакция на какое-либо действие или событие',
'фиксить': '(от англ. to fix - зд. приводить в порядок; налаживать, регулировать; ремонтировать, чинить) - исправление ошибки, выявленной в процессе тестирования, путем корректировки кода программы, а также "заплатка" к программе.',
'фича': '(от англ. feature - особенность, характерная черта; деталь, признак, свойство; свойства, особенности, общий вид; информационная функция; функциональная возможность) - функциональность, функциональная возможность, характерная особенность программы.',
'порт': 'сетевой порт - это сетевой ресурс, отображаемый в виде числа (1-65535), которое определяет назначение входящих или исходящих сетевых потоков данных на заданном устройстве.\n21 - ftp - Передача файлов по сети\n22 - ssh - Шифрованный терминал удаленного доступа\n25 - SМТР - Передача почты\n80 - Протокол передачи данных HTTP\n110 - Рорз Получение почты\n443 - Протокол передачи данных HTTPS',
'bash':'команды линуксовой консоли\npwd: текущая папка\ncd: сменить папку\nls: посмотреть содержимое папки\nmkdir: создать новую папку\nmv: пареместить папку или файл\ncp: копировать файл\ntouch: создать файл (+ .расширение)\nrm: удаление файла\nrmdir: удаление пустой папки\nrm-R: удаление папки с файлами\ncat: предпросмотр содержимого файла\nvim: открыть файл в редакторе\n:wq: выйти и сохранить из редактора\n:q!: выйти из редактора без сохранения\ncat файл | grep что_искать: покажет только строки что_искать. Регистрозависимый\n',
'git': 'система управления версиями\ngit init: сделать из любой папки git папку\ngit  clone ссылка на репозиторий: скачать на компьютер репозиторий\ngit pull: спулить обновление с origin\ngit checkout-b "имя новой ветки": \ngit checkout "имя ветки на которую переключаемся": создать новую ветку\ngit add: при добавлении/удалении файлов\ngit commit-am "название нового коммита": сохраняет текущие изменения\ngit push: запушить изменения\ngit status: в какой ветке находимся\ngit log: показывает какие папки изменили\ngit merge master: вливает свежий мастер в ветку\ngit reset-hard: отменить коммит',
'github': 'хранилище для репозиториев git',
'симулятор': 'это воспроизведение работы программы-оригинала сугубо виртуально, на движке специальной программы. Симуляция лишь имитирует выполнение кода, а не копирует его, всё виртуально на 100%, всё понарошку. Основное отличие эмулятора от симулятора заключается в том, что первый копирует суть (процесс, объект) работы, а второй - лишь окружающую действительность (оболочка, свойства объекта).',
'эмулятор': 'это воспроизведение работы программы или системы (а не какой-то её мизерной части) с сохранением ключевых её свойств и принципов работы. Эмуляция выполняет программный код в привычной для этого кода среде, состоящей из тех же компонентов, что и змулируемый объект. Основное отличие эмулятора от симулятора заключается в том, что первый копирует суть (процесс, объект) работы, а второй - лишь окружающую действительность (оболочка, свойства объекта).',
'баг-репорт': 'это технический документ, который подробно описывает ошибку в работе программы, приложения или другого ПО. Его составляет тестировщик, чтобы разработчикам было понятно, что работает неправильно, насколько дефект критичен и что нужно исправить.\nАтрибуты:\n1. Заголовок(Что? Где? Когда или при каких условиях?)\n2. Описание\n3. Версия продукта(если есть)\n4. Окружение\n5. Приоритет\n6. Серьезность\n7. Предусловия(если есть)\n8. Шаги воспроизведения\n9. Фактический результат\n10. Ожидаемый результат\n11. Прикрепленные файлы',
'чек-лист': 'это список, содержащий ряд необходимых проверок во время тестирования программного продукта. Отмечая пункты списка, команда или один тестировщик могут узнать о текущем состоянии выполненной работы и о качестве продукта. Можно сказать, что чек-лист — это упрощенный тест-кейс без шагов и прочего описания. Просто список того, что необходимо проверить.',
'тест-кейс': 'это профессиональная документация тестировщика, последовательность действий направленная на проверку какого-либо функционала, описывающая как придти к фактическому результату.\nАтрибуты тест-кейса:\n1.Уникальный идентификатор тест-кейса — необходим для удобной организации хранения и навигации по нашим тест-наборам.\n2. Название — основная тема, или идея тест-кейса. Краткое описание его сути.\n3. Предусловия — описание условий, которые не имеют прямого отношения к проверяемому функционалу, но должны быть выполнены.\n4. Шаги — описание последовательности действий, которая должна привести нас к ожидаемому результату\n5. Ожидаемый результат — что мы ожидаем увидеть после выполнения шагов.',
'priority': '(приоритет, приорити) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'приорити': '(priority, приоритет) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'приоритет': '(priority, приорити) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'серьезность': '(severity, северити) это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'severity': 'это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'северити': '(severity, серьезность) это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'толстый клиент': 'это приложение, обеспечивающее (в противовес тонкому клиенту) расширенную функциональность независимо от центрального сервера. Часто сервер в этом случае является лишь хранилищем данных, а вся работа по обработке и представлению этих данных переносится на машину клиента.',   
'тонкий клиент': 'компьютер или программа-клиент, который переносит все или большую часть задач по обработке информации на сервер. Примером тонкого клиента может служить компьютер с браузером, использующийся для работы с веб-приложениями.',
'идентификация': 'процесс позволяющий однозначно определить (распознать) субъект или объект, по его идентификатору, в той или иной системе. Например, для начала система запрашивает логин, пользователь его указывает, система распознает его как существующий — это идентификация.',
'аутентификация': 'процедура проверки подлинности, например проверка подлинности пользователя путем сравнения введенного им пароля с паролем, сохраненным в базе данных.',
'авторизация': 'предоставление доступа к той или иной системе, присутствие в ней и выполнения определенных действий.\nАвторизация не просто дает возможность зайти в систему, но и разрешает совершать там определенные операции: читать документы, отправлять письма, изменять данные.',
'верификация': 'процесс просмотра документации, дизайна, кода и программы для того, чтобы проверить, было ли программное обеспечение создано в соответствии с требованиями или нет. Верификация проверяет, соответствует ли ПО спецификации, в то время как валидация проверяет, соответствует ли ПО требованиям и ожиданиям. Основная цель процесса верификации – обеспечить качество приложения, дизайна, архитектуры и т.д.\nПроцесс верификации включает в себя такие действия, как ревью, пошаговое руководство и инспекция.',
'валидация': 'динамический механизм тестирования и проверки того, действительно ли программный продукт соответствует точным потребностям заказчика или нет.\nВалидация проверяет, соответствует ли ПО требованиям и ожиданиям, в то время как верификация проверяет, соответствует ли ПО спецификации.\nЭтот процесс помогает гарантировать, что ПО выполняет желаемое использование в подходящей среде.\nПроцесс валидации включает в себя такие действия, как модульное тестирование, интеграционное тестирование, системное тестирование и пользовательское приемочное тестирование.',}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
  
       bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!\nЯ помогу тебе расшифровать сложные аббревиатуры и термины 📕\nВведи интересующий термин, например, регресс".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Список терминов ❓"):
        bot.send_message(message.chat.id, text="json\nпорт\nbash\ngit\ngithub\nбаг-репорт\nчек-лист\nтест-кейс\npriority\nприорити\nприоритет\nсерьезность\nseverity\nсеверити\nэмулятор\nсимулятор\nвалидация\nверификация\nидентификация\nаутентификация\nавторизация\nтонкий клиент\nтолстый клиент")
a# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5339422481:AAFTnERL1SueKx8FBmcpffaT9QClacOnSrg', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
'новое слово': 'тут его определение',
'регресс': 'Проверить что новый функционал не сломал существующий',
'json': '(англ. JavaScript Object Notation — текстовый формат обмена данными, основанный на JavaScript.\n"ключ": значение\n"строка", число, null, boolean (true/false), {объект}, [массив]\nпример\n{"squadName": "Super hero squad",\n"homeTown": "Metro City",\n"formed": 2016,\n"secretBase": null,\n"active": true,\n"powers": ["Immortality", "Immunity", "Inferno"]\n}',
'деплой': '(от англ to deploy) - развертывать.',
'бэкап': '(от англ. backup – дублирование) – cоздание резервных копий данных с целью их восстановления в случае потери оригинальных данных по каким-либо причинам',
'деплой': '(от англ to deploy) - развертывать.',
'игнорить': '(от англ. to ignore) - игнорировать, пренебрегать, не придавать значения.',
'капча': '(от англ. CAPTCHA - аббревиатура от английских слов «Completely Automatic Public Turing Test to Tell Computers and Humans Apart», что означает «полностью автоматизированный публичный тест Тьюринга для различения компьютеров и людей»).',
'коммент': 'комментарий (к программе, тесту, ошибке, исправлению и др.)',
'коммит': '(от англ. commit - зд. фиксировать) - сохранение, фиксация (в архиве, репозитарии и др.) изменений в программном коде',
'лог': '(от англ. to log - зд. регистрировать в вахтенном журнале) - файл, содержащий информацию о деятельности и об успешности (и об ошибках) прохождения программы.',
'спек': '(от амер. формы англ. слова specification) - спецификация, утвержденный документ, являющийся основой для разработки компьютерной программы и для ее тестирования.',
'фидбэк': '(от англ. feedback - обратная связь) - отзыв, отклик, ответная реакция на какое-либо действие или событие',
'фиксить': '(от англ. to fix - зд. приводить в порядок; налаживать, регулировать; ремонтировать, чинить) - исправление ошибки, выявленной в процессе тестирования, путем корректировки кода программы, а также "заплатка" к программе.',
'фича': '(от англ. feature - особенность, характерная черта; деталь, признак, свойство; свойства, особенности, общий вид; информационная функция; функциональная возможность) - функциональность, функциональная возможность, характерная особенность программы.',
'порт': 'сетевой порт - это сетевой ресурс, отображаемый в виде числа (1-65535), которое определяет назначение входящих или исходящих сетевых потоков данных на заданном устройстве.\n21 - ftp - Передача файлов по сети\n22 - ssh - Шифрованный терминал удаленного доступа\n25 - SМТР - Передача почты\n80 - Протокол передачи данных HTTP\n110 - Рорз Получение почты\n443 - Протокол передачи данных HTTPS',
'bash':'команды линуксовой консоли\npwd: текущая папка\ncd: сменить папку\nls: посмотреть содержимое папки\nmkdir: создать новую папку\nmv: пареместить папку или файл\ncp: копировать файл\ntouch: создать файл (+ .расширение)\nrm: удаление файла\nrmdir: удаление пустой папки\nrm-R: удаление папки с файлами\ncat: предпросмотр содержимого файла\nvim: открыть файл в редакторе\n:wq: выйти и сохранить из редактора\n:q!: выйти из редактора без сохранения\ncat файл | grep что_искать: покажет только строки что_искать. Регистрозависимый\n',
'git': 'система управления версиями\ngit init: сделать из любой папки git папку\ngit  clone ссылка на репозиторий: скачать на компьютер репозиторий\ngit pull: спулить обновление с origin\ngit checkout-b "имя новой ветки": \ngit checkout "имя ветки на которую переключаемся": создать новую ветку\ngit add: при добавлении/удалении файлов\ngit commit-am "название нового коммита": сохраняет текущие изменения\ngit push: запушить изменения\ngit status: в какой ветке находимся\ngit log: показывает какие папки изменили\ngit merge master: вливает свежий мастер в ветку\ngit reset-hard: отменить коммит',
'github': 'хранилище для репозиториев git',
'симулятор': 'это воспроизведение работы программы-оригинала сугубо виртуально, на движке специальной программы. Симуляция лишь имитирует выполнение кода, а не копирует его, всё виртуально на 100%, всё понарошку. Основное отличие эмулятора от симулятора заключается в том, что первый копирует суть (процесс, объект) работы, а второй - лишь окружающую действительность (оболочка, свойства объекта).',
'эмулятор': 'это воспроизведение работы программы или системы (а не какой-то её мизерной части) с сохранением ключевых её свойств и принципов работы. Эмуляция выполняет программный код в привычной для этого кода среде, состоящей из тех же компонентов, что и змулируемый объект. Основное отличие эмулятора от симулятора заключается в том, что первый копирует суть (процесс, объект) работы, а второй - лишь окружающую действительность (оболочка, свойства объекта).',
'баг-репорт': 'это технический документ, который подробно описывает ошибку в работе программы, приложения или другого ПО. Его составляет тестировщик, чтобы разработчикам было понятно, что работает неправильно, насколько дефект критичен и что нужно исправить.\nАтрибуты:\n1. Заголовок(Что? Где? Когда или при каких условиях?)\n2. Описание\n3. Версия продукта(если есть)\n4. Окружение\n5. Приоритет\n6. Серьезность\n7. Предусловия(если есть)\n8. Шаги воспроизведения\n9. Фактический результат\n10. Ожидаемый результат\n11. Прикрепленные файлы',
'чек-лист': 'это список, содержащий ряд необходимых проверок во время тестирования программного продукта. Отмечая пункты списка, команда или один тестировщик могут узнать о текущем состоянии выполненной работы и о качестве продукта. Можно сказать, что чек-лист — это упрощенный тест-кейс без шагов и прочего описания. Просто список того, что необходимо проверить.',
'тест-кейс': 'это профессиональная документация тестировщика, последовательность действий направленная на проверку какого-либо функционала, описывающая как придти к фактическому результату.\nАтрибуты тест-кейса:\n1.Уникальный идентификатор тест-кейса — необходим для удобной организации хранения и навигации по нашим тест-наборам.\n2. Название — основная тема, или идея тест-кейса. Краткое описание его сути.\n3. Предусловия — описание условий, которые не имеют прямого отношения к проверяемому функционалу, но должны быть выполнены.\n4. Шаги — описание последовательности действий, которая должна привести нас к ожидаемому результату\n5. Ожидаемый результат — что мы ожидаем увидеть после выполнения шагов.',
'priority': '(приоритет, приорити) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'приорити': '(priority, приоритет) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'приоритет': '(priority, приорити) это атрибут, указывающий на очередность выполнения задачи или устранения дефекта. Проставляется руководителем или менеджером проекта.\nP1 – Высокий (High) – требуется исправить в первую очередь;\nP2 – Средний (Medium) – требуется исправить во вторую очередь, когда нет дефектов с высоким приоритетом;\nP3 – Низкий (Low) – исправляется в последнюю очередь, когда все дефекты с более высоким приоритетом уже исправлены.',
'серьезность': '(severity, северити) это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'severity': 'это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'северити': '(severity, серьезность) это атрибут, характеризующий влияние дефекта на работоспособность приложения. Проставляется тестировщиком или техническим специалистом, который может оценить степень влияния дефекта на работу системы.\nS1 – Блокирующий (Blocker) – дефект полностью блокирует выполнение функционала, нет никакого способа его обойти (дверь закрыта, нельзя войти).\nS2 – Критический (Critical) – дефект блокирует часть функциональности, но есть альтернативный путь для его обхода. (дверь закрыта, но есть окно).\nS3 – Значительный (Major) – дефект, указывающий на некорректную работу части функциональности. Зачастую связан не с тем, что функция не работает, а с тем, что она работает неправильно. В любом случае, существует более одной точки входа для инициаци нужной функциональности.\nS4 – Незначительный (Minor) – дефект, не относящийся к функциональности системы. Обычно серьезность Minor проставляется для тех дефектов, которые относятся к удобству использования или интерфейсу (на двери написано «От себя», хотя она открывается на себя), неудобное расположение замочной скважины и т.д.\nS5 – Тривиальный (Trivial) – дефект, не затрагивающий функциональность системы, а также оказывающий минимальное влияние на общее качество системы. Обычно это грамматические дефекты.',
'толстый клиент': 'это приложение, обеспечивающее (в противовес тонкому клиенту) расширенную функциональность независимо от центрального сервера. Часто сервер в этом случае является лишь хранилищем данных, а вся работа по обработке и представлению этих данных переносится на машину клиента.',   
'тонкий клиент': 'компьютер или программа-клиент, который переносит все или большую часть задач по обработке информации на сервер. Примером тонкого клиента может служить компьютер с браузером, использующийся для работы с веб-приложениями.',
'идентификация': 'процесс позволяющий однозначно определить (распознать) субъект или объект, по его идентификатору, в той или иной системе. Например, для начала система запрашивает логин, пользователь его указывает, система распознает его как существующий — это идентификация.',
'аутентификация': 'процедура проверки подлинности, например проверка подлинности пользователя путем сравнения введенного им пароля с паролем, сохраненным в базе данных.',
'авторизация': 'предоставление доступа к той или иной системе, присутствие в ней и выполнения определенных действий.\nАвторизация не просто дает возможность зайти в систему, но и разрешает совершать там определенные операции: читать документы, отправлять письма, изменять данные.',
'верификация': 'процесс просмотра документации, дизайна, кода и программы для того, чтобы проверить, было ли программное обеспечение создано в соответствии с требованиями или нет. Верификация проверяет, соответствует ли ПО спецификации, в то время как валидация проверяет, соответствует ли ПО требованиям и ожиданиям. Основная цель процесса верификации – обеспечить качество приложения, дизайна, архитектуры и т.д.\nПроцесс верификации включает в себя такие действия, как ревью, пошаговое руководство и инспекция.',
'валидация': 'динамический механизм тестирования и проверки того, действительно ли программный продукт соответствует точным потребностям заказчика или нет.\nВалидация проверяет, соответствует ли ПО требованиям и ожиданиям, в то время как верификация проверяет, соответствует ли ПО спецификации.\nЭтот процесс помогает гарантировать, что ПО выполняет желаемое использование в подходящей среде.\nПроцесс валидации включает в себя такие действия, как модульное тестирование, интеграционное тестирование, системное тестирование и пользовательское приемочное тестирование.',}


# обработчик команды '/start'  
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Список терминов ❓")
    markup.add(btn1)
    # отправляем ответ на команду '/start'
    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!\nЯ помогу тебе расшифровать сложные аббревиатуры и термины 📕\nВведи интересующий термин, например, регресс".format(message.from_user), reply_markup=markup)
 # обработчик всех остальных сообщений   
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Список терминов ❓"):
        bot.send_message(message.chat.id, text="json\nпорт\nbash\ngit\ngithub\nбаг-репорт\nчек-лист\nтест-кейс\npriority\nприорити\nприоритет\nсерьезность\nseverity\nсеверити\nэмулятор\nсимулятор\nвалидация\nверификация\nидентификация\nаутентификация\nавторизация\nтонкий клиент\nтолстый клиент")

    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()

@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
