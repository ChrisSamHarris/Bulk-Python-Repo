#pypi.org - prettytable

from prettytable import PrettyTable
#Class is a bluebrint for creating objects

#Object
table = PrettyTable()
#Methods to work with table object
#Method = a function associated with an object/ class, need to be called with a ()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

#Attributes to edit object
table.align = "c"

print(table)




