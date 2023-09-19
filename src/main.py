from person import Autor

def main() -> None:
    nombre = input("Digite el nombre del Autor: ")
    cedula = int(input("Digite la Cédula del autor: "))
    autor=Autor(nombre, cedula)
    print(autor)