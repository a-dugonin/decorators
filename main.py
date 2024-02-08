import decorators


@decorators.counter
@decorators.logging
@decorators.code_slowdown
@decorators.how_are_you
def test():
    """ Функция для тестирования декораторов """
    print('<Тут что-то происходит...>')
    print(1 / 0)


@decorators.cashing
@decorators.counter
def fibonacci(number: int):
    if number <= 2:
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)


# test()
# test()

print(fibonacci(10))
print(fibonacci(11))
