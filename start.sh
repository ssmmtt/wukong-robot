> nohup.out
ps -ef|grep wukong|grep -v grep|awk '{print $2}'|xargs kill -9
nohup python3 wukong.py &
tail -f nohup.out
