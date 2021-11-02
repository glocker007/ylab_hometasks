FROM python:3.9.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /recipe_book
WORKDIR /recipe_book
ADD . /recipe_book/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' python
RUN adduser python sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER python
