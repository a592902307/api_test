执行如下命令，可以解析log日志，执行完毕后会在 log 文件的同级目录下生成 当前时间戳.html 文件：
python3 formatLog.py文件的路径 log文件的路径或者log文件夹的路径
——————————————————————————————————————————————————————————————————————

示例如下：

解析 .log 日志文件：
python3 /Users/wlf/Documents/python/formatLog.py /Users/wlf/Desktop/log/mtc20200927_155442_554.log

解析 log 文件夹下的日志文件:
python3 /Users/wlf/Documents/python/formatLog.py /Users/wlf/Desktop/log

从某个时间开始解析 log 日志（可以精确到秒）：
从2020年9月27日13:54:42开始解析
python3 /Users/wlf/Documents/python/formatLog.py /Users/wlf/Desktop/log/mtc20200927_155442_554.log 20200927135442
从2020年9月27日00:00:00开始解析
python3 /Users/wlf/Documents/python/formatLog.py /Users/wlf/Desktop/log/mtc20200927_155442_554.log 20200927

在某个时间段解析 log 日志（可以精确到秒）：
python3 /Users/wlf/Documents/python/formatLog.py /Users/wlf/Desktop/log/mtc20200927_155442_554.log 20200927 20201009

——————————————————————————————————————————————————————————————————————

注意：由于不同的项目日志打印的时间格式不同，所以目前时间筛选功能可能只对 JC 日志有效
查看详情：https://juphoon.yuque.com/srei71/dxtlmt/rpgi3h