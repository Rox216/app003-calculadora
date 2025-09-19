import flet as ft
import math


def main(page: ft.Page):
    page.tittle = "calculadora simple w"
    page.bgcolor = ft.Colors.YELLOW_800

    titulo = ft.Text(        "Calculadora basica p",
        size=28,
        color=ft.Colors.BLACK87
        text_align="center",
        weight="bold"
    )

    
    
    num1 = ft.TextField(
        label="Numero 1",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.BLACK87)
    )
    num2 = ft.TextField(
        label="Numero 2",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.BLACK87)
    )
    resultado = ft.Text(
        value="Resultado",
        size=20,
        color=ft.Colors.BLACK87,
        text_align="center"
    )
    
    info = ft.Container(
        content=ft.Text(
            "Para el boton porcentaje: el campo de arriba es el numero base y el de abajo es el porcentaje (%) que quieres calcular"
            size=13,
            color=ft.Colors.BLACK87,
            text_align="center",
            italic=True
            max_lines=2,
            overflow="clip"
        ),
        alignment=ft.alignment.center,
        width=400,
        padding=5
    )
    
    def mostrar_resultado(valor):
        resultado.value = f"Resultado: {valor}"
        page.update()
        
    def suma(e):
        try:
            res = float(num1.value) + float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def resta(e):
        try:
            res = float(num1.value) - float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def multiplicacion(e):
        try:
            res = float(num1.value) * float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def division(e):
        try:
            res = float(num1.value) / float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def porcentaje(e):
        try:
            res = (float(num1.value) * float(num2.value)) / 100
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def raiz_cuadrada(e):
        try:
            res1 = math.sqrt(float(num1.value))
            res2 = math.sqrt(float(num2.value))
            mostrar_resultado(f"√")
                  
    page.add()


ft.app(main)
