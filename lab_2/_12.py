#12. Дано дійсне число - ціна 1 кг цукерок. Вивести вартість 1, 2, ..., 10 кг цукерок.

price=182.75

for i in range (1,11):
    pay=i*price
    print("For {0} kg must be paid {1} grn.\n".format(i,pay))
