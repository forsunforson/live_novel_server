#！/bin/bash
rm -f /tmp/runlog
git pull
nohup ./claude-env/bin/python3 main.py 2>/tmp/runlog &
