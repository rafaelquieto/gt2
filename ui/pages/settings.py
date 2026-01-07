import flet as ft


def build_settings_page(page: ft.Page, state, render):
    return ft.Column(
        controls=[
            ft.Text("Configurações", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("Em breve: exportar CSV, unidades (kg), etc."),
        ],
        expand=True,
        spacing=12,
    )
