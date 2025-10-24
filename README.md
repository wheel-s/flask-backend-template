# Flask Backend Template

A production-ready**Flask backend boilerplate** with:
 - JWT Authentication
 - Docker & Github Actions (CI/CD)
 - pytest + coverage
 - SQLite (default) or PostgreSQL
 - Marshmallow validation

## 🪛Installation (Local)

```bash
git clone https://github.com/<your-username>/flask-backend-template.git
cd flask-backend-template
python -m venv venv
source venv/bin/activate  #or venv\Scripts\activate on Windows
pip install -r reqirements.txt
```


## Initialize database:
```bash
flask db migrate
flask db upgrade
```

## Run and Test
```bash
flask run or python run.py

pytest -v     #run all tests


