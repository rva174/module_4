def test_function():
    def inner_function():
        print('Я из области видимости функции test_function')

    inner_function()    # Вызов ф-ии inner_function внутри ф-ии test_function: работает

#inner_function()        # Вызов ф-ии inner_function внутри ф-ции test_function: inner_function не определена

test_function()