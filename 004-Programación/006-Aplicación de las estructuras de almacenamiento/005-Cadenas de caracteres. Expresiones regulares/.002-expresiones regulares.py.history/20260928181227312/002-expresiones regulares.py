import re

email_bueno = "info@jocarsa.com"
email_malo = "hola que tal"

patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

print(re.match(patron, email_bueno))  # Match
print(re.match(patron, email_malo))   # None