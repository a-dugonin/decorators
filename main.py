import decorators


@decorators.code_slowdown
@decorators.how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
