import decorators


@decorators.logging
@decorators.code_slowdown
@decorators.how_are_you
def test():
    """ Функция для тестирования декораторов """
    print('<Тут что-то происходит...>')
    print(1/0)


test()
