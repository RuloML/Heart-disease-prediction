# Heart Disease Prediction — Recall-Oriented Clinical Analysis (FULL vs Screening)

This project addresses a binary classification problem focused on predicting the presence of heart disease using clinical and demographic data.  
Rather than optimizing for overall accuracy, the analysis is explicitly designed to **prioritize clinical sensitivity (recall)**, reflecting medical screening scenarios where failing to detect a true case (false negative) carries significant risk.

Importantly, this prioritization is implemented **within a controlled decision framework**, where increases in false positives are accepted only up to a clinically and operationally reasonable level.

---

## Problem Context

Cardiovascular disease screening involves an inherent trade-off between maximizing case detection and controlling the cost and burden of unnecessary follow-up tests.

From a public health perspective, minimizing false negatives is critical, as missed diagnoses may lead to severe clinical consequences. However, indiscriminately maximizing recall without considering false positives can overload healthcare systems and reduce overall efficiency.

This project explicitly explores that trade-off, identifying **decision thresholds that achieve high recall while avoiding unnecessary inflation of false positives once clinically acceptable sensitivity levels are reached**.

---

## Dataset

- Source: Public Heart Disease dataset from Kaggle
- Samples: ~1,000 patients
- Target variable:
  - `target = 1`: presence of heart disease
  - `target = 0`: absence of heart disease
- Feature types:
  - Demographic variables (age, sex)
  - Clinical measurements (blood pressure, cholesterol, ECG results)
  - Exercise-related indicators
- Literature:
  To provide additional clinical validation, scientific literature regarding the most influential features identified in the EDA were consulted. This allows us to support our modeling    assumptions with robust evidence and ensures that the proposed model is based on robust clinical foundations.

The dataset is approximately balanced between positive and negative cases.  
Some variables reflect advanced diagnostic information and are therefore evaluated carefully to avoid overly optimistic performance estimates and potential information leakage.

---

## Methodology

The task is formulated as a **binary classification problem**.

Two feature scenarios are evaluated:

- **FULL model**  
  Uses the complete set of available clinical features.
- **SCR (Screening) model**  
  Excludes variables that may not be available during early screening or that could implicitly encode diagnostic outcomes.

Key methodological principles:
- Use of Logistic Regression as an interpretable baseline model
- Model selection optimized for recall rather than accuracy
- Evaluation using Precision-Recall curves to focus on positive case detection
- Explicit threshold analysis to quantify the trade-off between false negatives and false positives

The emphasis of the analysis is not on achieving maximum metric values, but on understanding **where clinically meaningful operating points lie**.

---

## Evaluation Strategy

Given the medical context, evaluation goes beyond standard accuracy metrics.

Primary evaluation dimensions include:
- Recall (sensitivity)
- Precision
- False Negatives (FN)
- False Positives (FP)

Precision-Recall curves are used to analyze model behavior in **high-recall operating regions**, which are most relevant for screening applications.  
Threshold selection is guided by the principle that **once recall reaches clinically acceptable levels, further gains are not pursued if they lead to disproportionate increases in false positives**.

---

## Key Results

- The FULL model consistently achieves high recall with substantially fewer false positives compared to the SCR model.
- At comparable recall levels (≈ 0.93–0.95), the SCR model generates more than twice the number of false positives.
- Precision-Recall analysis shows that the FULL model dominates the SCR model in clinically relevant operating regions.

**Core insight:**  
Observed performance differences are driven primarily by information availability rather than algorithmic complexity.

---

## Clinical Interpretation

- The FULL model is better suited for diagnostic or controlled clinical environments, where richer clinical information is available and follow-up capacity is limited.
- The SCR model may be acceptable as an initial pre-screening tool, but its higher false positive rate necessitates confirmatory testing and careful operational consideration.

This framing reflects real-world healthcare decision-making rather than purely technical optimization.

---

## Potential Extensions and Future Work

This project is intentionally scoped as an academic and methodological exploration of recall-oriented evaluation in heart disease prediction.

As a potential future extension, the model could be enriched by incorporating additional cardiovascular risk factors derived from related predictive systems. For example, outputs from a diabetes risk prediction model could be integrated as an additional feature or upstream signal, reflecting the well-established relationship between diabetes and cardiovascular disease.

Such an approach would allow for:
- A more holistic risk assessment framework
- Improved early-stage screening performance
- Exploration of model stacking or multi-stage decision pipelines

This extension is deliberately left outside the current project scope to maintain methodological clarity and focus.

---

## Limitations

Several limitations should be acknowledged:

- The dataset is relatively small and well-curated, which may lead to optimistic performance estimates compared to real-world clinical data.
- Some features encode advanced diagnostic information that may not be available at early screening stages.
- The analysis is limited to a single dataset and does not include external validation on independent cohorts.
- Clinical costs associated with false positives and false negatives are discussed qualitatively rather than being modeled explicitly.

These limitations reinforce the academic and exploratory nature of the project.

---

## Conclusions

This project demonstrates how aligning model evaluation with healthcare objectives significantly influences both model selection and interpretation.
Prioritizing recall while explicitly controlling false positive growth leads to more actionable and responsible decision thresholds than maximizing aggregate performance metrics alone.

---

## Disclaimer

This project is intended for educational purposes only and does not constitute medical advice.

## Repository Structure

```text
notebooks/
├── 01_eda_inicial.ipynb
├── 02_heart_disease_logistic_analysis.ipynb
README.md
LICENSE
