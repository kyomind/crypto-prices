source /home/${USER}/code/crypto-prices/.venv/bin/activate
python /home/${USER}/code/crypto-prices/main.py >> /home/${USER}/code/crypto-prices/crontab.log 2>&1
deactivate
