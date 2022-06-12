FROM python:slim-buster

RUN pip3 install tqdm

WORKDIR /workspace

COPY ./ok.py /workspace/
CMD ["python3", "/workspace/ok.py"]
