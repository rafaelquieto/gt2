PRAGMA foreign_keys = ON;

DROP VIEW IF EXISTS v_template_cards;

CREATE VIEW v_template_cards AS
SELECT
  p.program_id,
  p.name AS program_name,
  p.is_active AS program_is_active,

  t.template_id,
  t.name AS template_name,
  t.is_active AS template_is_active,
  t.sort_order AS template_order,

  te.sort_order AS exercise_order,

  e.exercise_id,
  e.name AS exercise_name,

  te.prescribed_sets,
  te.prescribed_reps,
  COALESCE(te.notes, '') AS prescribed_notes,

  lw.performed_at AS last_date,
  ll.last_sets,
  ll.last_max_weight,
  ll.last_top_reps

FROM programs p
JOIN templates t ON t.program_id = p.program_id
JOIN template_exercises te ON te.template_id = t.template_id
JOIN exercises e ON e.exercise_id = te.exercise_id

-- último treino (data) em que o exercício apareceu
LEFT JOIN (
  SELECT
    el.exercise_id,
    MAX(w.performed_at) AS performed_at
  FROM exercise_logs el
  JOIN workouts w ON w.workout_id = el.workout_id
  GROUP BY el.exercise_id
) lw ON lw.exercise_id = e.exercise_id

-- agregados do último treino (sets / max weight / top reps)
LEFT JOIN (
  SELECT
    el.exercise_id,
    el.workout_id,
    COUNT(*) AS last_sets,
    MAX(el.weight) AS last_max_weight,
    MAX(el.reps) AS last_top_reps
  FROM exercise_logs el
  GROUP BY el.exercise_id, el.workout_id
) ll
  ON ll.exercise_id = e.exercise_id
 AND ll.workout_id = (
   SELECT w2.workout_id
   FROM workouts w2
   JOIN exercise_logs el2 ON el2.workout_id = w2.workout_id
   WHERE el2.exercise_id = e.exercise_id
   ORDER BY w2.performed_at DESC
   LIMIT 1
 );
