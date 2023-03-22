ingreso = 5000
gasto = 4000

#if anidados y else if (elif)


if ingreso > 10000:
    print("estas bien en cualquier parte del mundo")
elif ingreso > 1000:
    if ingreso - gasto > 3000:
        print("Estas mal")
    elif ingreso - gasto > 0:
        print("Estas bien")
    print("estas bien en latinoamerica")
else:
    print("sos pobre")