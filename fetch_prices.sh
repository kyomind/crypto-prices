#!/bin/bash
source /home/${USER}/code/crypto-prices/.venv/bin/activate
python /home/${USER}/code/crypto-prices/main.py >> /home/${USER}/code/crypto-prices/python.log 2>&1
deactivate
