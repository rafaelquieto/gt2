#estad do app
#guarda lista de exercícios em memória
#guarda página atual


"""
PASSO 1
Tarefa: crie um AppState com:

exercises: list[str]

route: str (ex.: "exercises")

"""
from dataclasses import dataclass, field


@dataclass
class AppState:
    # rota/página atual
    route: str = "exercises"  # "workout_today", "settings"

    # dados em memória (MVP)
    exercises: list[str] = field(default_factory=list)    #a funcao list cria uma lista nova e virgem para essa instancia. garante que se eu adicionar um exercicio para o dia 1 ele nao sera adicinado tambe ao dia dois
