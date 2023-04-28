def sh(shares,amount):
    if shares >4:
        retun=amount*.20
    else:
        retun=amount*.30
        return retun
    
sh(5,20000)

def credit_card (salary):
    if salary <10000:
        retun=salary*10
    elif salary >10000 and salary <30000:
        retun =salary*20
    else:
        retun=salary*30
        return retun
    
credit_card(7000)


def product (type,amount):
    if type == "electronic":
        retun=amount*.20
    elif type == "cloth" :
        retun=amount*.30
    elif type == "footware" :
        retun=amount*.40
    else:
        retun=amount*.50
        return retun
product ("cloth",10000)


def dmart (purchase_amount):
    if purchase_amount  <20000:
        retun=purchase_amount*.20
    elif purchase_amount >20000 and purchase_amount <40000:
        retun=purchase_amount*.30
    elif purchase_amount >50000:
        retun=purchase_amount*.40
        return retun
dmart(10000)

        

