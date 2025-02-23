#!/bin/bash
source /home/admin/gas-prices/.venv/bin/activate
export SLACK_TOKEN="xxxxx"
python /home/admin/gas-prices/main.py
deactivate
