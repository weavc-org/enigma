FROM python:3.8

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile* ./

RUN pipenv install --ignore-pipfile

COPY . .

CMD [ "pipenv", "run", "python", "enigma", "--web" ]