# import another_module
# print(another_module.another_variable)


# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# # print(timmy)
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
# table.align = "c"
print(table.align)
table.align['Type'] = 'l' # Changing the alignment of one column to left
print(table)
print(table.align)
