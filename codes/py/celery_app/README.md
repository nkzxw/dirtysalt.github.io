# 参考资料
- http://docs.celeryproject.org/en/master/getting-started/next-steps.html


# 启动celery worker

切换到上层目录下面. 使用下面命令来启动celery worker

`celery -A celery_app.app worker -l info`

默认地会去celery_app目录下面查找celery.py这个文件。如果想使用其他文件比如app.py的话，就需要指定 `-A celery_app.app`

# 调用celery worker

编写了一个test.py文件来发起task，调用celery worker. 运行起来比较奇怪，不能直接执行test.py这个文件，需要切换到上层目录使用下面命令

`python -m celery_app.test`

# 使用不同的Queue

这个可以通过celery的Routing机制来解决，将不同的task映射到不同的Queue上面去。

```
app.conf.update(
    task_routes = {
        'celery_app.tasks.add': {'queue': 'hipri'}
    }
)
```

这样所有`tasks.add`工作都会放到`hipri`这个队列里面. 然后在启动的时候需要添加`-Q hipri`参数来说，我监听`hipri`这个queue并且从里面获取task来执行。


