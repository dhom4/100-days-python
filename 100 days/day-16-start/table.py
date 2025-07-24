from prettytable import PrettyTable
resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
}

table = PrettyTable()
table.add_column("res", [1,2,3,4,4])
print(table)