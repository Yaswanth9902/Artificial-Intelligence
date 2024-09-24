% Facts defining dietary recommendations
diet(diabetes, low_sugar).
diet(hypertension, low_sodium).
diet(cholesterol, low_fat).
diet(obesity, low_calorie).

% Rule to suggest diet based on disease
suggest_diet(Disease) :-
    diet(Disease, Diet),
    write('Suggested diet: '), write(Diet), nl.

% Example queries:
% ?- suggest_diet(diabetes).
% ?- suggest_diet(obesity).
