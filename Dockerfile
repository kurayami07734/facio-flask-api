FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

CMD ["python", "./main.py"]