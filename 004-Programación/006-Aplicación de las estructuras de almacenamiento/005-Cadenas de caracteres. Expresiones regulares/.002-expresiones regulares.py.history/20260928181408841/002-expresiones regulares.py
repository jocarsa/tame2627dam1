import re

email_bueno = "info@jocarsa.com"
email_malo = "hola que tal"

patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
patron2 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 

print(re.match(patron2, email_bueno))  # Match
print(re.match(patron2, email_malo))   # None