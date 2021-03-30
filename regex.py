#coding:utf-8

import re
import custom
import json

### ----------检查日志是否在有效时间范围内---------- ###
def isInTimeScope(text, startTime, endTime):
    if (startTime == ""):
        return True
    if (len(text) < 17):
        return False
    text = text[0:17].replace("T", "").replace(":", "")
    if (text.isdigit() == False):
        return False
    textTime = int(text)
    while len(startTime) < 14:
        startTime += "0"
    startTime = int(startTime)
    if (endTime == ""):
        if (textTime >= startTime):
            return True
        else:
            return False
    else:
        while len(endTime) < 14:
            endTime += "0"
        endTime = int(endTime)
        if (textTime >= startTime and textTime<= endTime):
            return True
        else:
            return False

### ----------美化日志（替换状态码数值为中文、替换状态值为中文）---------- ###
beautifulList = []

class BeautifulModel:
    def __init__(self, rule, content):
        self.rule = rule
        self.content = content

def initBeautifyResult():
    # 循环取出每一个需要替代的beautifulRule，创建实例，然后将一个个实例加入列表中
    for obj in custom.beautifulRules:
        model = BeautifulModel(obj["rule"], obj["content"])
        beautifulList.append(model)

def beautify(text):
    if len(custom.beautifulRules) == 0:
        return text
    # 从列表中取出每个实例对象
    for model in beautifulList:
        # 取出每个实例正则
        matchKey = model.rule
        for index in range(0, len(model.content), 2):
            # 正则匹配，如果不为空，后面的替换前面的
            if (re.match(matchKey, text) != None):
                text = text.replace(model.content[index], model.content[index + 1])
    return text

### 过滤不需要的日志 ###
def isNeedDrop(text):
    for dropRule in custom.dropRules:
        if (re.match(dropRule, text) != None):
            return True
    return False

### ------------------------------筛选日志------------------------------ ###
filterList = [] #FilterModel储存实例对象

class FilterModel:
    def __init__(self, name, markCondition, rule):
        self.name = name
        self.markCondition = markCondition
        self.rule = rule
        self.filterItems = [] #储寸符合正则条件的日志

def initFilterResult():
    for obj in custom.filterRules:
        # markCondition存在就返回对应的值，不存在则插入key并设置值，然后返回值
        obj.setdefault("markCondition", "found")
        # 创建FilterModel实例对象，然后将一个个实例加入列表中
        model = FilterModel(obj["filterName"], obj["markCondition"], obj["rule"])
        filterList.append(model)

def analysisFilter(text):
    # 把列表中的实例对象通过下标一个个取出来
    for ruleIndex in range(0, len(filterList)):
        # model是每一个实例
        model = filterList[ruleIndex]
        # 通过下标取出每一个正则
        for index in range(0, len(model.rule)):
            # 拿每一个正则去匹配，如果不为None，加入到列表中
            if (re.match(model.rule[index], text) != None):
                filterList[ruleIndex].filterItems.append(text)

########################### 流程相关代码 ###########################

# 流程规则对象 #
processList = []

# 外面大的每一个的processRule的类
class ProcessModel:
    def __init__(self, name, only, steps):
        self.name = name
        self.only = only
        self.steps = steps
        self.beforeKey = ""
        self.afterKey = ""
        self.processingItems = []
        self.processFinishedItems = []
        self.processErrorItems = []

# processRule.steps里面每一个小的step的类
class ProcessStepModel:
    def __init__(self, stepName, rule, necessary):
        self.stepName = stepName
        self.rule = rule
        self.necessary = necessary

# 流程对象 #
class ProcessItem:
    def __init__(self, name, text, leftSteps):
        self.name = name
        self.logs = text
        self.leftSteps = leftSteps
        self.key = ""

    def isOver(self):
        return len(self.leftSteps) == 0

    def isNextStepAndTryAppendLog(self, text):
        isNextStep = False
        # 遍历leftSteps中每一个步骤
        for step in self.leftSteps:
            # 遍历步骤的每一个rule
            for rule in step.rule:
                if step.necessary:
                    # 如果necessary为True的，就去匹配流程中的正则
                    # 如果匹配到相应的字段，key等于空，执行appendLog并返回ture，否则去看text中有没有key，有返回ture，无返回false
                    if re.match(rule, text) != None:
                        if self.key == "":
                            self.appendLog(text, self.leftSteps.index(step))
                            return True
                        else:
                            if self.key in text:
                                self.appendLog(text, self.leftSteps.index(step))
                                return True
                            else:
                                return False
                else:
                    if re.match(rule, text) != None:
                        if self.key == "":
                            self.appendLog(text, self.leftSteps.index(step))
                            return True
                        else:
                            if self.key in text:
                                self.appendLog(text, self.leftSteps.index(step))
                                return True
        return False
    
    def appendLog(self, text, matchStepIndex):
        # logs=logs+（步骤名称+text） steps中的某一个step的stepName+符合正则的日志text
        self.logs += (self.leftSteps[matchStepIndex].stepName + text)
        # 如果还有剩余流程未执行，该流程的necessary为True，剔除掉当前步骤
        if len(self.leftSteps) > 0:
            if self.leftSteps[matchStepIndex].necessary:
                self.leftSteps = self.leftSteps[matchStepIndex +1:]

# 初始化流程规则对象列表和流程结果列表
def initProcessRulesAndProcessResults():
    # 遍历每个流程,obj
    for obj in custom.processRules:
        steps = []
        # 遍历流程中每个步骤
        for step in obj['steps']:
            # 创建流程中步骤对象实例   步骤名称、正则、步骤是否必须
            processStepModel = ProcessStepModel(step['stepName'], step['rule'], step['necessary'])
            steps.append(processStepModel)
        # 创建流程对象实例  流程名称 流程是否唯一 流程中的所有步骤
        processModel = ProcessModel(obj['processName'], obj['only'], steps)
        # 如果流程中only==False，则说明流程非唯一，需要beforeKey 和 afterKey 来获取 key 值做区分
        if obj['only'] == False:
            processModel.beforeKey = obj['beforeKey']
            processModel.afterKey = obj['afterKey']
        # 把所有流程加入流程规则对象列表中
        processList.append(processModel)

# 分析日志
def analysisProcess(text):
    # 遍历流程规则实例对象
    for result in processList:
        for item in result.processingItems:
            if item.isNextStepAndTryAppendLog(text):
                # 如果剩余流程步骤为0，正在进行的流程对象中删除item，完成的流程对象增加item
                if item.isOver():
                    result.processingItems.remove(item)
                    result.processFinishedItems.append(item)
                return

    for processRule in processList:
        # index 返回字符串开始的索引值
        index = processList.index(processRule)
        # 遍历流程中的steps的第一个step中的所有rule
        for rule in processRule.steps[0].rule:
            # 匹配到该rule，判断该rule所在的necessary是否为True
            if re.match(rule, text) != None:
                if processRule.only:
                    # 找正在处理的该流程并加入到失败队列
                    if len(processList[index].processingItems) > 0:
                        processList[index].processErrorItems.extend(processList[index].processingItems)
                        processList[index].processingItems = []
                item = ProcessItem(processRule.name, processRule.steps[0].stepName + text, processRule.steps[1:])
                # 如果该流程可以同时存在多个，那么就要找出key值
                if processRule.only == False:
                    key = text[text.index(processRule.beforeKey) + len(processRule.beforeKey):text.index(processRule.afterKey)]
                    item.key = key
                processList[index].processingItems.append(item)

# 分析日志结束后，将分析中列表的流程对象添加到异常列表中去
def processingToError():
    for result in processList:
        result.processErrorItems.extend(result.processingItems)
        result.processingItems = []
        for errorItem in result.processErrorItems:
            for step in errorItem.leftSteps:
                if step.necessary:
                    errorItem.logs += step.stepName