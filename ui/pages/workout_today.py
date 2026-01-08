# ui/pages/workout_today.py
from __future__ import annotations

import flet as ft

from repositories.cards_repo import list_active_template_cards
from ui.components.exercise_card import exercise_card


def workout_today_page(page: ft.Page):
    """
    Página: lista templates e seus exercícios (cards).
    """
    rows = list_active_template_cards()

    # Agrupar por template_name (A, B, etc.)
    grouped: dict[str, list[dict]] = {}
    for r in rows:
        grouped.setdefault(r["template_name"], []).append(r)

    snackbar = ft.SnackBar(content=ft.Text(""))

    def notify(msg: str):
        snackbar.content = ft.Text(msg)
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

    def on_save(row: dict, payload: dict):
        # Por enquanto só confirma na tela (depois gravamos no SQLite)
        notify(
            f"Salvo: {payload['exercise_name']} - "
            f"{payload['n_sets']} sets de {payload['reps']} reps @ {payload['weight']}kg"
        )

    sections: list[ft.Control] = []

    for template_name, items in grouped.items():
        sections.append(ft.Text(f"Treino {template_name}", size=20, weight=ft.FontWeight.BOLD))
        for r in items:
            sections.append(exercise_card(r, on_save))
        sections.append(ft.Divider())

    return ft.Column(sections, scroll=ft.ScrollMode.AUTO, expand=True)
