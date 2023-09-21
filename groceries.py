
fruit = ["apples", 1.50, "oranges", 1.75, "banana", 2.00, "avocado", 2.50, "kiwi", 1.15]
veges = []
deli = []

cart_total = 0
cart_items = []

while True:
    print("Choose Department:")
    print("(D)elicatessen")
    print("(F)ruit Section")
    print("V)egetables")
    print("e(X)it")
    section_choice = input("Enter Letter:")

    section_choice = section_choice[0]
    section_choice = section_choice.lower()
    match section_choice :

        case "d":
            print("go to delicatessan")
        case "f":
            print("Fruit section")
            print("(A)pples")
            print("a(V)ocado")
            print("(B)anana")
            print("(K)iwifruit")
            print("(O)ranges")
            print("(G)rapes")
            fruit_choice = input("Select Fruit:  ")
            fruit_choice = fruit_choice[0]
            fruit_amount =int (input("How Many: "))

        case "a":
            fruit_find = fruit.index("apples")

        case "v":
            fruit_find = fruit.index("avacado")

        case "b":
            fruit_find = fruit.index("banana")


        case"k":
            fruit_find = fruit.index("kiwi")

        case"o":
            fruit_find = fruit.index("oranges")

        case"g":
            continue

fruit_price = float(fruit[fruit_amount + 1])
fruit_cost = fruit_amount * fruit_price
print("go to vegetable")

cart_total = cart_total + fruit_cost
cart_items.append(fruit[fruit_amount])
print(cart_items)
print(f"Cost so far: {cart_total}")

