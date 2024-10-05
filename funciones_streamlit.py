#Oscar Manuel Gutierrez Camberos   Tarea: Funciones(1)
import streamlit as st

def saludo(nombre):
    st.write(f"Hola {nombre}")

def sumar(a,b):
    return a+b

def calcular_area_triangulo(base,altura):
    return base*altura/2

def calcular_precio_final(precio_original,descuento,impuesto):
    return (precio_original-precio_original*(descuento/100))+precio_original*impuesto/100

def sumar_lista(lista):
    return sum(lista)

def producto(nombre,cantidad,precio):
    return (f"{cantidad} {nombre}, TOTAL = ${cantidad*precio}")

def numeros_pares_e_impares(lista):
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    st.write(f"Los números pares son: {pares}   Los números impares son: {impares}")

def multiplicar_todos(*args):
    resultado=1
    for i in args:
        resultado*=i
    return resultado

def informacion_personal(**kwargs):
    for key, value in kwargs.items():
        st.write(f"{key}: {value}")

def calculadora_flexible(a,b,c):
    match c:
        case "+":
            return (f"{a} + {b} = ",a+b)
        case "-":
            return (f"{a} - {b} = ",a-b)
        case "*":
            return (f"{a} * {b} = ",a*b)
        case "/":
            return (f"{a} / {b} = ",a/b)
        case _:
            return "Operación no válida"

st.title("Menú de funciones")
st.subheader("Selecciona una opción")
opc=st.selectbox("",["Saludo","Suma","Área de un triángulo","Precio final","Suma de una lista","Producto","Pares e impares","Multiplicar lista","Información personal","Calculadora flexible"])
match opc:
    case "Saludo":
        nombre=st.text_input("Escribe tu nombre")
        saludo(nombre)

    case "Suma":
        n1=st.number_input("Escribe el primer número")
        n2=st.number_input("Escribe el segundo número")
        st.write("La suma es: ",sumar(n1,n2))

    case "Área de un triángulo":
        base=st.number_input("Escribe la medida de la base del triángulo")
        altura=st.number_input("Escribe la medida de la altura del triángulo")
        st.write(f"El área del triángulo es: ",calcular_area_triangulo(base,altura))

    case "Precio final": 
        precio_original=st.number_input("Escribe el precio original")
        descuento=st.number_input("Escribe el descuento")
        impuesto=st.number_input("Escribe el impuesto")
        st.write("El precio final es: ",calcular_precio_final(precio_original,descuento,impuesto))

    case "Suma de una lista":
        lista=st.text_input("Escribe los números de la lista separados por comas")
        try:
            if lista!="":
                lista=lista.split(",")
                lista=[int(i) for i in lista]
                st.write("La suma de la lista es:",sumar_lista(lista))
        except ValueError:
            st.write("Se ingresó un valor erróneo")
        

    case "Producto":
        product=st.text_input("Escribe el nombre del producto")
        cantidad=st.number_input("Escribe la cantidad de productos")
        precio=st.number_input("Escribe el precio del producto")
        st.write(producto(product,cantidad,precio))

    case "Pares e impares":
        lista=st.text_input("Escribe los números de la lista separados por comas")
        if lista!="":
            lista=lista.split(",")
            lista=[int(i) for i in lista]
        st.write(numeros_pares_e_impares(lista))

    case "Multiplicar lista":
        lista=st.text_input("Ingresa los números a multiplicar separados por comas")
        try:
            numeros=[int(num) for num in lista.split(",")]
            resultado=multiplicar_todos(*numeros)
            st.write(f"El resultado de multiplicar todos los números es: {resultado}")
        except ValueError:
            st.write("Se ingresió un valor erróneo")

    case "Información personal":
        name=st.text_input("Escribe tu nombre")
        age=st.number_input("Escribe tu edad")
        city=st.text_input("Escribe tu ciudad")
        st.write(informacion_personal(Nombre=(name),Edad=(age),Ciudad=(city)))

    case "Calculadora flexible":
        n1=st.number_input("Escribe el primer número")
        n2=st.number_input("Escribe el segundo número")
        op=st.selectbox("Selecciona una operación",["+","-","*","/"])        
        st.write(calculadora_flexible(n1,n2,op))