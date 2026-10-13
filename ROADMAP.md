# 52-Week AI/ML Placement Preparation Roadmap

This is a paced learning plan, not a completion claim or placement guarantee. Weeks 1-4 cover foundational concepts; independent practice continues. Weeks 5-52 are planned, not completed.

Plan for about five study sessions each week. If a prerequisite or exercise is unclear, repeat the week or slow down rather than rushing onward. Projects use synthetic or appropriately licensed public data and should explain limitations.

Across the year, aim for roughly 120-180 well-understood DSA problems, paced to your progress; focus on independent reasoning rather than copying solutions.

## Current foundation: Weeks 1-4

- [Weeks 1-2: Python fundamentals](week-01-02-python-basics/) - concepts covered; independent practice in progress.
- [Week 3: Python projects](week-03-python-projects/) - file handling, exceptions, modules, and Expense Tracker 2.0; independent practice in progress.
- [Week 4: NumPy](week-04-numpy/) and [pandas](week-04-pandas/) - concepts covered; independent practice in progress.

## Phase 1: Statistics, probability, SQL, and Python problem-solving (Weeks 5-8)

- [Week 5: Statistics foundations](week-05-statistics-foundations/README.md) - Mean, median, and mode, range, variance, and standard deviation, quartiles and outliers, sample versus population, robust summaries. **Build:** Create a one-page descriptive-statistics report from invented marks; include units and a short interpretation
- [Week 6: Probability for machine learning](week-06-probability-for-ml/README.md) - Events and sample spaces, complements and conditional probability, independent and dependent events, simple discrete distributions, simulation and expected value. **Build:** Build a reproducible coin/dice simulator and compare empirical frequencies with theoretical probabilities
- [Week 7: SQL fundamentals](week-07-sql-fundamentals/README.md) - Tables and keys, SELECT, WHERE, ORDER BY, aggregates and GROUP BY, NULL handling, INSERT, UPDATE, DELETE, and basic joins. **Build:** Create a small local SQLite schema and a query notebook/script of answered questions; never store real personal data
- [Week 8: Python DSA practice](week-08-python-dsa-practice/README.md) - Big-O intuition, arrays and strings, dictionaries and sets, linear and binary search, sorting, test cases and edge cases. **Build:** Solve and explain five easy problems with tests and complexity notes; focus on understanding, not speed

## Phase 2: Data preparation and analysis (Weeks 9-12)

- [Week 9: Data cleaning with pandas](week-09-data-cleaning/README.md) - Inspect columns and types, missing values, duplicates, inconsistent categories, safe conversion, record each cleaning decision. **Build:** Create a cleaning script and data-quality report using synthetic or appropriately licensed data
- [Week 10: Exploratory data analysis](week-10-exploratory-data-analysis/README.md) - Question-first analysis, distributions, group summaries, relationships, missingness, avoid causal claims from correlation. **Build:** Produce a short EDA report on a small synthetic or appropriately licensed public dataset
- [Week 11: Feature engineering](week-11-feature-engineering/README.md) - Feature versus target, categorical encoding, scaling, dates and simple derived variables, leakage, fit transformations only on training data. **Build:** Prepare a documented feature table without using post-outcome or private information
- [Week 12: Visualization and insights](week-12-visualization-and-insights/README.md) - Choose charts for questions, labels and units, distributions and comparisons, accessible color choices, honest captions. **Build:** Build a small visual report with a question, chart, finding, caveat, and data citation

## Phase 3: Machine learning fundamentals (Weeks 13-16)

- [Week 13: Machine learning fundamentals](week-13-machine-learning-fundamentals/README.md) - Supervised versus unsupervised learning, features and targets, train/test split, fit and predict, baseline, generalization. **Build:** Compare a simple baseline with one model on a small synthetic dataset; document the split
- [Week 14: Linear and logistic regression](week-14-linear-and-logistic-regression/README.md) - Regression targets, line and residual intuition, logistic probabilities, decision thresholds, scale and assumptions. **Build:** Compare a regression baseline and classifier on small synthetic data; report errors without overstating results
- [Week 15: Classification algorithms](week-15-classification-algorithms/README.md) - Class labels, k-nearest neighbors, naive Bayes, support-vector intuition, scaling, decision boundaries. **Build:** Run a controlled classifier comparison and explain when accuracy alone is misleading
- [Week 16: Model evaluation](week-16-model-evaluation/README.md) - Confusion matrix, accuracy, precision, recall, F1, MAE, MSE, RMSE, thresholds, class imbalance, validation versus test. **Build:** Write an evaluation report that separates validation choices from the final test result

## Phase 4: Model improvement (Weeks 17-20)

- [Week 17: Decision trees](week-17-decision-trees/README.md) - Splits and impurity intuition, depth, overfitting, feature importance caveats, interpretability and limits. **Build:** Explain a tree model with a small, non-sensitive dataset and a clear caveat
- [Week 18: Random forests](week-18-random-forests/README.md) - Ensembles, bootstrap sampling, feature subsampling, variance reduction, feature importance limitations. **Build:** Record a fair model comparison and discuss interpretability/runtime trade-offs
- [Week 19: Cross-validation and tuning](week-19-cross-validation-and-tuning/README.md) - Train/validation/test roles, folds, hyperparameter search, pipelines, leakage prevention, reproducible comparisons. **Build:** Compare a default model with a tuned model without repeatedly inspecting the test set
- [Week 20: Unsupervised learning](week-20-unsupervised-learning/README.md) - Unlabeled data, scaling, k-means intuition, cluster evaluation limits, dimensionality reduction overview. **Build:** Write a cautious cluster exploration; do not label clusters as ground truth

## Phase 5: SQL, DSA, and the first major ML project (Weeks 21-24)

- [Week 21: SQL intermediate](week-21-sql-intermediate/README.md) - Multi-table joins, subqueries, aggregate filters, CASE, window-function concepts, query readability and NULL behavior. **Build:** Build a set of documented queries on a synthetic SQLite database and check each result manually
- [Week 22: DSA practice patterns](week-22-dsa-practice/README.md) - Two pointers, hash maps, stacks and queues, recursion basics, sorting/search patterns, complexity and edge cases. **Build:** Complete six easy/early-medium problems with independent explanations and tests
- [Week 23: ML project development](week-23-ml-project-development/README.md) - Problem framing, data dictionary, baseline selection, reproducible split, pipeline, metrics, limitations and README. **Build:** Create a project skeleton and experiment log using synthetic or licensed data
- [Week 24: Student performance prediction](week-24-student-performance-prediction/README.md) - Project scope, synthetic data, leakage and proxy risks, EDA, baseline, model comparison, limitations. **Build:** Build a reproducible prediction demonstration using synthetic records only; state that it must not be used for real student decisions

## Phase 6: Deep learning and PyTorch (Weeks 25-28)

- [Week 25: Deep learning fundamentals](week-25-deep-learning-fundamentals/README.md) - Neuron and layers, weights and biases, activations, loss, gradient descent, backpropagation concept, overfitting. **Build:** Draw and annotate a tiny network; compare its limitations with a simpler baseline
- [Week 26: PyTorch basics](week-26-pytorch-basics/README.md) - Tensors and shapes, datasets and loaders, model objects, autograd, CPU/GPU awareness, reproducibility. **Build:** Run a minimal tensor/autograd exercise; no large model or GPU required
- [Week 27: Neural networks](week-27-neural-networks/README.md) - Layer composition, activations, loss functions, optimizer, training loop, validation, learning curves. **Build:** Record a learning curve and identify one sign of underfitting or overfitting
- [Week 28: Introductory deep-learning project](week-28-deep-learning-project/README.md) - Project framing, small dataset, baseline, training/validation, checkpoints, limits and compute budget. **Build:** Create a reproducible demo with evaluation, a model card-style note, and compute limits

## Phase 7: NLP, transformers, and LLM foundations (Weeks 29-32)

- [Week 29: NLP fundamentals](week-29-nlp-fundamentals/README.md) - Text tasks, tokenization, normalization, vocabulary, ambiguity, train/test separation for text. **Build:** Prepare a small, non-sensitive text sample and a task/data statement
- [Week 30: Text processing](week-30-text-processing/README.md) - Token counts, n-grams, bag of words, TF-IDF, sparse features, simple text classifier, leakage in preprocessing. **Build:** Compare a simple text baseline with a transparent error review
- [Week 31: Transformers and LLM foundations](week-31-transformers-and-llms/README.md) - Token IDs, attention intuition, context window, pretrained model, inference, model cards, limits and evaluation. **Build:** Write a model-selection note; core reading does not require a paid API or large download
- [Week 32: Embeddings and semantic search](week-32-embeddings-and-semantic-search/README.md) - Vector representations, cosine similarity, top-k retrieval, chunking trade-offs, relevance evaluation. **Build:** Compare keyword and vector search on a small public-text corpus with a relevance checklist

## Phase 8: AI applications and recommendation systems (Weeks 33-36)

- [Week 33: AI application development](week-33-ai-application-development/README.md) - Application requirements, input/output contracts, deterministic components, validation, error paths, privacy and user communication. **Build:** Build a command-line prototype with clear validation and a fallback when no result is relevant
- [Week 34: Recommendation systems](week-34-recommendation-systems/README.md) - Popularity baseline, content-based features, user/item signals, ranking, cold-start, offline evaluation limits. **Build:** Create a small recommender using synthetic preferences; clearly distinguish recommendations from facts
- [Week 35: AI Career Assistant project](week-35-ai-career-assistant/README.md) - Document ingestion, skill extraction, semantic retrieval, ranking, safe suggestions, user control and limitations. **Build:** Plan an explainable assistant that links suggestions to source text and avoids promises about hiring outcomes
- [Week 36: AI project improvement and responsibility](week-36-ai-project-improvements/README.md) - Error analysis, input validation, bias and privacy review, refusal/fallback behavior, evaluation, accessibility. **Build:** Improve the career-assistant prototype with feedback, source links, privacy notes, and safeguards

## Phase 9: Backend, frontend, and deployment (Weeks 37-40)

- [Week 37: FastAPI fundamentals](week-37-fastapi-fundamentals/README.md) - HTTP request/response, routes, JSON, type validation, status codes, interactive docs, local server lifecycle. **Build:** Create a tiny status/search API without exposing credentials or personal records
- [Week 38: Model API development](week-38-model-api-development/README.md) - Load a saved pipeline, validate features, predict, error handling, API tests, logging without sensitive payloads. **Build:** Create a reproducible local inference API; keep model artifacts small and untracked
- [Week 39: React frontend integration](week-39-react-frontend-integration/README.md) - Component state, forms, fetch, loading/error states, API contract, CORS, environment variables without secrets. **Build:** Connect a minimal React screen to the local model API; never put private keys in browser code
- [Week 40: Deployment and Docker](week-40-deployment-and-docker/README.md) - Images and containers, environment configuration, health checks, logs, resource limits, deployment choices. **Build:** Write a deployment checklist including secret storage, cost, privacy, and rollback; no cloud account required

## Phase 10: End-to-end projects and portfolio (Weeks 41-44)

- [Week 41: End-to-end ML project](week-41-end-to-end-ml-project/README.md) - Problem definition, data checks, pipeline, baseline, evaluation, inference, reproducibility, responsible limitations. **Build:** Build one end-to-end project; commit no private data, credentials, or large generated model files
- [Week 42: Testing and code quality](week-42-testing-and-code-quality/README.md) - Unit and integration tests, temporary data, deterministic tests, formatting/linting, type clarity, error messages. **Build:** Add a small test suite and a repeatable local quality-check command
- [Week 43: Portfolio and GitHub](week-43-portfolio-and-github/README.md) - Repository hygiene, focused commits, safe ignore rules, project selection, evidence-based descriptions, public/private data review. **Build:** Create a portfolio index that links only to working, appropriately described projects
- [Week 44: Project documentation](week-44-project-documentation/README.md) - Problem and audience, setup, data/source and license, methods, evaluation, limitations, screenshots/demo. **Build:** Finish a README with setup, run commands, results, limitations, and citations

## Phase 11: Interview preparation (Weeks 45-48)

- [Week 45: DSA interview practice](week-45-dsa-interview-practice/README.md) - Problem clarification, examples, brute force, optimization, complexity, test cases, verbal explanation. **Build:** Log five independently solved problems with approach, complexity, and one lesson each
- [Week 46: SQL interview practice](week-46-sql-interview-practice/README.md) - Filtering, joins, aggregation, NULL, subqueries, window-function concepts, explain query results. **Build:** Create a query-answer log with expected result shape and edge cases
- [Week 47: ML interview preparation](week-47-ml-interview-preparation/README.md) - Statistics, leakage, bias/variance, model choice, metrics, validation, limitations, concise explanations. **Build:** Build a personal question bank with answers you can explain and verify
- [Week 48: Project and behavioral interviews](week-48-project-and-hr-interviews/README.md) - Project walkthrough, trade-offs, debugging story, collaboration, STAR answers, honest scope and learning reflection. **Build:** Record a mock interview reflection with strengths, gaps, and next practice task

## Phase 12: Placement readiness (Weeks 49-52)

- [Week 49: Resume and LinkedIn](week-49-resume-and-linkedin/README.md) - Role targeting, evidence-based bullets, project links, skills accuracy, profile completeness, no fabricated metrics. **Build:** Prepare a role-specific resume and LinkedIn checklist; never invent experience or results
- [Week 50: Mock interviews](week-50-mock-interviews/README.md) - Timed coding, SQL explanation, ML questions, project walkthrough, feedback, recovery after mistakes. **Build:** Create a mock-interview scorecard and a short practice plan for the top two gaps
- [Week 51: Placement applications](week-51-placement-applications/README.md) - Find relevant internships/entry roles, tailor applications, track dates, professional follow-up, scam awareness. **Build:** Create a private local application-tracking template; do not publish personal application data
- [Week 52: Final review and continued plan](week-52-final-review-and-placement-plan/README.md) - Review evidence, identify gaps, reflect on results, set next 90-day goals, sustainable placement search. **Build:** Write a realistic 90-day continuation plan; placement and salary outcomes are not guaranteed
