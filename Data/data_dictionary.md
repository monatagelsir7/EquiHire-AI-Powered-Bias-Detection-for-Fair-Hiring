# Resume Callback Study Data Dictionary

This document describes the variables in the resume dataset (4870 observations × 30 variables).

## Job Characteristics

| Variable Name | Type | Description |
|--------------|------|-------------|
| `job_ad_id` | Numeric | Unique identifier for the job advertisement |
| `job_city` | Categorical | City where the job was located (e.g., "Chicago") |
| `job_industry` | Categorical | Industry sector (e.g., "manufacturing", "finance_insurance_real_estate") |
| `job_type` | Categorical | Type of role (e.g., "clerical", "manager") |
| `job_fed_contractor` | Binary | 1 = Federal contractor, 0 = Not a federal contractor |
| `job_equal_opp_employer` | Binary | 1 = Employer claims Equal Opportunity status |
| `job_ownership` | Categorical | Company type (e.g., "nonprofit", "unknown") |

## Job Requirements

| Variable Name | Type | Description |
|--------------|------|-------------|
| `job_req_any` | Binary | 1 = Job lists any requirements |
| `job_req_communication` | Binary | 1 = Communication skills required |
| `job_req_education` | Binary | 1 = Education requirements specified |
| `job_req_min_experience` | Numeric | Minimum years of experience required |
| `job_req_computer` | Binary | 1 = Computer skills required |
| `job_req_organization` | Binary | 1 = Organizational skills required |
| `job_req_school` | Categorical | Education level required (if any) |

## Resume/Candidate Characteristics

| Variable Name | Type | Description |
|--------------|------|-------------|
| `received_callback` | Binary | **Target variable**: 1 = Received callback, 0 = No callback |
| `firstname` | String | First name used on the resume |
| `race` | Categorical | Inferred race from name (e.g., "white", "black") |
| `gender` | Categorical | Inferred gender from name ("f" or "m") |
| `years_college` | Numeric | Years of college education listed |
| `college_degree` | Binary | 1 = Resume lists a college degree |
| `honors` | Binary | 1 = Resume lists academic honors |
| `worked_during_school` | Binary | 1 = Work experience during school listed |

## Experience & Skills

| Variable Name | Type | Description |
|--------------|------|-------------|
| `years_experience` | Numeric | Total years of work experience listed |
| `computer_skills` | Binary | 1 = Computer skills mentioned |
| `special_skills` | Binary | 1 = Special skills section present |
| `volunteer` | Binary | 1 = Volunteer experience listed |
| `military` | Binary | 1 = Military service listed |

## Resume Quality Indicators

| Variable Name | Type | Description |
|--------------|------|-------------|
| `employment_holes` | Binary | 1 = Gaps present in employment history |
| `has_email_address` | Binary | 1 = Resume includes email contact |
| `resume_quality` | Categorical | Subjective quality rating ("low", "high") |