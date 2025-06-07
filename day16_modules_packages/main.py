from calculator import add, subtract
from calculator.advanced_ops import multiply, divide
from calculator import add, greet_user, capitalize_words

print(greet_user("ade"))
print(capitalize_words("python is awesome"))


print("Add:", add(2, 3))
print("Subtract:", subtract(5, 2))
print("Multiply:", multiply(3, 4))
print("Divide:", divide(10, 2))