calls = 0 # Создать переменную calls = 0 вне функций.
def count_calls(): # Создать функцию count_calls и изменять в ней значение переменной calls.
    global calls
    calls += 1

def string_info(string): # Создать функцию string_info с параметром string
    global calls
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): # Создать функцию is_contains с двумя параметрами string и list_to_search
    global calls
    count_calls()
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls) # Вывести значение переменной calls на экран