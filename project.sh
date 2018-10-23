#! /bin/bash
echo "12345" | sudo -S killall python
echo "12345" | sudo -S killall python3
echo "12345" | sudo -S killall node
cd Index
echo "12345" | sudo -S python3 -m http.server 80 &
python ../Blog/manage.py runserver 0.0.0.0:8000 &
node Visualizer/index.js &

firefox 0.0.0.0
