vege = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
vege = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cartprice = 0
cartitems = []

while True:
    print("Select Area to Shop")
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

            fruit_price = float(fruit[fruit_find + 1])
            fruit_amount = int(input(f"How many {fruit[fruit_find]} do you want: "))
            fruit_cost = fruit_price * fruit_amount
            cartprice += fruit_cost
            cartitems.append(fruit[fruit_find])

            print("Cost so far = {cartprice}")
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

            vege_price = float(vege[vege_find + 1])
            vege_amount = int(input(f"How many {vege[vege_find]} do you want: "))
            vege_cost = vege_price * vege_amount
            cartprice += vege_cost
            cartitems.append(vege[vege_find])

            print("Cost so far = {cartprice}")
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

            deli_price = float(deli[deli_find + 1])
            deli_amount = int(input(f"How many {deli[deli_find]} do you want: "))
            deli_cost = deli_price * deli_amount
            cartprice += deli_cost
            cartitems.append(deli[deli_find])

            print("Cost so far = {cartprice}")
            print(f"cartitems = {cartitems}")




    else:
        break