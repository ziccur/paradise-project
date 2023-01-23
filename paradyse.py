import string, random

# SCRIPT MADE BY YERAY on 2023-01-20
# Proyecto Paradise #1 
# C & D, Auto Generet Key and specific Key Cifrate

##DICS 1 and 2. 1=C 2=D (dic1,dic2)

dic1 = {"a":"R4f","A":"m4w",":":"ukq","ç":"vrT","á":"B6M","1":"Ppj","b":"NT3","B":"P7g","-":"3YN","¨":"aPP","à":"fta", "2":"qAn","c":"ekJ",    "C":"Vua",   ".":"miH",    "^":"Ac8",    "é":"ZMt",    "3":"YjG","d":"ctZ","D":"Bg7",",":"xRV",    "[":"6Zk",    "è":"Fyg",    "4":"mpX","e":"bD9",    "E":"YBA",   ";":"mCa",    "]":"VX5",    "í":"8UK",    "5":"rEd","f":"HCq",    "F":"dTr",   "_":"77Y",    "{":"GzH",    "ì":"5re",    "6":"8zr","g":"Hix",    "G":"4Yv",   "+":"hHL",    "}":"xtK",    "ó":"66U",    "7":"7x9","h":"4HL",    "H":"YcX",   "*":"HrS",    "¬":"zzF",    "ú":"jfu",    "8":"2Pz","i":"vvf",    "I":"BLG",   "`":"G7a",    "~":"DiS",    "ù":"APB",    "9":"kXu","j":"9bX",    "J":"krr",   "´":"VCz",    "#":"Qg8",    "ò":"9rq",    "0":"Daa","k":"RBp",    "K":"RGx",   "?":"Gd6",    "@":"rZB","l":"wJa",    "L":"dpZ",   "'":"Zzk",    "|":"SAD","m":"Rez",    "M":"aMu",   "¿":"Zy8",    "€":"EaX","n":"DGz",    "N":"ttE",   "¡":"6rn",    '"':"fhn","ñ":"YrR",    "Ñ":"M8K",   "=":"j2Y",    "!":"T9r","o":"nbq",    "O":"Q7n",   ")":"vzH",    "·":"GqF","p":"BJZ",    "P":"q68",   "(":"UEA",    "$":"ZNp","q":"3hQ",    "Q":"Z9i",   "/":"6K9",    "%":"mXq","r":"RLH",    "R":"bpp",   "|":"8bF",    "&":"dLK","s":"vYp",    "S":"zfE",   "t":"X3b",    "T":"fdL",   "ª":"Pcy","u":"bTy",    "U":"NxZ","v":"VkH",    "V":"nNa","w":"nu6",    "W":"j72","x":"t75",    "X":"HuL","y":"3QG",    "Y":"LJt","z":"bYV",    "Z":"P7n"," ":"6Ur"}
dic2 = {"R4f":"a",    "m4w":"A",   "ukq":":",    "vrT":"ç",    "B6M":"á",    "Ppj":"1","NT3":"b",    "P7g":"B",   "3YN":"-",    "aPP":"¨",    "fta":"à",    "qAn":"2","ekJ":"c",    "Vua":"C",   "miH":".",    "Ac8":"^",    "ZMt":"é",    "YjG":"3","ctZ":"d",    "Bg7":"D",   "xRV":",",    "6Zk":"[",    "Fyg":"è",    "mpX":"4","bD9":"e",    "YBA":"E",   "mCa":";",    "VX5":"]",    "8UK":"í",    "rEd":"5","HCq":"f",    "dTr":"F",   "77Y":"_",    "GzH":"{",    "5re":"ì",    "8zr":"6","Hix":"g",    "4Yv":"G",   "hHL":"+",    "xtK":"}",    "66U":"ó",    "7x9":"7","4HL":"h",    "YcX":"H",   "HrS":"*",    "zzF":"¬",    "jfu":"ú",    "2Pz":"8","vvf":"i",    "BLG":"I",   "G7a":"`",    "DiS":"~",    "APB":"ù",    "kXu":"9","9bX":"j",    "krr":"J",   "VCz":"´",    "Qg8":"#",    "9rq":"ò",    "Daa":"0","RBp":"k",    "RGx":"K",   "Gd6":"?",    "rZB":"@","wJa":"l",    "dpZ":"L",   "Zzk":"'",    "SAD":"|","Rez":"m",    "aMu":"M",   "Zy8":"¿",    "EaX":"€","DGz":"n",    "ttE":"N",   "6rn":"¡","YrR":"ñ",    "M8K":"Ñ",   "j2Y":"=","nbq":"o",    "Q7n":"O",   "vzH":")","BJZ":"p",    "q68":"P",   "UEA":"(","3hQ":"q",    "Z9i":"Q",   "6K9":"/","RLH":"r",    "bpp":"R",   "dLK":"&","vYp":"s",    "zfE":"S",   "mXq":"%","X3b":"t",    "fdL":"T",   "ZNp":"$","bTy":"u",    "NxZ":"U",   "GqF":"·","VkH":"v",    "nNa":"V",   "T9r":"!","nu6":"w",    "W":"j72",   "fhn":'"',"t75":"x",    "HuL":"X",   "Pcy":"ª","3QG":"y",    "LJt":"Y",   "bYV":"z",    "P7n":"Z",   "8bF":"|","6Ur":" "}
dic3= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9",":","-",".",",",";","_","+","*","`","´","?","'","¿","¡","=",")","(","/","|","ª","ç","¨","^","[","]","{","}","¬","~","#","@","|","€",'"',"!","·","$","%","&","á","à","é","è","í","ì","ó","ú","ù","ò"," "]
dic_custom = {}

# PRINCIPALS VARIABLES 

KEYLONG = 342
LENKEY_PROV = 0
barras = "-"*100
barras2 = "-"*25

# PRINCIPAL DEFS

    # Check is a valid

def check_key(keyGen):
    list1 =[]
    checking = keyGen
    tmp = ""
    
    while len(checking) != 0:  
        trimp = checking[0:3]
        checking = checking[3::]  
        if list1.count(trimp) == 0:
            list1.append(trimp)
            tmp += trimp
        else:
            i = 0
            while i != 3:
                i += 1
                tmp += generate_key()
    return tmp
        
    # Generate random letters and numbers whit probabilities
def generate_key():

    temp = random.randint(1,3)
    temp_key = ""
    if temp == 1 or temp == 2:
        temp_key += random.choice(string.ascii_letters)
    else:
        temp_key += str(random.choice(string.digits))
    return temp_key


cd = str(input(barras+"\n\n"+"Choose:\nC = Encrypt\nD = Desencrrypt\n\n"+barras+ "\n").lower())

if cd == "c":
    choose = int(input(barras+"\n\n"+"1 = Use Default Key\n2 = Use a custom key"+"\n\n"+barras+"\n"))

    # Use default diccionary

    if choose == 1:
        texto = str(input("Add text to encrypt: \n"))

        trad = ""
        for x in texto:
            trad += dic1[x]

        print("\n"+barras2 + "   CIPHERTEXT    "  + barras2 +  "\n\n"+trad+"\n\n"+barras)
    
    elif choose == 2:

        key = str(input("\n"+barras+"\n\n"+"Enter the key"+"\nPress Intro to generate random key\n\n"+barras+"\n"))
        LENKEY_PROV = len(key)


        # Check spaces and substitute
                
        key = key.replace(" ","")
        Qautotune = ""
        
        # Check long key

        if len(key) != 0:
            
            if LENKEY_PROV < KEYLONG or LENKEY_PROV > KEYLONG :
                Qautotune = str(input(barras+"\n\n\n\n\n\n\n"+f"ERROR 4050: The key length is too short or too long.( {KEYLONG} characters are required, your key has {LENKEY_PROV} characters)\n\nPress 'A' to key autotune or 'Q' for exit"+"\n"+barras+ "\n").lower())
                
                # EXIT ERROR 4050
    
                if Qautotune == "q": exit("\n\n\n\n\n\nGoodby World !\n\n\n\n\n\n")
            
            # AUTOTUNE KEY ----------------------------------- MUY MAL OPTIMIZADO -------------------------------------


        if LENKEY_PROV > KEYLONG:
            keyGen = ""

            while len(keyGen) != KEYLONG:
                keyGen += key[0:1]
                key = key[1::]
                
        if LENKEY_PROV < KEYLONG:
            keyGen = key
            while len(keyGen) != KEYLONG:
                keyGen += generate_key()
                      
        # CHECK ZONE
        if len(key) == KEYLONG:
            keyGen = key
        keyGen = check_key(keyGen)
            
        # Prints the key
        if Qautotune == "a":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras2+"   AUTOGENERATE KEY USED   "+ barras2 +"\n\n"+  keyGen + "\n\n" + barras )
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras2+"   KEY USED   "+ barras2 +"\n\n"+  keyGen + "\n\n" + barras)
            
    
#--------------------------------------------------------------- ADD TO CUSTOM DICCIONARY ---------------------------------------------------------------
        key2 = keyGen
        
        while len(key2)!= 0:
    
            temp =  key2[0:3]
            key2 = key2[3::]
            if len(dic3) != 0:
                dic_custom.update({dic3[0]:temp})
                dic3.pop(0)
#--------------------------------------------------------------- CIPHERTEXT ---------------------------------------------------------------
     
        texto = str(input("Add text to encrypt: \n"))
        trad = ""
        for x in texto:
            trad += dic_custom[x]
    
        print("\n"+barras2 + "   CIPHERTEXT    "  + barras2 +  "\n\n"+trad+"\n\n"+barras)

if cd == "d":
    choose = int(input("\n\n\n\n\n\n\n\n\n\n\n\n"+barras+"\n\n"+"DESENCRIPT"+"\n\n"+"1 = Use Default Key\n2 = Use a custom key"+"\n\n"+barras+"\n"))
    texto = str(input(barras +"\n\nAdd text to desencrypt: \n"))
    if choose == 1:
        trad = ""
        while len(texto) != 0:
            temp = texto[0:3]
            texto = texto[3::]
            if temp in dic2:
                trad += dic2[temp]  
            else:
                exit("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras + "   \n\nERROR 5010: The text introduced it's not compatible with default key\n\n" + barras+ "\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras2 + "   DECRYPTED TEXT   "  + barras2 +  "\n\n"+trad+"\n\n"+barras)
    if choose == 2:
        key = str(input("\n"+barras+"\n\nEnter the key: "+"\n\n"))
        
        # CHECK KEY 
        
        if len(key) != KEYLONG:
                exit("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras + "   \n\nERROR 5020: The key entered hasn't have characters than necessary\n\n" + barras+ "\n\n")

        for x in key:
            if x == " ":
                exit("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras + "   \n\nERROR 5030: The password entered is not valid (contains spaces)\n\n" + barras+ "\n\n")
        
        trad = ""
        
        # Add to custom dictionary
        
        while len(key)!= 0:
            temp =  key[0:3]
            key = key[3::]
            if len(dic2)!= 0:
                dic_custom.update({temp:dic3[0]})
                dic3.pop(0)
        
        # Translation
        
        while len(texto) != 0:
            temp = texto[0:3]
            texto = texto[3::]
            if temp in dic_custom:
                trad += dic_custom[temp]  
            else:
                exit("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras + "   \n\nERROR 5040: The text introduced it's not compatible with the key introduced\n\n" + barras+ "\n\n")
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+barras2 + "   DECRYPTED TEXT   "  + barras2 +  "\n\n"+trad+"\n\n"+barras)

# SCRIPT MADE BY YERAY on 2023-01-2023