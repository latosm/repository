# 1. Funkcja przyjmująca imię i nazwisko, zwracająca powitanie
def greet(name, surname):
    result = f"Cześć {name} {surname}!"
    return result

# Przykład użycia i wyświetlenie wyniku
greeting_result = greet("Jan", "Kowalski")
print(greeting_result)

# 2. Funkcja mnożąca dwie liczby
def multiply_numbers(a, b):
    result = a * b
    return result

# Przykład użycia i wyświetlenie wyniku
multiplication_result = multiply_numbers(3, 4)
print(multiplication_result)

# 3. Funkcja sprawdzająca parzystość liczby
def is_even(number):
    return number % 2 == 0

# Przykład użycia i wyświetlenie wyniku
even_check_result = is_even(7)
if even_check_result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# 4. Funkcja sprawdzająca warunek na sumę dwóch pierwszych liczb
def check_sum_condition(a, b, c):
    return (a + b) >= c

# Przykład użycia i wyświetlenie wyniku
sum_condition_result = check_sum_condition(5, 7, 10)
print(sum_condition_result)

# 5. Funkcja sprawdzająca obecność wartości w liście
def check_value_in_list(input_list, value):
    return value in input_list

# Przykład użycia i wyświetlenie wyniku
list_check_result = check_value_in_list([1, 2, 3, 4], 3)
print(list_check_result)

# 6. Funkcja łącząca, usuwająca duplikaty i podnosząca do potęgi 3 elementy list
def process_lists(list1, list2):
    merged_list = list(set(list1 + list2))
    result_list = [x ** 3 for x in merged_list]
    return result_list

# Przykład użycia i wyświetlenie wyniku
list_processing_result = process_lists([1, 2, 3], [3, 4, 5])
print(list_processing_result)