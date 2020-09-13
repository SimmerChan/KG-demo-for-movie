#!/bin/bash

streamlit run /kbqa/streamlit_app.py --server.enableCORS=true &
cd /kbqa/jena/apache-jena-fuseki-3.5.0 || return
./fuseki-server