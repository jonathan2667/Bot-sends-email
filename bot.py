
import smtplib

print("Scrie pe rand, cate un mesaj pe care vrei sa il trimiti.")
mesaj = str(input("1 : "))

print("Logheaza-te la gmail !")

emitator = str((input("Adresa ta de gmail : ")))
parola = str((input("Parola ta de la gmail : ")))
receptor1 = str((input("Adresa celui ce ii trimiti mail-ul : ")))
receptor2 = str((input("Adresa celui ce ii trimiti mail-ul : ")))
receptor3 = str((input("Adresa celui ce ii trimiti mail-ul : ")))

print("Te-ai logat cu succes !")

nr_email = int(input("Numar de email-uri pe care vrei sa le trimiti : "))
for i in range(nr_email):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(emitator, parola)
    server.sendmail(emitator, receptor1, mesaj)
    server.sendmail(emitator, receptor2, mesaj)
    server.sendmail(emitator, receptor3, mesaj)
    print("Mail cu mesajul " + str(i) +  "trimis cu succes !")
