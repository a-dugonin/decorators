from decorators import how_are_you, code_slowdown, logging, counter


@counter
@logging
@code_slowdown
@how_are_you
def test():
    """ Функция для тестирования декораторов """
    print('<Тут что-то происходит...>')
    return 1 / 0


test()
test()
