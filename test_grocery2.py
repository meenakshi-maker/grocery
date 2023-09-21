def calculate(item_list, item_find):
    item_price = float(item_list[item_find + 1])
    item_amount = int(input(f"How many {item_list[item_find]} do you want: "))
    item_cost = item_price * item_amount
    item_list[item_find] + str(item_amount + ".")

    item_list.append()
    return item_cost


fruit = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
vege = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cartprice = 0
cartitems = []

while True:
    print("\nSelect Area to Shop")
    print("(F)ruit")
    print("(V)egetables")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()

    if len(area) > 1:
        area = area[0]

        if area == "f":
            print("Fruit Section")
            print("(A)pples")
            print("A(v)ocado")
            print("(B)anana")
            print("(K)iwifruit")
            print("(O)ranges")
            print("(G)o Back")
        fruit_choice = input("Enter fruit letter: ").lower()

        if len(fruit_choice) > 1:
            fruit_choice = fruit_choice[0]

        choices = ["a", "v", "b", "k", "o", "g"]

        if fruit_choice not in choices:
            print("Selection Error")
            continue
        elif fruit_choice == "a":
            fruit_find = fruit.index("apples")
        elif fruit_choice == "v":
            fruit_find = fruit.index("avocado")
        elif fruit_choice == "b":
            fruit_find = fruit.index("banana")
        elif fruit_choice == "k":
            fruit_find = fruit.index("kiwi")
        elif fruit_choice == "o":
            fruit_find = fruit.index("oranges")
        else:
            continue

            cartprice += fruit_cost

            money = "${:, .2f}".format(cartprice)
            print(f"Cost so far = {money}")
            print(f"cartitems = {cartitems}")

    elif area == "v":
        print("Vegetable Section")
        print("(C)ucumber")
        print("(L)ettuce")
        print("(O)nions")
        print("(P)otatoes")
        print("(S)alad Mix")
        print("(G)o Back")
        vege_choice = input("Enter vege letter: ").lower()

        if len(vege_choice) > 1:
            vege_choice = vege_choice[0]

        choices = ["a", "v", "b", "k", "o", "g"]

        if vege_choice not in choices:
            print("Selection Error")
            continue
        elif vege_choice == "c":
            vege_find = vege.index("cucumber")
        elif vege_choice == "l":
            vege_find = vege.index("lettuce")
        elif vege_choice == "o":
            vege_find = vege.index("onions")
        elif vege_choice == "p":
            vege_find = vege.index("potatoes")
        elif vege_choice == "s":
            vege_find = vege.index("salad mix")
        else:
            continue

            vege_cost = calculate(vege, vege_find)

            cartprice += vege_cost

            money = "${:, .2f}".format(cartprice)
            print(f"Cost so far = {money}")
            print(f"cartitems = {cartitems}")



    elif area == "d":
        print("Delicatessan")
        print("delitable Section")
        print("(C)ucumber")
        print("(L)ettuce")
        print("(O)nions")
        print("(P)otatoes")
        print("(S)alad Mix")
        print("(G)o Back")
        deli_choice = input("Enter deli letter: ").lower()

        if len(deli_choice) > 1:
            deli_choice = deli_choice[0]

        choices = ["h", "m", "s", "l", "u", "g"]

        if deli_choice not in choices:
            print("Selection Error")
            continue
        elif deli_choice == "h":
            deli_find = deli.index("ham")
        elif deli_choice == "m":
            deli_find = deli.index("mussels")
        elif deli_choice == "o":
            deli_find = deli.index("salami")
        elif deli_choice == "p":
            deli_find = deli.index("salmon")
        elif deli_choice == "s":
            deli_find = deli.index("sausages")
        else:
            continue

            deli_cost = calculate(deli, deli_find)

            cartprice += deli_cost
            money = "${:, .2f}".format(cartprice)
            print(f"Cost so far = {money}")
            print(f"cartitems = {cartitems}")




    else:
        break

print("thank you for shopping with us.")
print(f"Total cost-{cartprice}")
print("Items bought = {cartitems}")