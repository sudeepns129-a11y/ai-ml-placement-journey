# Week 10: Exploratory data analysis
# Follow the TODO prompts in README.md in this exercises folder.
import pandas as pd

data = pd.DataFrame(
    {"name": ["A", "B", "B"], "score": [80, None, 80], "group": ["x", "X", "x"]}
)

# TODO: inspect shape, data types, missing values, and duplicate rows.
# TODO: choose and document a rule for inconsistent group labels.
# TODO: verify the row count and missing-value count after cleaning.
print(data)