#coding:utf-8
import os
import re
import regex
import sys
import webbrowser
import json
import time

html = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Document</title><link rel="stylesheet" type="text/css" href="https://www.layuicdn.com/layui/css/layui.css"><script src="https://www.layuicdn.com/layui/layui.js"></script><style>.header{top:0;width:100%;position:fixed}.header div{float:left}.header .logo{width:200px;height:60px;background-color:#393d49;color:#fff;text-align:center;font-size:20px;line-height:60px}.header .menu{width:calc(100% - 200px)}.layui-nav{border-radius:0}.article{width:100%}.left{position:fixed;width:200px;height:100vh;background-color:#393d49}.right{padding:15px;margin-left:200px;height:100%}#content{white-space:break-spaces;word-break:break-all}</style></head><body><div class="header"><div class="logo">日志分析工具</div><div class="menu"><ul class="layui-nav" lay-filter=""></ul></div></div><div class="article"><div class="left"><ul class="layui-nav layui-nav-tree"></ul></div><div class="right"><div id="content"></div></div></div><script>window.strimgTurnDom = function (txt) {
            try //Internet Explorer
            {
                xmlDoc = new ActiveXObject("Microsoft.HTMLDOM");
                xmlDoc.async = "false";
                xmlDoc.loadXML(txt);
                alert("ie");
                return (xmlDoc);
            }
            catch (e) {
                try //Firefox, Mozilla, Opera, etc.
                {
                    parser = new DOMParser();
                    xmlDoc = parser.parseFromString(txt, "text/html");
                    return (xmlDoc);
                }
                catch (e) { alert(e.message) }
            }
            return (null);
        }
        var alldata = []
        function renderhtml(res) {
            console.log(res)
            var data = alldata.filter(function (item) {
                return item.num == res;
            })
            data = data[0]
            res = data.html
            console.log(res)
            res = res ? res : '当前标签无内容'
            layui.use(['element', 'jquery'], function () {
                var element = layui.element;
                var $ = layui.jquery
                $("#content").html(res)
                element.init()
            })
        }
        //注意：导航 依赖 element 模块，否则无法进行功能性操作
        layui.use(['element', 'jquery', 'layer'], function () {
            var element = layui.element;
            var $ = layui.jquery
            var index = layer.load(1, {
                shade: [0.1, '#fff'] //0.1透明度的白色背景
            });
            //…
            function renderdata(datalist) {
                let html = ''
                let data = []
                let data_num = 0
                datalist.forEach((e, i) => {
                    let href = e.html ? e.html : 'javascript:;'
                    // let layui_this = i == 0 ? 'layui-this' : ''
                    let layui_this = ''
                    if (!e.children) {
                        data.push(Object.assign({ num: data_num }, e))
                        html += [
                            `<li class="layui-nav-item ${layui_this}">`,
                            `<a href="javascript:;" onclick="renderhtml('${data_num}')">${e.title}</a>`,
                            `</li>\n`
                        ].join("")
                        data_num++
                    } else {
                        data.push(Object.assign({ num: data_num }, e))
                        html += [
                            `<li class="layui-nav-item ${layui_this}">`,
                            `<a href="javascript:;">${e.title}</a>`,
                            `<dl class="layui-nav-child">\n`
                        ].join("")
                        data_num++
                        e.children.forEach(ele => {
                            data.push(Object.assign({ num: data_num }, ele))
                            let children_html = ele.html ? ele.html : 'javascript:;'
                            let mark = ele.mark
                            html += [`<dd><a href="javascript:;" onclick="renderhtml('${data_num}')">${ele.title}`,
                            mark ? `<span class="layui-badge-dot" style="position: relative;top: -2px;left: -3px;"></span>` : '',
                                `</a></dd>\n`].join("")
                            data_num++
                        })
                        html += [`</dl></li>\n`]
                    }
                })
                alldata = data
                return html
            }
            // $.get('data.json', function (res) {
            //     console.log(res)
            let datalist = """

html2 = """ 
        var needhtml = renderdata(datalist)
            layer.close(index)
            // $(".menu .layui-nav").html(needhtml)
            $(".layui-nav.layui-nav-tree").html(needhtml)
            renderhtml('0')
            element.init();
            // })
        });</script></body></html>"""

outputParentPath = os.path.split(os.path.realpath(sys.argv[1]))[0]

allLog = ""
mtcErrorLog = ""
sysLog = ""
clientProcessLog = ""
callProcessLog = ""
mediaChannelProcessLog = ""
processLog = ""
startTime = ""
endTime = ""

def outputHtml():
    logList = []  #LogList=[allLogItem,filterLogItem,processLogItem]
    # 原始日志
    allLogItem = {}
    allLogItem["title"] = "原始日志"
    allLogItem["html"] = allLog
    logList.append(allLogItem)

    # 日志筛选
    filterLogItem = {}
    filterLogItem["title"] = "日志筛选"
    childList = []
    # 遍历regex.filterList中每一个实例对象
    for filterResult in regex.filterList:
        filterItem = {}          # filterItem={“title”:filterResult.name,"html":,"mark":}
        # 日志筛选的每个名称
        filterItem["title"] = filterResult.name
        # 日志筛选里面的内容以及是否需要打上小标点
        if len(filterResult.filterItems) == 0:
            filterItem["html"] = ""
            if (filterResult.markCondition == "notFound"):
                filterItem["mark"] = True
        else:
            filterItem["html"] = filterResult.filterItems[0:]
            if (filterResult.markCondition == "found"):
                filterItem["mark"] = True

        # 把每个实例产生的filterItem列表加到childList中去
        childList.append(filterItem)
    filterLogItem["children"] = childList
    logList.append(filterLogItem)

    # 流程
    processLogItem = {}
    processLogItem["title"] = "流程"
    childList = []
    for result in regex.processList:
        processItem = {}
        processItem["title"] = result.name
        processContent = "<h1><font color=#1e90ff>异常流程:</font></h1>"
        for errorItem in result.processErrorItems:
            if (errorItem.logs != ""):
                processItem["mark"] = True
                processContent += (errorItem.logs + "<br/>")
        processContent += "<h1><font color=#1e90ff>正常流程:</font></h1>"
        for finishedItem in result.processFinishedItems:
            processContent += (finishedItem.logs + "<br/>")
        processItem["html"] = processContent
        childList.append(processItem)
    processLogItem["children"] = childList
    logList.append(processLogItem)

    print('----------------------1130----------------------')

    outputPath = outputParentPath + "/" + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + ".html"
    dataFile = open(outputPath, "w")
    outJson = json.dumps(logList)
    dataFile.write(html+outJson+html2)
    dataFile.close()
    webbrowser.open("file://" + outputPath)

def parseFile(filePath):
    file = open(filePath, encoding = 'latin')
    lines = file.readlines()
    for singleLine in lines:
        # 调用isInTimeScope，检查日志是否在有效时间内
        if (regex.isInTimeScope(singleLine, startTime, endTime) == False):
            continue
        # 调用isNeedDrop，检查是否有需要丢弃的日志，如果有就跳出本次循环，开始下次循环
        if (regex.isNeedDrop(singleLine) == True):
            continue
        # 美化日志，替换错误码
        newLine = regex.beautify(singleLine).replace("&", "&amp").replace("<", "&lt").replace(">", "&gt").replace('"', "&quot").replace("\n",  "<br/>").replace("\r", "")
        global allLog
        # 把处理好的日志加入到原始日志、日志筛选、流程三个模块中
        allLog += newLine
        regex.analysisFilter(newLine)
        regex.analysisProcess(newLine)
    file.close()

def main():
    regex.initBeautifyResult()
    regex.initFilterResult()
    regex.initProcessRulesAndProcessResults()
    global startTime
    global endTime
    # 命令行输入格式 python formatLog.py .log文件 开始时间 结束时间
    # python 0 1 2 3
    if (len(sys.argv) == 3):
        startTime = sys.argv[2]
    if (len(sys.argv) == 4):
        startTime = sys.argv[2]
        endTime = sys.argv[3]
    if sys.argv[1].endswith('.log'):
        parseFile(sys.argv[1])
    else:
        # os.listdir 返回指定路径下的文件和文件夹列表，sort()排序，遍历取出文件夹中的.log结尾日志文件
        path_list = os.listdir(sys.argv[1])
        # path_list.remove('.DS_Store')
        path_list.sort()
        for filePath in path_list:
            if (filePath.endswith('.log')):
                parseFile(sys.argv[1] + "/" + filePath)
    regex.processingToError()
    outputHtml()

main()