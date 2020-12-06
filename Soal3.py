input_kata = input("Masukkan kata: ")

def urai(x):
    input_kata = input("Masukkan kata: ")
    x = 0
    for input_kata in range(x): 
        x += 1
    b = str(input_kata[0]) * str(input_kata[x]) #ini maksudnya untuk memperpanjang huruf inputan
    return b 

print(urai(input_kata))

def rajut(y):
    input_kata = input("Masukkan kata: ")
    y = -1 #ini negatif untuk memperpendek huruf inputan. 
    for input_kata in range(y):
        y += 1
    c = str(input_kata[0]) * str(input_kata[y])
    return c

print(rajut(input_kata))

#Disini error nya banyak. Kebetulan saya gak dapet logicnya disini. 
