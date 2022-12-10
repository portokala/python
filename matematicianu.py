name = input("Ce faci pepushe cum te chiama?\n")
print ("Ce faci fa " + (name) + "?\n Hai sa vedem daca stii sa calculezi pe degete")
raspuns = int(input("cat face unu plus unu? "))
raspuns_corect = 2
if raspuns == raspuns_corect:
    print("bravo boss hai ca nu esti asa prost")
elif raspuns != raspuns_corect:
    print("vai de capul tau") 
ix= input("mai am o rugaminte la tn inainte sa pleci ok??")
print(ix)

while True:
    try:
        numaru = int(input("numaru tau de telefon "))
        if numaru > 20000000:
            break
    except ValueError:
        print("pepushe tiam cerut nr nu adresa de aks")
        continue
print("verific acum daca asta e ms", numaru)