from decorators import how_are_you

if __name__ == '__main__':
    @how_are_you
    def test():
        print('<Тут что-то происходит...>')


    test()
