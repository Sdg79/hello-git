# Guardo datos en un texto para probar GitHub Actions
import xml
import os
from datetime import datetime

# .txt file

now = datetime.now()

# escribir
txt_file = open("c:/Users/SergioDGiovagnoli/Documents/Git/Hello Git/texto.txt", "a+")

txt_file.write(
    "\nEjecución de GibHub Actions: " + str(now))
print(now)

# Cierra el fichero
txt_file.close()
