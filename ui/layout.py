import flet as ft

#from ui.pages.exercise import build_exercises_page
#from ui.pages.workout_today import build_workout_today_page
#from ui.pages.settings import build_settings_page
from ui.pages.workout_today import workout_today_page



def render_app(page: ft.Page, state, render):
    # Limpa conteúdo principal
    page.controls.clear()

    # Escolhe página
    if state.route == "workout_today":
        content = workout_today_page(page)
        selected_index = 0
    elif state.route == "exercises":
        content = ft.Text("Exercises (em breve)")
        selected_index = 1
    else:
        content = ft.Text("Settings (em breve)")
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
