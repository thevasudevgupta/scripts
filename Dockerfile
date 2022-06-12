FROM python:slim-buster

WORKDIR /workspace
COPY ./ok.py /workspace/
CMD ["python3", "/workspace/ok.py"]
