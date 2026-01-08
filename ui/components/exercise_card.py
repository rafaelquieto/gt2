# ui/components/exercise_card.py
from __future__ import annotations

import flet as ft


def exercise_card(row: dict, on_save):
    """
    row: dict vindo da VIEW (template_name, exercise_name, prescribed_sets, etc.)
    on_save: callback(row, sets_payload) que será chamado ao salvar
    """

    template = row["template_name"]
    ex_name = row["exercise_name"]

    prescribed_sets = row["prescribed_sets"]
    prescribed_reps = row["prescribed_reps"]
    notes = row.get("prescribed_notes") or ""

    last_w = row.get("last_max_weight")
    last_reps = row.get("last_top_reps")
    last_date = row.get("last_date")

    last_line = "—"
    if last_date is not None:
        last_line = f"{last_w} kg x {last_reps} ( {last_date} )"

    # Inputs do modal (simples: um set por linha, você pode repetir sets rápido)
    weight = ft.TextField(label="Carga (kg)", keyboard_type=ft.KeyboardType.NUMBER)
    reps = ft.TextField(label="Reps", keyboard_type=ft.KeyboardType.NUMBER)
    rpe = ft.TextField(label="RPE (opcional)", keyboard_type=ft.KeyboardType.NUMBER)
    set_count = ft.TextField(label="Quantos sets?", value=str(prescribed_sets), keyboard_type=ft.KeyboardType.NUMBER)
    extra_notes = ft.TextField(label="Observação (opcional)", multiline=True, min_lines=2, max_lines=3)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text(f"Registrar: {ex_name}"),
        content=ft.Column(
            [
                ft.Text(f"Prescrito: {prescribed_sets} x {prescribed_reps}"),
                ft.Text(f"Última vez: {last_line}"),
                ft.Divider(),
                set_count,
                weight,
                reps,
                rpe,
                extra_notes,
            ],
            tight=True,
            width=420,
        ),
    )

    def open_dlg(e):
        e.page.dialog = dlg
        dlg.open = True
        e.page.update()

    def close_dlg(e):
        dlg.open = False
        e.page.update()

    def save(e):
        # validação mínima
        try:
            n_sets = int(set_count.value or "0")
        except ValueError:
            n_sets = 0

        if n_sets <= 0 or not reps.value:
            reps.error_text = "Informe reps"
            e.page.update()
            return

        payload = {
            "template_name": template,
            "exercise_name": ex_name,
            "n_sets": n_sets,
            "weight": float(weight.value) if (weight.value or "").strip() else None,
            "reps": int(reps.value),
            "rpe": float(rpe.value) if (rpe.value or "").strip() else None,
            "notes": (extra_notes.value or "").strip(),
        }

        on_save(row, payload)
        close_dlg(e)

    dlg.actions = [
        ft.TextButton("Cancelar", on_click=close_dlg),
        ft.FilledButton("Salvar", on_click=save),
    ]

    return ft.Card(
        content=ft.Container(
            padding=12,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(ex_name, size=16, weight=ft.FontWeight.BOLD),
                            ft.Container(expand=True),
                            ft.FilledButton("Registrar", on_click=open_dlg),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text(f"Prescrito: {prescribed_sets} x {prescribed_reps}"),
                    ft.Text(f"Obs: {notes}" if notes else "Obs: —"),
                    ft.Text(f"Última vez: {last_line}"),
                ],
                spacing=6,
            ),
        ),
    )
