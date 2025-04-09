def yuri_gagarini():
        wneva = int(input("შეიყვანეთ თქვენი გულის წნევა: "))
        pulsi = int(input("შეიყვანეთ თქვენი პულსი: "))
        
        if wneva == 120 and pulsi == 80:
            return True
        else:
            return False
result = yuri_gagarini()
print(result)
