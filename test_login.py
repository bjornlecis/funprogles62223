gebruikers = {"user":"jan","wachtwoord":"1234"}
user = input("geef gebruiker")
ww = input("geef wachtwoord")

if gebruikers["user"] == user and gebruikers["wachtwoord"] == ww:
    print("inlog gelukt")
else:
    print("verkeerd username of password")
