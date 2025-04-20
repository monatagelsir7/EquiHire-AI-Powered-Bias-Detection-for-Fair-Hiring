# EquiHire-AI-Powered-Bias-Detection-for-Fair-Hiring



----
# Plan of action 

## We have two elements - bias in descriptions and bias in hiring (on platforms, based on resume) 
# Proof of Concept
* Bias in job descriptions - embedding models to **measure bias** --> here can be obvious metrics and such 
* Fairness in Hiring Trends --> disparate impact ration --> **can do simulations on who would get hired/picked up by ATS normally and with our model --> more fair**



## Final Report - focus on building and validating core research components

## Part 1. Bias in Job Description
### 🎯 **Objective**

Detect and mitigate biased language in job descriptions using NLP techniques. Demonstrate that your model identifies bias and effectively rewrites it, leading to measurable improvements in fairness metrics.

### Main deliverables in the report
| Deliverable                             | Description                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ** 📅 Analytical Summary (2025-04-20)** | Overview of how bias is measured (bias score methodology, examples, thresholds) and what the current bias levels look like in your sample corpus. |
| **🧠 Model Output Showcase**            | Examples of flagged phrases and suggested debiased rewrites. Could include top N biased terms, before/after snippets.                             |
| **📊 Evaluation of Improvement**        | Apply fairness/bias metrics to the dataset before and after debiasing. Show improvement quantitatively (e.g., lower average bias score).          |

### To get there
- [ ] **Step1:** Gather original data - job descriptions with or without metadata
#### Available Data Found:
### Problem right now - no data on the bias vectors so we will probably need to create "bias dataset" with vectors for it and type of bias mapped  
### Job descriptions data: 
* [Kaggle: LinkedIn Jobs and skills 1.3m posts](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024)
* [ Kaggle: Job title and Job Description Dataset](https://www.kaggle.com/datasets/kshitizregmi/jobs-and-job-description)  --> lacks bias markers (real descriptions)
* [Kaggle: Job  Dataset](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset) - no bias markers  + it's synthetic 
* [Kaggle: Job Classification Dataset] (https://www.kaggle.com/datasets/HRAnalyticRepository/job-classification-dataset) -> fictional/synthetic but has some labels we can use like **pay grade**
* [Kaggle: Real vs Fake Job Postings ] (https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) -> has metadata and descriptions (can filter fake ones out)
* [Hugging Face: Job Description Public](https://huggingface.co/datasets/nakamoto-yama/job-descriptions-public/viewer?views%5B%5D=train) -> 
* [Hugging Face: Data Science Job Descriptions](https://huggingface.co/datasets/nathansutton/data-science-job-descriptions) ->  has companies and titles 
* **!!*[Research + Github Repo : Large Language Models for Detecting bias in Job Descriptions](https://github.com/2024-mcm-everitt-ryan) 
	* has research we can reference 
	* have labels for different biases in job descriptions --> masculine, feminine, general, disability, age, race, sexuality
	* around 3k units so not a lot but probably enough for the Proof-of-Concepts + we can probably get **bias** vectors from the model or dataset
* [Paper: Investigating Gender Bias In STEM Job Advertisements](https://aclanthology.org/2024.gebnlp-1.11/)
	* they go beyond simple feminine/masculine bias and propose some sub-biases categories: agentic, balanced, and communal --> via clustering information in the job descriptions 
* [Tools: Ongig Text Analysis to detect gender bias in job description](https://www.ongig.com/bias-job-descriptions)
	* maybe they have some proven results we can borrow ffrom
* [Data Science Jobs and Salaries Indeed](https://www.kaggle.com/datasets/ritiksharma07/data-science-jobs-and-salaries-indeed)
### Bias Research (no data but probably should be enough to construct a bias dataset)
* [Uncovering Bias Based on Gender in Job Descriptions](https://www.omdena.com/blog/uncovering-gender-bias-in-texts-exploring-inclusivity-in-ai)
* 

- [ ] **Step 2: **Define and implement Bias Metrics on the original dataset 
	-  Get bias score by comparing cosine similarty between job descriptions and known biased language terms 
	- or if we have biased markers in the job descriptions somewhere
- [ ] **Step 3: ** Thresholding + Flagging  
	- decide on what makes a biased description 
	- use XAI to calibrate show off
- [ ] **[Optional] Step 4:**  Bias Rewriting 🔺 
	- we mentioned it in the proposal but let's keep it sorta optional 
	- create a module to rewrite the job description to be de-biased (LLMs prob easiest)
		- or rule based substitution 
	- ➡️ Output: Table or JSON with original + rewritten versions.
- [ ] **Step 5** : Compare original vs Debiased Set 
	- recompute bias scores on the original (already computed ) and on the **de-biased** counterpart 
	- Show  : bias scores histogram shift, reduction in cosine similarity and what not
	- ➡️ Output: Before/after plots, summary stats table, word shift visual.
## 📂 Folder Structure Suggestion

```bash 
/bias_detection_job_descriptions/
│
├── data/
│   ├── job_descriptions_raw.csv
│   ├── job_descriptions_debiased.csv
│
├── notebooks/
│   ├── 01_bias_score_analysis.ipynb
│   ├── 02_rewriting_module.ipynb
│   ├── 03_comparison_metrics.ipynb
│
├── outputs/
│   ├── bias_score_histogram.png
│   ├── top_biased_terms.csv
│   ├── original_vs_debiased_examples.md
│
└── report/
    └── part1_bias_in_job_descriptions.md

```

### Papers/Research/codes kinda relevant for this part

**(LIKELY WILL FOCUS ON THIS ONE) Pre-processing:** Modifying the training data before model training. This is often considered a proactive approach. Techniques include: 
* Data Augmentation , data filtering/selection, dataset balancing
* [# Evaluating and Mitigating Gender Bias in Generative Large Language Models](https://univagora.ro/jour/index.php/ijccc/article/view/6853)*
* [Bias Mitigation For LLMs using Adversarial Learning](https://d-nb.info/1328386538/34)
* [BiasWipe: Mitigating Unintended Bias in Text Classifiers through Model Interpretability](https://aclanthology.org/2024.emnlp-main.1172.pdf)
* [A comprehensive Review of AI Techniques for addressing Algorithmic Bias in Job Hiring](https://www.mdpi.com/2673-2688/5/1/19)

**In-processing** Modifying the model's training process or architecture to reduce bias learning. Examples include:
* adversarial debiasing 
* regularizations 
* ....

**Post-processing**: Modifying the model's output after generation. This is the category the user's rewriting module falls into. Techniques include:
* - _Output Filtering/Ranking:_ Blocking or re-ranking outputs identified as biased.  
- _Calibration:_ Adjusting output probabilities or scores to ensure fairness across groups.
- _Controlled Text Generation:_ Guiding the generation process to avoid biased language.
- _Text Rewriting:_ Automatically editing the generated text to replace biased language with neutral alternatives.

**Table 3: Comparison of Debiasing/Rewriting Techniques for Job Descriptions**

| Technique                                | Core Mechanism                                                            | Pros                                                                  | Cons                                                                                          | Relevance to User Plan (Step 4) | Key Snippets |
| :--------------------------------------- | :------------------------------------------------------------------------ | :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- | :------------------------------ | :----------- |
| **Rule-Based Substitution**              | Predefined dictionary mapping biased terms to inclusive alternatives.     | Simple, interpretable, high precision for known terms.                | Limited scope, misses context, requires manual maintenance, inflexible.                       | Direct implementation option.   | [User Plan]  |
| **T5 Fine-tuning**                       | Fine-tuning an encoder-decoder Transformer on biased/unbiased text pairs. | Learns complex patterns, context-aware, leverages pre-training.       | Requires paired training data, computationally moderate, potential for errors.                | Potential model choice.         | [User Plan]  |
| **LLM Prompting**                        | Providing instructions within the prompt to guide rewriting.              | Flexible, leverages powerful LLMs, requires no fine-tuning.           | Requires careful prompt engineering, output consistency can vary, potential cost/latency.     | Potential model choice.         | [User Plan]  |
| **LLM Fine-tuning / Instruction Tuning** | Adapting an LLM using custom datasets of instructions and rewrites.       | High performance, adapts LLM to specific task (debiasing), effective. | Requires significant data/compute for tuning, complex, potential for catastrophic forgetting. | Potential model choice.         | [User Plan]  |

# Part 2. Hiring Bias 

### 🎯 **Objective**

Evaluate **bias in hiring outcomes** (e.g., resume callbacks, salary offers, promotions) across demographic groups using fairness metrics, and optionally build a prototype to test whether **de-identified resumes** perform better in a biased pipeline (e.g., gender-neutral resumes vs. original ones).

## 📦 Final Deliverables (for the report)

|Deliverable|Description|
|---|---|
|**📊 Hiring Fairness Analysis**|Statistical tests and metrics (like disparate impact, selection rates, p-values) showing bias in a dataset (real or simulated).|
|**📄 Resume Bias Prototype (optional)**|A prototype tool that removes identity indicators (e.g., name, gendered pronouns, affiliations) from a resume and shows side-by-side versions.|
|**🔍 Evaluation**|Compare the likelihood of "callback" or "hire" based on debiased vs. original resumes using either dataset scoring or simulated ATS filters.|
### To get there
- [ ] **Step 1** Choose or create a hiring dataset 

#### Step 1. Hiring Datasets 
### Table 1: Comparison of Publicly Available Hiring/Resume Datasets

| Dataset Type/Example                                                                                              | Focus                                       | Key Features                                                              | Data Type                    | Size (Approx.) | Availability/Access             | Key Limitations                                                                                                 |
| :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------ | :------------------------------------------------------------------------ | :--------------------------- | :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------- |
| [Bertrand & Mullainathan (2004)](https://www.aeaweb.org/journals/data)                                            | Racial Name Bias in Callbacks               | Name Type (Race Signal), Resume Quality, Callback Outcome                 | Field Experiment             | ~5,000 Resumes | Via Replication Archives (e.g.) | Focuses only on name/race bias; only callback outcome; older data.                                              |
| [Bias in Bios (De-Arteaga '19)](https://paperswithcode.com/dataset/biasbios)                                      | Gender/Occupation Bias in Textual Data      | Biography Text, Occupation, Inferred Binary Gender                        | Web Scraped (Common Crawl)   | ~400,000 Bios  | Via Authors/Project Page (e.g.) | No hiring outcome; binary gender; demographics may not match workforce; text is biographies, not resumes.       |
| Kaggle HR Analytics (General)                                                                                     | Employee Outcomes, Attrition, Performance   | Demographics (often Gender, Age), Tenure, Salary, Dept, Performance, etc. | Survey / Organizational Data | Varies widely  | Kaggle                          | Typically post-hire data (selection bias); often lacks resume text; variable quality and completeness.          |
| Kaggle Resume Classification                                                                                      | Resume Categorization by Job Type/Skills    | Resume Text, Job Category Label                                           | Often Synthetic or Scraped   | Varies widely  | Kaggle                          | Often lacks demographics and real hiring outcomes; may be synthetic; focus is classification, not bias outcome. |
| [Utrecht Fairness Recruitment](https://www.kaggle.com/datasets/ictinstitute/utrecht-fairness-recruitment-dataset) | Illustrating Fairness Metrics & Definitions | Sensitive Features (Age, Gender, Loc.), Synthetic Model Decisions         | Purely Synthetic             | ~100s-1000s    | Kaggle                          | Artificial; designed for pedagogy, not realistic simulation; small scale.                                       |

## Kaggle Datasets: 
* [Predicting Hiring Decisions in Recruitment](https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data)
* [Salary by Job Title and Country](https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country) -> has salary information (can be used for bias whatev)
* [70k+ Job Applicants Data (Human Resource)](https://www.kaggle.com/datasets/ayushtankha/70k-job-applicants-data-human-resource)
	* has info on job applicants and **their respective employability scores** (PROBABLY PERFECT FOR US)
	* **target variable** - employed or not 
* [Human Resources Data set](https://www.kaggle.com/datasets/davidepolizzi/hr-data-set-based-on-human-resources-data-set)
	* synthetic but simulates basically employee data (e.g. age, gender) + action data (actions, promotions) + performance data 
* [AI Recruitment Pipeline Dataset](https://www.kaggle.com/datasets/yaswanthkumary/ai-recruitment-pipeline-dataset)
	* Not sure if it's synthetic or not but meant to directly trace ATS
	* has 10k records
	* Structure: 
		* 1. **ID** – A unique identifier for each applicant.
		* **Name** – The candidate’s name.
		* **Role** – The job position the candidate applied for.
		* **Transcript** – The full text of the interview conversation.
		* **Resume** – The resume text submitted by the candidate.
		* **Decision** – The final hiring outcome (`select` or `reject`).
		* **Reason_for_decision** – Explanation for the hiring decision.
		* **Job_Description** – The job description for the applied position.
 * [Pwc Diversity & Inclusion Dashboards](https://www.kaggle.com/datasets/rithikmurali/pwc-diversity-and-inclusion-dashboard)
 * [Automating Talent](https://www.kaggle.com/datasets/willianoliveiragibin/automating-talent)
	 * also something with ATS but I didnt understand what the data shows exactly (probably ATS score)
* [Real-World Tech Job Applications](https://www.kaggle.com/datasets/niklasfischer/real-world-tech-job-applications)
	* ~2k real job applications sent to various tech companies 
	* has more gradual labels like --> invited to inteview --> rejected bla bla
		* we should probably focus on **invited to interview** here since interviews didnt actually happen lmao 
	* gender bias by name
* [Top Tech Startups Hiring in 2023](https://www.kaggle.com/datasets/chickooo/top-tech-startups-hiring-2023)
* [AI-Powered Resume Screening dataset](https://www.kaggle.com/datasets/mdtalhask/ai-powered-resume-screening-dataset-2025)
	* synthetic resumes
	* not sure about hiring decisions - are they also synthetic or was there an experiment?
* [HR Analytics Data Set](https://www.kaggle.com/datasets/raminhuseyn/hr-analytics-data-set)
* [HR Analytics Dataset 2 - expanded?](https://www.kaggle.com/datasets/anshika2301/hr-analytics-dataset)
* [Human Resources Dataset](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set)
* [# Employee Upskilling and Hiring Success Dataset](https://www.kaggle.com/datasets/sumittr26/employee-upskilling-and-hiring-success-dataset)
	* likely synthetic 
* [Employee Data][https://www.kaggle.com/datasets/zahidmughal2343/employee-data]
* [Job Placement Dataset](https://www.kaggle.com/datasets/mahad049/job-placement-dataset)
	* placements of different bachelor degree holders after graduation
* [Employee Dataset](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset)
	* might be real data actually 
* [Employee Details Dataset](https://www.kaggle.com/datasets/mayanolan/employee-details-dataset)
* 



- [ ] **Step 2** Run Fairness Analysiss
	- if we have hiring outcome label just analyse from this points -- fairness, counterfactual fairness and so on 

- [ ] **Step 3** (Optional) RESUME DE-BIASING PROTOTYPE
	-  we can do a pipeline of 
		- Input: resume gotten in (as a pdf of just data point with simulated data) --> 
		- --> identify attributes (and proxy attributes) that will likely produce bias --> 
		- ---> remake  those into something else --> 
		- Output: de-biased data entry (either as a prototype with a pdf or just synthetic data)
		- **Analysis** --> put de-biased resumes through the original hiring model (we can simulate off the original dataset) and see if hiring outcomes changed/ fairness metrics -->
- [ ] **Step 4**: Simulate ATS or Hiring Model 
	- if we have a dataset with hiring outcome we can just scrape the "filler model"
- [ ] **Step 5** Evaluation and Analysis for the report 
	- Questions we kinda want to answer and demonstrate with this whole thing: 
		- Do de-biased resumes perform better in a fairness-aware system?
		- Could de-identification improve selection rate parity?
		- ➡️ Output: Report section with bias metric comparison + visualizations (before/after fairness curves, example resumes).

### Articles and anything relevant 
* [Sample Selection Bias](https://library.fiveable.me/introduction-econometrics/unit-6/sample-selection-bias/study-guide/z5oqKYDkQZVcQGnB)
> In a new study, UW researchers found that ChatGPT consistently ranked resumes with disability-related honors and credentials — such as the “Tom Wilson Disability Leadership Award” — lower than the same resumes without those honors and credentials. From [this article](https://www.washington.edu/news/2024/06/21/chatgpt-ai-bias-ableism-disability-resume-cv/)
* [# Identifying and Improving Disability Bias in GPT-Based Resume Screening](https://dl.acm.org/doi/10.1145/3630106.3658933)
	* may have data? 
	* For proof of concept --> can use same pertubations /sampling techniques 
	> To address this important concern, we present a resume audit study, in which we ask ChatGPT (specifically, GPT-4) to rank a resume against the same resume enhanced with an additional leadership award, scholarship, panel presentation, and membership that are disability-related. We find that GPT-4 exhibits prejudice towards these enhanced CVs.
	* Code for this paper [here](https://paperswithcode.com/paper/identifying-and-improving-disability-bias-in)


### Papers with potential data and code
* [# Incentivized Resume Rating: Eliciting Employer Preferences without Deception](https://www.aeaweb.org/articles?id=10.1257/aer.20181714)
* [Field Experiment Paper: # Is there a glass ceiling for ethnic minorities to enter leadership positions? Evidence from a field experiment with over 12,000 job applications](https://www.sciencedirect.com/science/article/pii/S1048984322000583)
* [# When your resume is (not) turning you down: Modelling ethnic bias in resume screening](https://www.researchgate.net/publication/328833697_When_your_resume_is_not_turning_you_down_Modelling_ethnic_bias_in_resume_screening)
* 

