from random import randint
secret = randint(0, 100)
minejums = -1  #kaut kas, kas nav iespējams

while minejums != secret:
    minejums = int(input("Lūdzu miniet skaitli: "))

    if secret > minejums:
        print("Īstais skaitlis ir lielāks")
    elif secret < minejums:
        print("Īstais skaitlis ir mazāks")
    else:
        print("Apsveicu, skaitlis ir atminēts")
