#!/bin/bash
source /home/kyo/code/crypto-prices/.venv/bin/activate >> /home/kyo/code/crypto-prices/crontab.log 2>&1
python /home/kyo/code/crypto-prices/main.py >> /home/kyo/code/crypto-prices/crontab.log 2>&1
deactivate
