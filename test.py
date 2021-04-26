

print(mydb)
cursor = mydb.cursor()


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()



def start():
    print('~-' * 10)
    setpassword = input('>>[Entrez le mot de passe]: ')
    if(setpassword == password):
        ok()
    else:
        print('Mot de passe incorrect')
        start()


def ok():
    print('~-' * 10)
    credit = input('>>[Entrez le montant des crédits à générer]: ')
    if(credit.isnumeric() is True):
        credits = int(credit)
        print('~-' * 10)
        howmany = input('>>[Combien de code à générer ? (default 1)]: ')
        if(howmany.isnumeric() is True):
            howmany = int(howmany)
        if(howmany is None or howmany == ""):
            howmany = 1
        for i in range(howmany):
            letters = string.ascii_uppercase
            key = ''.join(random.choice(letters) for i in range(5)) +"-" +''.join(random.choice(letters) for i in range(5))+"-" +''.join(random.choice(letters) for i in range(5))+"-" +''.join(random.choice(letters) for i in range(5))
            query = "INSERT INTO credits_code (code, credit) VALUES (%s, %s)"
            ## storing values in a variable
            values = (key, credits)
            cursor.execute(query, values)
            mydb.commit()
            print('You '+credit+' credit key is : '+key)
            ok()
    else:
        print('Invalide')
        ok()




start()