FROM python: 3.11-slim

WORKDIR /app


COPY requirments.txt requirements.txt

COPY . .

ENV FLASK_APP = app
ENV_FLASK_ENV = production


CMD ["flask", "run", --host="0.0.0.0"]