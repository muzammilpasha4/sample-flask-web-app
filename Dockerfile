FROM python:slim

WORKDIR /app

COPY . .

RUN apt update && apt install -y python3 python3-pip &&\
    pip install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]    #can define this host & port inside app.py under app.run*
