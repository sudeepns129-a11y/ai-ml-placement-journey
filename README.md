# AI/ML Placement Journey

## Project objective

A beginner-friendly, year-long learning plan for a second-year BTech CSE/AIML student preparing for entry-level AI/ML, data, Python, and related software roles. The personal salary target is INR 6-10 LPA; this plan cannot guarantee placement or salary outcomes.

This repository records practice and projects. **A planned week or example file does not mean the topic is mastered.** The aim is to understand concepts, solve exercises independently, build small projects, and explain limitations.

## Current status

- Weeks 1-4: concepts covered; independent practice in progress.
- Weeks 5-52: structured learning plan created; not completed.
- Start with [Week 5: Statistics foundations](week-05-statistics-foundations/README.md) and its [five-day plan](week-05-statistics-foundations/learning-plan.md).
- See [PROGRESS.md](PROGRESS.md) for self-updated checkboxes and [ROADMAP.md](ROADMAP.md) for all 52 weeks.

## Roadmap at a glance

### Phase 1 - Weeks 1-8: Foundations
[Weeks 1-2 Python fundamentals](week-01-02-python-basics/) | [Week 3 Python projects](week-03-python-projects/) | [Week 4 NumPy](week-04-numpy/) | [Week 4 pandas](week-04-pandas/). Continue with [Week 5 statistics](week-05-statistics-foundations/README.md), [Week 6 probability](week-06-probability-for-ml/README.md), [Week 7 SQL](week-07-sql-fundamentals/README.md), and [Week 8 DSA](week-08-python-dsa-practice/README.md).

### Phase 2 - Weeks 9-12: Data preparation and analysis
[Week 9 cleaning](week-09-data-cleaning/README.md) | [Week 10 EDA](week-10-exploratory-data-analysis/README.md) | [Week 11 features](week-11-feature-engineering/README.md) | [Week 12 visualization](week-12-visualization-and-insights/README.md)

### Phase 3 - Weeks 13-16: ML fundamentals
[Week 13 foundations](week-13-machine-learning-fundamentals/README.md) | [Week 14 regression](week-14-linear-and-logistic-regression/README.md) | [Week 15 classification](week-15-classification-algorithms/README.md) | [Week 16 evaluation](week-16-model-evaluation/README.md)

### Phase 4 - Weeks 17-20: Model improvement
[Week 17 trees](week-17-decision-trees/README.md) | [Week 18 forests](week-18-random-forests/README.md) | [Week 19 validation and tuning](week-19-cross-validation-and-tuning/README.md) | [Week 20 unsupervised learning](week-20-unsupervised-learning/README.md)

### Phase 5 - Weeks 21-24: SQL, DSA, and first ML project
[Week 21 SQL](week-21-sql-intermediate/README.md) | [Week 22 DSA](week-22-dsa-practice/README.md) | [Week 23 project development](week-23-ml-project-development/README.md) | [Week 24 student-performance demo](week-24-student-performance-prediction/README.md) - synthetic records only.

### Phase 6 - Weeks 25-28: Deep learning and PyTorch
[Week 25 concepts](week-25-deep-learning-fundamentals/README.md) | [Week 26 PyTorch](week-26-pytorch-basics/README.md) | [Week 27 networks](week-27-neural-networks/README.md) | [Week 28 project](week-28-deep-learning-project/README.md)

### Phase 7 - Weeks 29-32: NLP, transformers, and LLMs
[Week 29 NLP](week-29-nlp-fundamentals/README.md) | [Week 30 text processing](week-30-text-processing/README.md) | [Week 31 transformers](week-31-transformers-and-llms/README.md) | [Week 32 embeddings and search](week-32-embeddings-and-semantic-search/README.md)

### Phase 8 - Weeks 33-36: AI applications
[Week 33 application development](week-33-ai-application-development/README.md) | [Week 34 recommenders](week-34-recommendation-systems/README.md) | [Week 35 AI Career Assistant](week-35-ai-career-assistant/README.md) | [Week 36 safeguards and improvements](week-36-ai-project-improvements/README.md)

### Phase 9 - Weeks 37-40: Backend, frontend, and deployment
[Week 37 FastAPI](week-37-fastapi-fundamentals/README.md) | [Week 38 model API](week-38-model-api-development/README.md) | [Week 39 React integration](week-39-react-frontend-integration/README.md) | [Week 40 Docker and deployment](week-40-deployment-and-docker/README.md)

### Phase 10 - Weeks 41-44: Projects and portfolio
[Week 41 end-to-end ML](week-41-end-to-end-ml-project/README.md) | [Week 42 testing](week-42-testing-and-code-quality/README.md) | [Week 43 portfolio](week-43-portfolio-and-github/README.md) | [Week 44 documentation](week-44-project-documentation/README.md)

### Phase 11 - Weeks 45-48: Interviews
[Week 45 DSA](week-45-dsa-interview-practice/README.md) | [Week 46 SQL](week-46-sql-interview-practice/README.md) | [Week 47 ML](week-47-ml-interview-preparation/README.md) | [Week 48 projects and HR](week-48-project-and-hr-interviews/README.md)

Aim to work toward roughly 120-180 well-understood DSA problems over the year, adjusting the pace to your progress rather than copying solutions.

### Phase 12 - Weeks 49-52: Placement readiness
[Week 49 resume](week-49-resume-and-linkedin/README.md) | [Week 50 mock interviews](week-50-mock-interviews/README.md) | [Week 51 applications](week-51-placement-applications/README.md) | [Week 52 continued plan](week-52-final-review-and-placement-plan/README.md)

The [complete weekly scope and deliverables](ROADMAP.md) and [progress checklist](PROGRESS.md) are maintained separately.

## Skills and tools covered

Python; NumPy; pandas; statistics and probability; SQL and SQLite; problem-solving and DSA; data cleaning, EDA, and visualization; scikit-learn and model evaluation; PyTorch; NLP, transformers, embeddings, and retrieval; FastAPI; React integration; testing, Git/GitHub, Docker, documentation, and interview preparation.

Future libraries are introduced in their relevant weeks rather than installed all at once. The root [requirements.txt](requirements.txt) contains only dependencies used by the current Weeks 1-4 code.

## Setup and running code

Use Windows PowerShell from the repository root. Confirm Python is installed with python --version (or use py if that's the command on your machine). Install current dependencies with:

`powershell
python -m pip install -r requirements.txt
`

Run current examples from the repository root:

`powershell
python .\week-01-02-python-basics\even_odd.py
python .\week-04-numpy\numpy_day1.py
python .\week-04-pandas\pandas_day3.py
`

Weekly starter files may intentionally contain TODOs and may require a library that is introduced later. Read that week's setup notes before installing anything. Do not run a starter as though it were a finished project.

## Current project portfolio

- **Expense Tracker 2.0:** small menu-based JSON exercise; personal expenses.json remains local and is ignored by Git.
- **Calculator and file-handling exercise:** basic arithmetic, and reading/writing a local note.
- **NumPy marks exercises:** arrays, arithmetic, filtering, and summary statistics.
- **Pandas student-data exercises:** sample CSV inspection and a basic analysis report.
- Weeks 5-52: proposed practice and project milestones, not completed portfolio claims.

## Future learning goals

Build a stronger foundation in statistics, probability, SQL, and DSA; practise data cleaning and exploratory analysis; learn and evaluate machine-learning models; then progress to deep learning, NLP, and responsible AI applications. Build practical AI/ML projects and use them to practise APIs, deployment, documentation, and testing. Finish by reviewing portfolio evidence and preparing for relevant entry-level roles. The INR 6-10 LPA salary target is aspirational, not a promised outcome.

The Week 24 student-performance prediction task must use synthetic data only and must not be used to make real decisions about students. Use only appropriately licensed, non-sensitive datasets elsewhere; cite the source and explain limitations.

## Learning resources

Weekly guides link to official or reputable documentation where available. These links were checked while preparing this roadmap; websites and library instructions can change, so follow the current official setup guidance. Free reading and local exercises are preferred; paid APIs are not required for the core plan.

## Safe repository habits

Keep credentials, .env files, virtual environments, generated models, logs, private data, and real expense records out of Git. .gitignore prevents new accidental additions but does not erase anything already present in Git history. Review git status and the diff before committing.