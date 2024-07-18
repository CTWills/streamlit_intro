FROM python:3.11.9-slim-bookworm

WORKDIR /app

RUN git clone https://github.com/CTWills/streamlit_intro.git .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]