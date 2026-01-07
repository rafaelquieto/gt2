import flet as ft


def build_workout_today_page(page: ft.Page, state, render):
    return ft.Column(
        controls=[
            ft.Text("Treino de hoje", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("Em breve: selecionar exercícios e registrar séries."),
        ],
        expand=True,
        spacing=12,
    )
