FROM python:3.9-slim

COPY requirements.txt ./

RUN echo "Python version:" && python --version
RUN echo "Pip version:" && pip --version
RUN echo "Installing production dependencies!" && pip install -r requirements.txt

COPY . ./

CMD python main.py
