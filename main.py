"""
apredizado sobre app declarativo
eventos (cliques) vao mudar o state
chamam render()
"""
import flet as ft

from ui.state import AppState
from ui.layout import render_app


def main(page: ft.Page):
    # Configuração básica da janela / página
    page.title = "GymTracker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 12

    # 1) Estado central do app (em memória)
    state = AppState()

    # 2) Função render: redesenha a UI a partir do estado (declarativo)
    def render():
        render_app(page, state, render)

    # 3) Primeiro desenho da tela
    render()

if __name__ == "__main__":
    ft.run(main=main, view=ft.AppView.WEB_BROWSER)


