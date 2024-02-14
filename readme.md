# Задача 1. Как дела?
### Что нужно сделать

Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор, который при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после такой выходки Васю чуть не уволили с работы.

Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

**Пример кода:**
```markdown
@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
```


**Результат:**
```markdown
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>
```
### Что оценивается

* Результат вычислений корректен.
* Формат вывода соответствует примеру.
* Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
* Классы и методы/функции имеют прописанную документацию.
* Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не возвращает, то используется None.
* Во всех декораторах используется functools.wraps().

### Запуск и тестирование скрипта
Запуск и тестирование скрипта производится из основного файла [main.py](main.py)
____


# Задача 2. Замедление кода
### Что нужно сделать

В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
### Что оценивается

* Результат вычислений корректен.
* Сообщения о процессе получения результата осмыслены и понятны для пользователя.
* Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
* Классы и методы/функции имеют прописанную документацию.
* Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не возвращает, то используется None.
* Во всех декораторах используется functools.wraps().
### Запуск и тестирование скрипта
Запуск и тестирование скрипта производится из основного файла [main.py](main.py)
____

# Задача 3. Логирование
### Что нужно сделать

Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции и её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log записываются название функции и ошибки. 

Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
### Что оценивается

* Результат вычислений корректен.
* Сообщения о процессе получения результата осмыслены и понятны для пользователя.
* Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
* Классы и методы/функции имеют прописанную документацию.
* Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не возвращает, то используется None.
* Во всех декораторах используется functools.wraps().
### Запуск и тестирование скрипта
Запуск и тестирование скрипта производится из основного файла [main.py](main.py)
*****
# Задача 4. Счётчик
### Что нужно сделать

Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
### Что оценивается

* Результат вычислений корректен.
* Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
* Классы и методы/функции имеют прописанную документацию.
* Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не возвращает, то используется None.
* Во всех декораторах используется functools.wraps().
### Запуск и тестирование скрипта
Запуск и тестирование скрипта производится из основного файла [main.py](main.py)
*****
# Задача 5. Кэширование для ускорения вычислений
### Что нужно сделать
Вы разрабатываете программу для оптимизации вычислений чисел Фибоначчи. Числа Фибоначчи вычисляются рекурсивной функцией, каждое число равно сумме двух предыдущих чисел. Однако вы заметили, что при больших значениях чисел Фибоначчи вычисления занимают значительное время, так как многие значения вычисляются повторно. Вам поручено создать декоратор, который кэширует результаты вызова функции и позволяет избежать повторных вычислений для одних и тех же аргументов.

Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова функции и, при повторном вызове с теми же аргументами, возвращает сохранённый результат. 

Примените его к рекурсивной функции вычисления чисел Фибоначчи.

В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, если такие аргументы уже использовались, должен вернуть сохранённый результат вместо запуска расчёта.
### Советы

Для хранения результатов удобно использовать словарь, так как поиск элементов внутри словаря будет иметь сложность, равную в среднем O(1).
При этом не стоит хранить все вычисления в одном словаре, созданном снаружи функций (в глобальной области видимости). Лучше создавать отдельные словари для каждой декорируемой функции.


### Что оценивается в практической работе

* Все задачи выполнены в соответствующих папках и файлах main.py.
* Описания коммитов осмысленные и понятные: 111, done, «я сделалъ» — неверно, added m15 homework, 14.3 fix: variables naming — верно.
* Использованы именованные индексы, не просто i (подробнее об этом в видео 7.2).
* Использованы правильные числа, без дополнительных действий со стороны пользователя, без +1 (подробнее об этом в видео 7.4).
* Правильно оформлен input, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
* Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
* Присутствуют пробелы после запятых и при бинарных операциях.
* Отсутствуют пробелы после имён функций и перед скобками: print (),input () — неверно, print() — верно.
* Правильно оформлены блоки if-elif-else, циклы и функции, отступы одинаковы во всех блоках одного уровня.
* Все входные и выходные файлы называются так, как указано в задачах.
* Работа с файлами осуществляется с помощью контекстного менеджера with.
* Для обработки исключений используются блоки try-except.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Если классы вынесены в отдельный модуль, то импортируются определённые классы (запись вида from garden import * считается плохим тоном).
* Классы и методы/функции имеют прописанную документацию (хотя бы минимальную).
* Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не возвращает, то используется None.
* Во всех декораторах используется functools.wraps().

### Запуск и тестирование скрипта
Запуск и тестирование скрипта производится из основного файла [main.py](main.py)
*****


### Общие советы и рекомендации

* Арифметические операции PEP 8 остаются в приоритете. Необходимо вводить and, or.
* Руководство по стилю Python PEP 8 на английском языке.
* Руководство по стилю Python PEP 8 на русском языке.
* Список встроенных функций.