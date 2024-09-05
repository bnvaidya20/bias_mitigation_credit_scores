# Age Bias Detection and Mitigation Strategies for Credit Decision Making

## Introduction

This project focuses on detecting and mitigating age-related bias in credit decision-making using machine learning models. Bias in automated credit scoring can lead to unfair decisions, especially regarding sensitive attributes like age. The goal is to assess and mitigate age bias in predictive models built using the German Credit dataset and improve the fairness of credit decisions across different age groups.

## Problem Statement

In financial decision-making, such as loan approvals, biased models can negatively impact specific groups of individuals. This project aims to explore how age bias affects credit decision models and implement bias mitigation strategies to promote fairer outcomes. We analyze the disparity between the privileged group (age ≥ 25) and the unprivileged group (age < 25) in the model's decisions.

## Dataset Used

The **German Credit dataset** is used for this project, containing 1,000 records and 20 features, including age, credit amount, employment status, and more. The dataset classifies individuals as either having "good" or "bad" credit risk, making it suitable for assessing the fairness of financial decisions.

**Key Features:**
- **Credit History**
- **Purpose**
- **Credit Amount**
- **Employment Status**
- **Age** (Used as the protected attribute for bias detection)

## Methodology

### 1. **Bias Detection**
   - We begin by training machine learning models (Logistic Regression and Random Forest) on the dataset without applying any bias mitigation techniques.
   - Fairness metrics such as **Disparate Impact**, **Average Odds Difference**, **Equal Opportunity Difference**, and **Statistical Parity Difference** are computed to evaluate the presence of bias based on the protected attribute: **Age**.
   
### 2. **Bias Mitigation (Reweighing)**
   - After detecting bias, we apply the **Reweighing** technique (a pre-processing bias mitigation algorithm). This technique adjusts the weights of the training data to balance the outcomes for privileged and unprivileged groups.
   - We retrain the models using the transformed dataset and reassess bias using the same fairness metrics.

### 3. **Model Evaluation**
   - The models are evaluated both for accuracy and fairness. We compare the performance before and after bias mitigation to assess the effectiveness of the reweighing technique.
   - The fairness metrics are computed on both the original and transformed datasets to measure the change in bias.

## Results

- **Without Bias Mitigation**: Initial analysis shows that the privileged group (age ≥ 25) received more favorable credit outcomes compared to the unprivileged group (age < 25). 
- **With Bias Mitigation (Reweighing)**: After applying the reweighing technique, there was a notable improvement in fairness metrics, such as Disparate Impact and Equal Opportunity Difference, while maintaining a comparable level of model accuracy.

## Fairness Metrics Used

- **Disparate Impact**: Measures the ratio of favorable outcomes between unprivileged and privileged groups.
- **Equal Opportunity Difference**: Evaluates the difference in true positive rates between privileged and unprivileged groups.
- **Average Odds Difference**: Measures the average difference in false positive and false negative rates.
- **Statistical Parity Difference**: Measures the difference in the probability of favorable outcomes between groups.
- **Theil Index**: Measures inequality in the model’s predictions.

## Conclusion

The project demonstrates how machine learning models can exhibit bias based on age when making credit decisions. By applying the Reweighing technique, we successfully mitigated the bias, leading to more equitable outcomes for both age groups. This study highlights the importance of integrating bias detection and mitigation into machine learning workflows, particularly in high-stakes areas like credit scoring.

## How to Run the Project

1. **Clone the repository**: 
   ```bash
   git clone https://github.com/bnvaidya20/bias_mitigation_credit_scores.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Jupyter Notebooks**: Open and execute the provided Jupyter notebooks to replicate the experiments.


## References

- [AI Fairness 360 documentation](https://aif360.readthedocs.io/en/stable/)

- [German Credit Dataset - UCI Repository](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) 

This project showcases the importance of addressing bias in machine learning systems and provides practical strategies for detecting and mitigating bias in credit scoring models.