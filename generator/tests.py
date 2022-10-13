from django.test import TestCase

# Create your tests here.
first_name, last_name, age = input(), input(), input()
print('Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!'.format(first_name, last_name, age))
