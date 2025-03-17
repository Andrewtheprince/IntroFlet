from time import sleep

import flet as ft
from flet.core.types import TextAlign


def main(page: ft.Page):

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
        sleep(0.5)

    #2) Creare un campo in cui l'utente può scrivere del testo


    #3) Creare dei bottoni, alla pressione del quale eseguo del codice

    #4) Creare un menu a tendina

    #5) Visualizzare lunghi elenchi di testo

ft.app(target = main, view=ft.AppView.FLET_APP)