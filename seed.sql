-- Programa ativo
INSERT INTO programs (name, is_active) VALUES ('Força 2026 Q1', 1);

-- Templates A e B
INSERT INTO templates (program_id, name, is_active, sort_order)
VALUES
((SELECT program_id FROM programs WHERE name='Força 2026 Q1'), 'A', 1, 1),
((SELECT program_id FROM programs WHERE name='Força 2026 Q1'), 'B', 1, 2);

-- Exercícios
INSERT INTO exercises (name, unit, is_active) VALUES
('Supino reto', 'kg', 1),
('Agachamento', 'kg', 1),
('Remada', 'kg', 1);

-- Prescrição do template A
INSERT INTO template_exercises (template_id, exercise_id, prescribed_sets, prescribed_reps, notes, sort_order)
VALUES
((SELECT template_id FROM templates WHERE name='A' AND program_id=(SELECT program_id FROM programs WHERE name='Força 2026 Q1')),
 (SELECT exercise_id FROM exercises WHERE name='Supino reto'),
 3, 8, 'RPE ~8', 1);

INSERT INTO template_exercises (template_id, exercise_id, prescribed_sets, prescribed_reps, notes, sort_order)
VALUES
((SELECT template_id FROM templates WHERE name='A' AND program_id=(SELECT program_id FROM programs WHERE name='Força 2026 Q1')),
 (SELECT exercise_id FROM exercises WHERE name='Remada'),
 3, 10, '', 2);

-- Prescrição do template B
INSERT INTO template_exercises (template_id, exercise_id, prescribed_sets, prescribed_reps, notes, sort_order)
VALUES
((SELECT template_id FROM templates WHERE name='B' AND program_id=(SELECT program_id FROM programs WHERE name='Força 2026 Q1')),
 (SELECT exercise_id FROM exercises WHERE name='Agachamento'),
 3, 5, 'subir carga quando fechar reps', 1);
