import flet as ft

from ui.pages.exercise import build_exercises_page
from ui.pages.workout_today import build_workout_today_page
from ui.pages.settings import build_settings_page


def render_app(page: ft.Page, state, render):
    # Limpa conteúdo principal
    page.controls.clear()

    # Escolhe página
    if state.route == "workout_today":
        content = build_workout_today_page(page, state, render)
        selected_index = 0
    elif state.route == "exercises":
        content = build_exercises_page(page, state, render)
        selected_index = 1
    else:
        content = build_settings_page(page, state, render)
        selected_index = 2

    # NavigationBar: no Flet atual, é idiomático usar page.navigation_bar
    def on_nav_change(e: ft.ControlEvent):
        idx = int(e.control.selected_index)
        state.route = ["workout_today", "exercises", "settings"][idx]
        render()

    page.navigation_bar = ft.NavigationBar(
        selected_index=selected_index,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label="Treino"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST_ALT, label="Exercícios"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Config"),
        ],
    )

    # Conteúdo principal
    page.add(content)

    page.update()
