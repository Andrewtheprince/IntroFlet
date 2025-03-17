from time import sleep

import flet as ft
from flet.core.types import TextAlign


def main(page: ft.Page):
    page.bgcolor="white"

    #1) Scrivere del testo

    myText=ft.Text(value="Buongiorno", color="green", size=30)
    page.controls.append(myText)
    page.update()
    myCounter = ft.Text(value="")
    page.controls.append(myCounter)
    for i in range(100):
        myCounter.value = f"Counter: {i}"
        myCounter.color=ft.colors.random()
        page.update()

    #2) Creare un campo in cui l'utente può scrivere del testo

    txtIn = ft.TextField(label="Nome", value="Andrea", color="green", disabled=False)
    page.add(txtIn) #Equivale a page.controls.append seguito da page.update

    #3) Creare dei bottoni, alla pressione del quale eseguo del codice

    def handleBtnSaluta(e):
        txtOut.value = f"Ciao {txtIn.value}!"
        txtIn.value=""
        page.update()

    btnSaluta = ft.ElevatedButton(text="Saluta", on_click=handleBtnSaluta)
    txtOut = ft.Text(value="Come ti chiami?")

    row3 = ft.Row(controls=[btnSaluta, txtOut])

    page.add(row3)

    #4) Creare un menu a tendina

    dd=ft.Dropdown(label="Opzioni", hint_text="Seleziona opzione" ,options=[ft.dropdown.Option("Opzione 1"), ft.dropdown.Option("Opzione 2")])
    for i in range(3,20):
        dd.options.append(ft.dropdown.Option(f"Opzione {i}"))
    page.add(dd)

    #5) Visualizzare lunghi elenchi di testo

    def handleAddLV(e):
        if txtIn2.value=="":
            lv.controls.append(ft.Text("Errore, aggiungi una stringa valida", color = "red"))
            page.update()
        else:
            lv.controls.append(ft.Text(txtIn2.value))
            page.update()

    txtIn2=ft.TextField(label="Stringa input")
    btnIn2 = ft.CupertinoButton(text="Aggiungi a listView", on_click=handleAddLV, color="white", bgcolor="Blue")

    row5 = ft.Row(controls = [txtIn2, btnIn2], alignment=ft.MainAxisAlignment.CENTER)

    lv = ft.ListView(expand=1, padding=20,spacing=10 ,auto_scroll=True)
    page.add(row5, lv)


ft.app(target = main, view=ft.AppView.FLET_APP)