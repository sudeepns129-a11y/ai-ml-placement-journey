# Week 24 project: Student Performance Prediction (synthetic data only)

## Purpose and safety

Build a small, reproducible machine-learning demonstration that predicts a clearly defined outcome from invented student-like records. This is an educational exercise only. Do not collect, publish, or use real student data, and do not use the model to make decisions about students. A small example cannot establish that a model is fair, useful, or accurate in real settings.

## Suggested project steps

1. **Describe the dataset:** State that every row and value is synthetic. Document the columns, units, target, and how the records were created.
2. **Clean and inspect:** Check column types, missing values, duplicates, and value ranges. Explain any cleaning decisions and report row counts before and after.
3. **Explore:** Summarize distributions and relationships with small tables or charts. Avoid interpreting correlation as causation.
4. **Select features:** Identify inputs and target. Exclude identifiers and any information that would only be known after the outcome. Explain why the selected features are appropriate for this demonstration.
5. **Train a baseline:** Split the synthetic data before fitting transformations or a model. Compare a simple baseline with one model using a suitable metric.
6. **Evaluate honestly:** Report the split and metric, check at least one failure mode, and state that results on invented data say nothing about real student performance.
7. **Make it reproducible:** Record the Python and package requirements for the exercise, seed/randomness choices, run command, and expected output. Do not commit generated model files or private data.

## Small deliverable

Create a short report and runnable script or notebook. Keep the code small enough to explain; do not add an API or complex model for this exercise.

## Acceptance checklist

- [ ] State the problem and intended audience in plain language.
- [ ] Confirm the dataset is synthetic and describe its columns.
- [ ] Document cleaning and exploratory-analysis steps.
- [ ] Explain feature selection and how leakage was avoided.
- [ ] Compare a simple baseline with a model using a suitable metric.
- [ ] Include limitations and reproducible run instructions.
- [ ] Confirm no real or sensitive student information is present.

Do not claim model quality, real-world usefulness, business impact, placement readiness, or mastery without evidence.
