#!/bin/bash

pip install setuptools==57.5.0
pip install pyhash==0.9.3
cd calvin_env_repo/tacto
pip install -e .
cd ..
pip install -e .
cd ..
pip install -e .
