FROM python:3.8-slim

RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list

RUN apt-get -y install default-jdk

ADD . /kbqa
WORKDIR /kbqa

RUN /usr/local/bin/pip install -r requirements.txt -i https://pypi.douban.com/simple/ && rm -rf ~/.cache/pip

RUN /kbqa/jena/apache-jena-3.5.0/bin/tdbloader --loc="/kbqa/jena/tdb" "/kbqa/kg_demo_movie.nt"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 STREAMLIT_SERVER_PORT=80 FUSEKI_HOME=/kbqa/jena/apache-jena-fuseki-3.5.0

EXPOSE 80

CMD ["./start.sh"]