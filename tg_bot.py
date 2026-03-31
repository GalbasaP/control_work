import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def update_screen(call, text=None, photo=None, markup=None):
    try:
        if photo:
            media = types.InputMediaPhoto(photo, caption=text)

            bot.edit_message_media(
                media,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup
            )
        else:
            bot.edit_message_text(
                text,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup
            )
    except Exception:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if photo:
            bot.send_photo(call.message.chat.id, photo, caption=text, reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton('📚 Теория', callback_data='theory')
    markup.add(button1)
    bot.send_message(
        message.chat.id,
        f'Привет! Я Чупайкабра!\nТвой "молчаливый" фамильяр в мире Пайтон!\n'
        f'Вот инструкция по управлению мной:\n',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'theory' or call.data == 'back':

        markup = types.InlineKeyboardMarkup()

        cycles = types.InlineKeyboardButton('🔄 Циклы', callback_data='cycles')
        condition = types.InlineKeyboardButton('📌 Условия', callback_data='condition')
        variables = types.InlineKeyboardButton('📦 Переменные', callback_data='variables')
        function_def = types.InlineKeyboardButton('🧩 Функции', callback_data='functions')
        exceptions = types.InlineKeyboardButton('🐞 Ошибки', callback_data='errors')
        function_style = types.InlineKeyboardButton('🧠 Функциональный стиль', callback_data='other')
        # back_step = types.InlineKeyboardButton("⬅️ Назад", callback_data='back')

        markup.add(variables, condition, cycles, function_def, exceptions, function_style)  # back_step)

        bot.edit_message_text(
            'Выбери тему:',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'variables' or call.data == 'back_variables':
        markup = types.InlineKeyboardMarkup()
        names_variables = types.InlineKeyboardButton('🔖 Имена', callback_data='name_variables')
        types_information = types.InlineKeyboardButton('🔢 Типы данных', callback_data='type_inf')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(names_variables, types_information, back_step)
        bot.edit_message_text(
            'К чему лежит твоя душа конкретно?',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data == 'condition' or call.data == 'condition_back':
        markup = types.InlineKeyboardMarkup()
        if_inf = types.InlineKeyboardButton('⁉️ if/elif/else', callback_data='if_else')
        match_case_inf = types.InlineKeyboardButton('❕ match/case', callback_data='match_case')
        operators = types.InlineKeyboardButton('⚖️ Операторы', callback_data='operators')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(if_inf, match_case_inf, operators, back_step)
        bot.edit_message_text(
            'К чему лежит твоя душа конкретно?',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'cycles' or call.data == 'cycles_back':
        markup = types.InlineKeyboardMarkup()
        for_inf = types.InlineKeyboardButton('🔂 for', callback_data='for')
        while_inf = types.InlineKeyboardButton('🔁 while', callback_data='while')
        break_continue = types.InlineKeyboardButton('⏹️⏭️ break/continue', callback_data='continue')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(for_inf, while_inf, break_continue, back_step)
        bot.edit_message_text(
            '123',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'functions' or call.data == 'functions_back':
        markup = types.InlineKeyboardMarkup()

        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(back_step)
        bot.edit_message_text(
            'В разработке :(',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'errors' or call.data == 'errors_back':
        markup = types.InlineKeyboardMarkup()
        exceptions_inf = types.InlineKeyboardButton('🚫 Исключения', callback_data='exception')
        debugging = types.InlineKeyboardButton('🔎 Отладка', callback_data='debug')
        correction = types.InlineKeyboardButton('🙈 Игнорирование', callback_data='ignore')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(exceptions_inf, debugging, correction, back_step)
        bot.edit_message_text(
            '123',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data == 'other' or call.data == 'other_back':
        markup = types.InlineKeyboardMarkup()
        lambda_inf = types.InlineKeyboardButton('⚡️ lambda', callback_data='lambda')
        map_inf = types.InlineKeyboardButton('♻️ map', callback_data='map')
        reduce_inf = types.InlineKeyboardButton('🧮 reduce', callback_data='reduce')
        filter_inf = types.InlineKeyboardButton('🔍 filter', callback_data='filter')
        comprehensions_inf = types.InlineKeyboardButton('➕ Comprehesions', callback_data='comprehension')
        short_circuits = types.InlineKeyboardButton('🔒 Замыкания', callback_data='circuits')
        decorators = types.InlineKeyboardButton('🎭 Декораторы', callback_data='decorator')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')
        markup.add(comprehensions_inf, lambda_inf, map_inf, filter_inf, reduce_inf, short_circuits, decorators,
                   back_step)
        bot.edit_message_text(
            '123',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'name_variables':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back_variables')
        markup.add(back_step)
        bot.edit_message_text(
            f'Переменная - именованная область памяти, в которой хранится значение определённого типа\n'
            f'Имеет: тип, имя, значение\n'
            f'\nИмя должно начинаться с маленькой буквы или _\n'
            f'\n_ можно использовать в виде разделителя\n'
            f'\nСтиль именования в Python - snake_case',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif call.data == 'type_inf' or call.data == 'type_inf_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_type_inf')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='back_variables')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Immutable:\n'
            f'\nint - Целые числа\n'
            f'float - Числа с плавающей точкой\n'
            f'complex - Комплексные числа, состояшие из вещественной и мнимой частей\n'
            f'bytes - Байты\n'
            f'tuple - неизменяемый тип данных в Python, который используется для хранения упорядоченной '
            f'последовательности элементов\n'
            f'str - строка\n'
            f'\nMutable:\n'
            f'dict - коллекция пар ключ-значение, где ключ уникален, а значения могут повторяться\n'
            f'list - коллекция нескольких элементов, к которым обращаешься по индексам\n'
            f'set - изменяемое множество уникальных значений\n'
            f'\nother:\n'
            f'bool - булевые значения True/False\n'
            f'NoneType - нейтральное пустое значение None',
            markup=markup
        )
    elif call.data == 'if_else' or call.data == 'if_else_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_if_else')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='condition_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Условные операторы помогают выполнить определенный код в зависимости от условий:\n'
            f'\nОператор if - если логическое выражение соответствует написанному кодером - выполняется код в блоке '
            f'ниже\n'
            f'\nelif - опциональный оператор, если условие в if не выполняется, '
            f'проверяется логическое выражение в этом операторе и если соответсвует, то выполняется код ниже\n'
            f'\nelse - если логическое выражение не соответствует ни одному if/elif, выполняется блок кода else, '
            f'условия прописывать не нужно',
            markup=markup
        )
    elif call.data == 'match_case' or call.data == 'match_case_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_match_case')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='condition_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Конструкция match/case — это мощный инструмент, '
            f'который позволяет писать более читаемый и лаконичный код.\n'
            f'Она особенно полезна, когда нужно обрабатывать разные форматы данных или проверять множество условий.',
            markup=markup
        )
    elif call.data == 'operators' or call.data == 'operators_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_operators')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='condition_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Операторы сравнения:\n'
            f'\n== - равен ли левый операнд правому'
            f'\n!= - проверяет неравенство левого операнда к правому'
            f'\n> - больше ли левый операнд правого'
            f'\n< - меньше ли левый операнд правого'
            f'\n>= - больше или равен, ли левый операнд правому'
            f'\n<= - меньше или равен, ли левый операнд правому'
            f'\nis - проверяет тождественное равенство на нахождение их по одному адресу в памяти\n'
            f'\nЛогические операторы:'
            f'\nand - результат - True ,если оба варианта истинны'
            f'\nor - результат - True, если хоть один из вариантов истинен'
            f'\nnot - инвертитрует значения: из True в False, из False в True',
            markup=markup
        )
    elif call.data == 'for' or call.data == 'for_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_for')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='cycles_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Используется когда мы заранее знаем точное число повторений.\n'
            f'Последовательно получает значения из набора и передает их в переменную.\n'
            f'Когда все значения из набора будут перебраны, цикл закончит свою работу.\n',
            markup=markup
        )
    elif call.data == 'while' or call.data == 'while_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_while')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='cycles_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Цикл while используется когда мы не знаем точное число повторений',
            markup=markup
        )
    elif call.data == 'continue' or call.data == 'continue_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_continue')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='cycles_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Оператор continue переходит к следующей итерации цикла минуя оставшиеся команды в теле цикла\n'
            f'\nОператор break досрочно прерывает цикл. Оставшиеся итерации выполняться не будут',
            markup=markup
        )
    elif call.data == 'exception' or call.data == 'exception_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_exception')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='errors_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Исключения - это механизм обработки ошибок во время выполнения программы.\n'
            f'Они позволяют программе продолжить работу после обнаружения ошибки, а не завершаться аварийно.\n'
            f'В Python есть встроенные исключения, которые обрабатывают большинство типовых ошибок.\n'
            f'\nПримеры исключений: '
            f'\nTypeError - операция или функция применяется к объекту несоответствующего типа.'
            f'\nValueError - операция или функция получает аргумент неподходящего значения. '
            f'К примеру, исключение возникает, если попытаться преобразовать строку в число.'
            f'\nIndexError - обращение к элементу по несуществующему индексу.'
            f'\nZeroDivisionError - деление числа на ноль.'
            f'\nFileNotFoundError - Python не может найти файл, который мы хотим открыть.'
            f'\nИ куча многих других',
            markup=markup
        )
    elif call.data == 'debug' or call.data == 'debug_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_debug')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='errors_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'При возникновении исключения работа программы прерывается.\n'
            f'Чтобы этого избежать в Python существует обработчик try/except:\n'
            f'\nВесь основной код в котором потенциально может возникнуть исключение помещается после try'
            f'\nЕсли в этом коде генерируется исключение, то работа в данном блоке прерывается, '
            f'выполнение переходит в переходит в блок except'
            f'\nВ блоке except содержится код, который будет выполняться, если в блоке try нашлась ошибка.'
            f'\nБлок except без указания конкретного типа исключения будет обрабатывать все исключения, '
            f'которые не были обработаны в предыдущих блоках except, в том числе прерывание с клавиатуры, '
            f'системный выход и другое, однако это правило плохого тона, так делать не стоит'
            f'\nПомимо основных try/except существуют дополнительные блоки finally/else:\n'
            f'\nfinally: в нем помещают код, который будет выполняться независимо от того, '
            f'была ли найдена ошибка или нет. Часто этот блок используют для работы с файлами, чтобы закрыть документ.'
            f'\nКод в else выполняется, если try не нашёл исключений.',
            markup=markup
        )
    elif call.data == 'ignore' or call.data == 'ignore_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_ignore')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='errors_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Для игнорирования исключений в Python можно использовать блок try/except.'
            f'\nПри этом нужно except оставить пустым или записать в нём оператор-заглушку pass, '
            f'который ничего не делает.\n'
            f'Важно помнить, что не стоит полностью игнорировать ошибки. '
            f'Это может привести к тому, что скрытые проблемы в коде останутся незамеченными и '
            f'будет сложнее отлаживать и поддерживать программу в долгосрочной перспективе.',
            markup=markup
        )
    elif call.data == 'lambda' or call.data == 'lambda_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_lambda')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Lambda функции являются анонимными функциями(у функции нет имени), '
            f'"lambda" - ключевое слово для объявления'
            f'анонимной функции. Такие функции могут иметь любое кол-во аргументов, '
            f'но тело функции должно содержать только одну инструкцию.'
            f'\nlambda функции не содержат операторы return, pass, raise/assert.'
            f'Oна сразу предовставляет возвращаемое значение.'
            f'\nВ lambda функции аннотация типов также недоступна',
            markup=markup
        )
    elif call.data == 'map' or call.data == 'map_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_map')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Втроенная функция map работает только со списками, массивами, кортежами, строками или множествами.'
            f'\nmap принимает 2 аргумента: функцию и последовательность.'
            f'Переданная в качестве аргумента функция применяется к последовательности.'
            f'\nРезультат работы map() - новая последовательность из результатов обработки аргументной функции.'
            f'\nФункция map() использует особый механизм обработки данных: вместо немедленного создания нового списка, '
            f'она возвращает специальный объект итератор'
            f'Он работает по принципу "ленивых вычислений": функция преобразования применяется к элементам только '
            f'тогда, когда они действительно необходимы. '
            f'Когда они не нужны итератор не тратит ресурсы на их обработку.'
            f'\nЧтобы увидеть результат map() надо его преобразовать при помощи list(map(...)).'
            f'\nИтератор можно использовать только один раз, далее он пуст, '
            f'поэтому если цель - многократно возвращаться к результату map() - '
            f'лучше его результат сохранить в отдельную переменную',
            markup=markup
        )
    elif call.data == 'filter' or call.data == 'filter_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_filter')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Функция filter() также является встроенной и также как и map() принимает 2 аргумента'
            f': функцию и последовательность.'
            f'\nОднако результат работы - булевые значения True/False'
            f'\nfilter() - отфильтровывает элементы последовательности на основе какого-либо критерия. '
            f'Критерий прописан в аргументной функции, она применяется по порядку к каждому элементу '
            f'последовательности',
            markup=markup
        )
    elif call.data == 'reduce' or call.data == 'reduce_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_reduce')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Функция reduce() в отличии от своих собратьев map()/filter() не является встроенной. '
            f'Вынесена в модуль functools'
            f'\nreduce() кумулятивно применяет аргументную функцию к элементам последовательностей, '
            f'сводя их к единственному значению.'
            f'\nВ функцию reduce() передаются 2 аргумента: аккумулированное значение из аргументной функции '
            f'и следующий элемент последовательности'
            f'\n\n! Для reduce() может быть задан 3-ий аргумента: инициализирующее значение, '
            f'eсли последовательность пустая то вернется инициализирующее значение ',
            markup=markup
        )
    elif call.data == 'comprehension' or call.data == 'comprehension_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_comprehension')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Comprehension - это синтаксическая конструкция, позволяющая создавать '
            f'коллекции данных(списки, словари, множества)'
            f'или генераторы в более лаконичной и выразительной форме, чем с помощью традиционных циклов.'
            f'\n\nComprehensions исходит из функционального программирования и '
            f'математической теории множеств и напоминает нотацию для описания множеств.'
            f'\nВ конец comprehensions можно добавить условный оператор if, для генерации конкретного по условию списка'
            f'\n\nТакже comprehensions можно делать вложенными друг в друга для генерации многомерных массивов(матрицы)'
            f'\n\n!Важный нюанс:'
            f' после того, как генератор отработает, '
            f'вложенная переменная будет забыта и вернуться к ней будет невозможно.',
            markup=markup
        )
    elif call.data == 'circuits' or call.data == 'circuits_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_circuits')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'closure(замыкания) - это функция, сочетающаяся с окружением, в котором она была определена.'
            f'\nПозволяет функции запоминать значения из этого окружения.'
            f'\nПозволяет запоминать значения из этого окружени, даже если оно уже не существует во время выполнения. '
            f'\nЗамыкания часто возникают когда определяется функция внутри другой функции. '
            f'Внутренней функции функции нужны значения переменных из внешней функции'
            f'\n\n! Захват происходит не по значению, а по ссылке. '
            f'Это может привести к неочевидным результам особенно при работе с изменяемыми '
            f'типами данных или когда переменные меняются в процессе выполнения',
            markup=markup
        )
    elif call.data == 'decorator' or call.data == 'decorator_back':
        markup = types.InlineKeyboardMarkup()
        example = types.InlineKeyboardButton('📝 Пример', callback_data='example_decorator')
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='other_back')
        markup.add(example, back_step)
        update_screen(
            call,
            f'Декоратор - функция, которая используется для расширения возможностей другой функции или класса.'
            f'\nДекораторы позволяют модифицировать исходную функцию, значения ее параметров и её результат, '
            f'без изменения исходного кода самой функции.'
            f'\nПрименение декоратора осуществляется через @ после которого идет имя'
            f' декоратора сверху над именем декорируемой функции'
            f'\nДекораторы могут работать с передачей аргументов в исходную функцию.'
            f'\nДля этого внутренняя функция декоратора должна содержать параметр *args, '
            f'который и будет захватывать переданные исходной функции аргументы.'
            f'\nК одной функции можно применять несколько декораторов. Порядок их вызова будет соответствовать '
            f'тому порядку, в котором декораторы указаны при определении исходной функции',
            markup=markup
        )

    elif call.data == 'example_type_inf':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='type_inf_back')
        markup.add(back_step)
        photo = open('jpgs/example_types.png', 'rb')
        update_screen(
            call,
            text='Пример типов данных',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_if_else':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='if_else_back')
        markup.add(back_step)
        photo = open('jpgs/if_else_example.png', 'rb')
        update_screen(
            call,
            text='Пример if/else',
            photo=photo,
            markup=markup
        )
        photo.close()

    elif call.data == 'example_match_case':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='match_case_back')
        markup.add(back_step)
        photo = open('jpgs/match_case.png', 'rb')
        update_screen(
            call,
            text='Пример match/case',
            photo=photo,
            markup=markup
        )
        photo.close()

    elif call.data == 'example_operators':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='operators_back')
        markup.add(back_step)
        photo = open('jpgs/comparison.png', 'rb')
        update_screen(
            call,
            text='Список всех операторов',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_for':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='for_back')
        markup.add(back_step)
        photo = open('jpgs/for.png', 'rb')
        update_screen(
            call,
            text='Пример цикла for',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_while':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='while_back')
        markup.add(back_step)
        photo = open('jpgs/while.png', 'rb')
        update_screen(
            call,
            text='Пример цикла while',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_continue':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='continue_back')
        markup.add(back_step)
        photo = open('jpgs/continue_break.png', 'rb')
        update_screen(
            call,
            text='Пример использования операторов continue/break',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_exception':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='exception_back')
        markup.add(back_step)
        photo = open('jpgs/exceptions.png', 'rb')
        update_screen(
            call,
            text='Примеры исключений',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_debug':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='debug_back')
        markup.add(back_step)
        photo = open('jpgs/raise.png', 'rb')
        update_screen(
            call,
            text='Пример',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_ignore':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='ignore_back')
        markup.add(back_step)
        photo = open('jpgs/ignore.png', 'rb')
        update_screen(
            call,
            text='Пример',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_comprehension':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='comprehension_back')
        markup.add(back_step)
        photo = open('jpgs/comprehension.png', 'rb')
        update_screen(
            call,
            text='Пример использования comprehension',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_lambda':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='lambda_back')
        markup.add(back_step)
        photo = open('jpgs/lambda.png', 'rb')
        update_screen(
            call,
            text='Пример использования фукнции lambda',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_map':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='map_back')
        markup.add(back_step)
        photo = open('jpgs/map.png', 'rb')
        update_screen(
            call,
            text='Пример с использованием map()',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_filter':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='filter_back')
        markup.add(back_step)
        photo = open('jpgs/filter.png', 'rb')
        update_screen(
            call,
            text='Пример с использованием filter()',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_reduce':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='reduce_back')
        markup.add(back_step)
        photo = open('jpgs/reduce.png', 'rb')
        update_screen(
            call,
            text='Пример с использованием reduce()',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_circuits':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='circuits_back')
        markup.add(back_step)
        photo = open('jpgs/circuits.png', 'rb')
        update_screen(
            call,
            text='Пример с использованием замыканий',
            photo=photo,
            markup=markup
        )
        photo.close()
    elif call.data == 'example_decorator':
        markup = types.InlineKeyboardMarkup()
        back_step = types.InlineKeyboardButton('⬅️ Назад', callback_data='decorator_back')
        markup.add(back_step)
        photo = open('jpgs/decorator.png', 'rb')
        update_screen(
            call,
            text='Пример с использованием декоратора',
            photo=photo,
            markup=markup
        )
        photo.close()


@bot.message_handler(func=lambda message: True)
def handle_any_text(message):
    bot.delete_message(

        message.chat.id,
        message.message_id
    )


bot.infinity_polling()
