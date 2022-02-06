print("************************\nFibonacci Serisi Programı"
      "\n************************")

alinan_deger = input("Seri Kaç kere tekrarlansın:")
alinan_deger =int(alinan_deger)

sayi1,sayi2=1,1

fibonacci =[sayi1,sayi2]

for i in range(alinan_deger):

    sayi1,sayi2=sayi2,sayi1+sayi2
    fibonacci.append(sayi2)

print(fibonacci)