
#Crear md5 

import os
import hashlib 

def main():
    ingresar = raw_input("Introduce la palabra que quieres encriptar: ")

    md5 = hashlib.md5(ingresar).hexdigest()
    print("El hash es: " + md5)


if __name__ == '__main__':
    main()



