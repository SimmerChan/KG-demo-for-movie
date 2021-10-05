#!/bin/bash

streamlit run /kbqa/streamlit_app.py --server.enableCORS=true &
cd /kbqa/jena/apache-jena-fuseki-4.2.0 || return
./fuseki-server
