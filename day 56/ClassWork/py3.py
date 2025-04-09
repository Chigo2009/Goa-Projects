def captianjack(gold_coin):
    ships = {
        150: "150 ოქროს მონეტა",
        200: "200 ოქროს მონეტა",
        250: "250 ოქროს მონეტა",
        300: "300 ოქროს მონეტა",
        350: "350 ოქროს მონეტა"
    }

    
    if gold_coin == 0:
        print("ეკიპაჯი აჯანყდა")
        return

    print("დასაშვები გემები:")
    for price in ships:
        print(f"{ships[price]} - {price} ოქროს მონეტა")

   
    chosen_ship = int(input("აირჩიე გემი"))
    
    if chosen_ship not in ships:
        print("არასწორი არჩევანი!")
        return
    
    if gold_coin >= chosen_ship:
        print(f"გემი {chosen_ship} ოქროს მონეტით წარმატებით შეიძენილია! დარჩენილი მონეტები: {gold_coin - chosen_ship}")
    else:
        print("ეკიპაჟი აჯანყდება! ოქროს მონეტები არ ჰყოფნის."