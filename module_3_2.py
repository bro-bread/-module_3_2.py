def send_email(message, recipient, sender = "university.help@gmail.com"):
    f = recipient.find("@")
    e1 = recipient.endswith(".com")
    e2 = recipient.endswith(".ru")
    e3 = recipient.endswith(".not")

    g = sender.find("@")
    w1 = sender.endswith(".com")
    w2 = sender.endswith(".ru")
    w3 = sender.endswith(".not")

    if g == 0:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <", sender, "> на адрес <", recipient, ">.")

    if w1 == False and w2 == False and w3 == False:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <",sender,"> на адрес <",recipient,">.")

    elif w1 == True or w2 == True or w3 == True or g > 0:
        if e1 == True or e2 == True or e3 == True:
            if f >  0:
                if recipient == sender:
                    print("Нельзя отправить письмо самому себе!")
                else:
                    print("Письмо успешно отправлено с адреса <", sender, "> на адрес <", recipient, ">.")



send_email(1,"university.help@gmail.not", "university.help@gmail.not")