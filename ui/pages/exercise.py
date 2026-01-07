""" 
Componentes mínimos:

Título “Exercícios”

TextField “Nome do exercício”

Botão “Adicionar”

Lista dos exercícios adicionados (com botão de remover ao lado)

Regra declarativa: a lista na tela é sempre re-renderizada a partir de state.exercises.
"""
import flet as ft


def build_exercises_page(page: ft.Page, state, render):
    name_tf = ft.TextField(
        label="Nome do exercício",
        hint_text="Ex.: Supino reto",
        autofocus=True,
        expand=True,
    )

    def add_exercise(_):
        name = (name_tf.value or "").strip()
        if not name:
            return
        state.exercises.append(name)
        name_tf.value = ""
        render()

    def remove_exercise(name: str):
        def _handler(_):
            if name in state.exercises:
                state.exercises.remove(name)
            render()
        return _handler

    items = []
    for ex in state.exercises:
        items.append(
            ft.Row(
                controls=[
                    ft.Text(ex, expand=True),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Remover",
                        on_click=remove_exercise(ex),
                    ),
                ]
            )
        )

    return ft.Column(
        controls=[
            ft.Text("Exercícios", size=22, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    name_tf,
                    ft.ElevatedButton("Adicionar", on_click=add_exercise),
                ]
            ),
            ft.Divider(),
            ft.Text(f"Total: {len(state.exercises)}"),
            ft.Column(
                controls=items,
                spacing=6,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
        ],
        expand=True,
        spacing=12,
    )
