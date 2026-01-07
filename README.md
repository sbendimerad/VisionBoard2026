
# 🎯 Vision 2026 — Goal & Behavior Tracking System (Neon + Streamlit)

Vision 2026 is a goal-tracking and reflection system designed to help users **set goals**, **track daily/weekly execution**, and **monitor long-term consistency** (monthly → yearly).

This project focuses on **behavioral feedback** over time — not just checking tasks.


## Why this exists

Most trackers answer: “Did you do the task?”

Vision 2026 answers:
- Are you consistent over time?
- Which life domains are neglected?
- Are you on track for long-term goals (monthly/quarter/semester/yearly)?
- Where do you need to adjust your behavior to reach your objectives?


## Features

- **Goal Setup**: create goals with a category + frequency  
  Daily, Weekly, Monthly, Quarterly, Semester, Yearly
- **Tracking Board**
- **Reports**
  - Daily consistency timeline 
  - Weekly consistency table 
  - Long-term strategic health 

## Tech Stack

- **Frontend**: Streamlit
- **Database**: Neon (PostgreSQL)
- **Data**: Pandas
- **Charts**: Plotly
- **Auth**: simple email/password (MVP)


## Project Structure

```

vision-2026/
├── app.py
├── core_logic.py
├── db_utils.py
├── requirements.txt
├── packages.txt
├── .gitignore
├── README.md
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml        # local only (never commit)
└── screenshots/

````


## Getting Started (Local with Conda)

### 1) Clone
```bash
git clone https://github.com/sbendimerad/vision-2026.git
cd vision-2026
````

### 2) Create and activate a Conda environment

```bash
conda create -n vision2026 python=3.11 -y
conda activate vision2026
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```


## Configure Neon (PostgreSQL)

This project reads the Neon connection string from **Streamlit secrets**.

### 1) Create `.streamlit/secrets.toml`

Create this file locally:

```bash
mkdir -p .streamlit
touch .streamlit/secrets.toml
```

Add your Neon connection string inside:

```toml
DATABASE_URL="postgresql://<user>:<password>@<host>/<dbname>?sslmode=require"
```

### 2) Ensure `secrets.toml` is ignored by git

Your `.gitignore` should include:

```gitignore
.streamlit/secrets.toml
```


## Run the app

```bash
streamlit run app.py
```


## Deployment Notes (Streamlit Cloud / others)

For deployment, you should not upload `secrets.toml`.

Instead, set the secret in your platform settings:

## Security (MVP)

This repository currently uses a simple MVP auth approach.
For production, you should implement:

* secure password hashing (bcrypt/argon2)
* proper session management
* rate limiting and brute-force protection
* password reset flow


## Roadmap

* Performance optimizations (reduce per-checkbox DB queries, caching, indexes)
* Cleaner UX for large goal catalogs
* CSV export/import for users
* Stronger auth and user onboarding
* Public demo deployment

---

## Author

Built by **Sabrine Bendimerad**
AI / Data Science / MLOps


