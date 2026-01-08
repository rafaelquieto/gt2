PRAGMA foreign_keys = ON;

-- 1) programs
CREATE TABLE IF NOT EXISTS programs (
  program_id  INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT    NOT NULL UNIQUE,
  is_active   INTEGER NOT NULL DEFAULT 0 CHECK (is_active IN (0, 1)),
  created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- Garante que só exista 1 programa ativo (SQLite: índice parcial)
CREATE UNIQUE INDEX IF NOT EXISTS ux_one_active_program
ON programs(is_active)
WHERE is_active = 1;

-- 2) templates (dias A/B/etc dentro de um programa)
CREATE TABLE IF NOT EXISTS templates (
  template_id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id  INTEGER NOT NULL,
  name        TEXT    NOT NULL,                 -- ex.: 'A', 'B', 'Upper'
  is_active   INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1)),
  sort_order  INTEGER NOT NULL DEFAULT 1,

  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
  UNIQUE(program_id, name)
);

-- 3) exercises
CREATE TABLE IF NOT EXISTS exercises (
  exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT    NOT NULL UNIQUE,
  unit        TEXT    NOT NULL DEFAULT 'kg',
  is_active   INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
);

-- 4) template_exercises (prescrito)
CREATE TABLE IF NOT EXISTS template_exercises (
  template_exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
  template_id          INTEGER NOT NULL,
  exercise_id          INTEGER NOT NULL,
  prescribed_sets      INTEGER NOT NULL CHECK (prescribed_sets > 0),
  prescribed_reps      INTEGER NOT NULL CHECK (prescribed_reps > 0),
  notes                TEXT,
  sort_order           INTEGER NOT NULL DEFAULT 1,

  FOREIGN KEY (template_id) REFERENCES templates(template_id) ON DELETE CASCADE,
  FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id) ON DELETE RESTRICT,
  UNIQUE(template_id, exercise_id)
);

-- 5) workouts (executado)
CREATE TABLE IF NOT EXISTS workouts (
  workout_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  performed_at TEXT    NOT NULL,       -- ISO: '2026-01-07 05:10:00'
  program_id   INTEGER,                -- qual programa estava seguindo
  template_id  INTEGER,                -- qual template usou (A/B/etc)
  notes        TEXT,

  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE SET NULL,
  FOREIGN KEY (template_id) REFERENCES templates(template_id) ON DELETE SET NULL
);

-- 6) exercise_logs (nível de série)
CREATE TABLE IF NOT EXISTS exercise_logs (
  exercise_log_id INTEGER PRIMARY KEY AUTOINCREMENT,
  workout_id      INTEGER NOT NULL,
  exercise_id     INTEGER NOT NULL,
  set_number      INTEGER NOT NULL CHECK (set_number > 0),
  weight          REAL,
  reps            INTEGER NOT NULL CHECK (reps > 0),
  rpe             REAL,
  notes           TEXT,

  FOREIGN KEY (workout_id) REFERENCES workouts(workout_id) ON DELETE CASCADE,
  FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id) ON DELETE RESTRICT
);

-- Índices úteis
CREATE INDEX IF NOT EXISTS idx_workouts_performed_at ON workouts(performed_at);
CREATE INDEX IF NOT EXISTS idx_logs_exercise_id ON exercise_logs(exercise_id);
CREATE INDEX IF NOT EXISTS idx_logs_workout_id ON exercise_logs(workout_id);
