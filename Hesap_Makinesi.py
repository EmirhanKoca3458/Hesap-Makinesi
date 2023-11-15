
while True:
    
    
    işlem = input("Hoşgeldiniz\n1-Toplama\n2-Çıkarma\n3-Bölme\n4-Çarpma\n5-Çıkmak için F tuşuna basınız.")
    
    
    if işlem == "1":
        sayı1 = int(input("1-Sayı giriniz:"))
        sayı2 = int(input("2-Sayı giriniz:"))
        
        x = sayı1 + sayı2 
        print("Sonuç:",x)
        
        
        
        
    elif işlem == "2":
        sayı1 = int(input("1-Sayı giriniz:"))
        sayı2 = int(input("2-Sayı giriniz:"))
        
        x = sayı1 - sayı2 
        print("Sonuç:",x)
        

        
    elif işlem == "3":
        sayı1 = int(input("1-Sayı giriniz:"))
        sayı2 = int(input("2-Sayı giriniz:"))
        
        x = sayı1 / sayı2 
        print("Sonuç:",x)
        
        
        
    elif işlem == "4":
        sayı1 = int(input("1-Sayı giriniz:"))
        sayı2 = int(input("2-Sayı giriniz:"))
        
        x = sayı1 * sayı2 
        print("Sonuç:",x)
        
        
        
    elif işlem == "F" or "f" :
        break
        
    
    