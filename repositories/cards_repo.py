# repositories/cards_repo.py
from __future__ import annotations

from repositories.db import fetch_all


def list_active_template_cards() -> list[dict]:
    """
    Retorna os cards (prescrito + última vez) do programa ativo.
    """
    sql = """
    SELECT
      template_name,
      exercise_name,
      prescribed_sets,
      prescribed_reps,
      prescribed_notes,
      last_max_weight,
      last_top_reps,
      last_date
    FROM v_template_cards
    WHERE program_is_active = 1
      AND template_is_active = 1
    ORDER BY template_order, exercise_order;
    """
    return fetch_all(sql)
