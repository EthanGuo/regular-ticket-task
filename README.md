Regular Ticket task
===============

# Start server

    python server.py -c config/demo.py


# 安装python依赖库， 在Linux终端执行以下命令。

    sudo pip install -r errorAnalyzer/requirements.txt


# 启动工具， 终端执行

    需要启动beat和worker，其中worker可以启动多个，但是切记beat只能启动一个。
    
    - 下面的命令是同时启动beat和worker:

            celery worker --beat --app=worker:worker --logfile <log-file>  --pidfile <pid-file>

    - 下面的命令是只启动worker:

            celery worker --app=worker:worker --logfile <log-file>  --pidfile <pid-file>

    - 下面的命令只启动beat:

            celery beat --app=worker:worker --logfile <log-file>  --pidfile <pid-file>

    如果需要后台启动，可以使用`--detach`参数。