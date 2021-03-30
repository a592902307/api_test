#coding:utf-8

"""
    dropRules 使用说明：
    功能：丢弃不值得关注的日志
    示例：
    dropRules = [
        "正则A",
        "正则B"
    ]
    符合正则A或正则B的日志字符串将会被丢弃，最终输出的 html 文件中将看不到符合上述正则的字符串
"""
dropRules = [
    r"((.*)Active call object not found(.*))",
    r"((.*)can't find active callItem(.*))",
    r"((.*)Call object not found(.*))",
    r"((.*)#ZOSLOG#(.*))",
    r"((.*)DbufCreate invalid size 0(.*))",
    r"((.*)disable error concealing(.*))"
]


"""
    beautifulRules 使用说明：
    功能：替换错误码数值为中文、替换状态值为中文
    示例 ：
    beautifulRules = [
        {
            "rule" : "正则A",
            "content" : 
            [
                "string 1", "string 2",
                "string 3", "string 4",
            ]
        },
        {
            "rule" : "正则B",
            "content" : 
            [
                "string A", "string B",
                "string C", "string D"
            ]
        }
    ]
    符合正则A的日志字符串 text，如果 text 中出现了 string 1，那么就会被替换成 string 2，如果 text 中出现了 string 3，那么就会被替换成 string 4
    符合正则B的日志字符串 text，如果 text 中出现了 string A，那么就会被替换成 string B，如果 text 中出现了 string C，那么就会被替换成 string D
"""
beautifulRules = [
    #自动配置
    {
        "rule": r"((.*)notify cp(.*)failed code(.*))",
        "content":
        [
            "code<57345>", "code<连接超时>",
            "code<57346>", "code<网络错误>",
            "code<57347>", "code<请求被拒绝（403 forbidden）>",
            "code<57348>", "code<服务器内部错误（配置服务器返回500）>",
            "code<57349>", "code<配置文件xml格式错误>",
            "code<57350>", "code<暂时禁止使用RCS业务>",
            "code<57351>", "code<停机导致RCS业务无法使用>",
            "code<57354>", "code<无效的token>",
            "code<57357>", "code<大boss返回错误>",
            "code<57358>", "code<用户不在白名单>",
            "code<57359>", "code<大boss超时>",
            "code<57360>", "code<等待APP输入token超时>",
            "code<57361>", "code<第一个200 ok有body>",
            "code<57362>", "code<301重定向超过限制次数>",
            "code<57363>", "code<平台下发的配置版本号错误>",
            "code<57364>", "code<RCS业务关闭导致无法使用>",
            "code<57365>", "code<永久禁止使用RCS业务>",
            "code<57366>", "code<大boss返回错误>",
        ]
    },
    # 注册
    {
        "rule": r"((.*)MtcCliCbLoginFailed(.*))",
        "content":
        [
            "StatCode 57603", "57603鉴权失败，无效的用户名或密码",
            "StatCode 57604", "57604使用无效的用户名",
            "StatCode 57605", "57605注册超时",
            "StatCode 57606", "57606服务器忙",
            "StatCode 57607", "57607服务器不可达",
            "StatCode 57608", "57608请求被拒绝",
            "StatCode 57609", "57609服务不存在",
            "StatCode 57610", "57610dns查询失败",
            "StatCode 57611", "57611网络错误",
            "StatCode 57612", "57612网络侧要求重新注册",
            "StatCode 57614", "57614服务器内部错误",
            "StatCode 57615", "57615没有资源",
            "StatCode 57616", "57616被踢下线",
            "StatCode 57617", "57617sip错误",
            "StatCode 57618", "57618注销错误",
            "StatCode 57619", "57619无效的地址",
            "StatCode 57620", "57620等待APP输入SIP密码超时",
            "StatCode 57621", "57621平台数据不一致",
            "StatCode 57622", "57622注册用户关闭或者停机",
            "StatCode 57623", "57623注册用户的pvi不一致",
            "StatCode 57624", "57624注册用户不存在",
        ]
    },
    # Pager Mode点对点消息
    {
    "rule": r"((.*)SprocOnRieEvntP call PMsgSendFailed msg(.*))",
    "content":
        [
            "code<59905>", "code<59905消息禁止>",
            "code<59907>", "code<59907消息未被认可>",
            "code<59908>", "code<59908参与者临时不可用>",
            "code<59909>", "code<59909请求终止>",
            "code<59910>", "code<59910服务器内部错误>",
            "code<59911>", "code<59911服务不可用>",
            "code<59912>", "code<59912请求超时>",
            "code<59913>", "code<59912被叫方未注册>",
            "code<59914>", "code<59914网络错误>"
        ]
    },
    #Large Mode点对点消息
    {
        "rule": r"((.*)SprocOnRieEvntL call LMsgSendFailed msg(.*))",
        "content":
        [
            "code<59905>", "code<59905消息禁止>",
            "code<59907>", "code<59907消息未被认可>",
            "code<59908>", "code<59908参与者临时不可用>",
            "code<59909>", "code<59909请求终止>",
            "code<59910>", "code<59910服务器内部错误>",
            "code<59911>", "code<59911服务不可用>",
            "code<59912>", "code<59912请求超时>",
            "code<59913>", "code<59912被叫方未注册>",
            "code<59914>", "code<59914网络错误>"
        ]
    },
    # 上传文件
    {
        "rule": r"((.*)SprocOnRieEvntFtHttp call FtHttpUploadFailed sess(.*))",
        "content":
        [
            "code<59960>", "code<59960传输服务不可用>",
            "code<59961>", "code<59961传输打开文件失败>",
            "code<59962>", "code<59962传输文件太大>",
            "code<59963>", "code<59963传输打开http错误>",
            "code<59964>", "code<59964传输打开传输错误>",
            "code<59965>", "code<59965传输文件取消>",
            "code<59966>", "code<59966传输文件打开文件失败>",
            "code<59967>", "code<59967传输http连接错误>",
            "code<59968>", "code<59968传输gab引导错误>",
            "code<59969>", "code<59969传输时http断开>",
            "code<59970>", "code<59970传输时http发送错误>",
            "code<59971>", "code<59971传输时http接收失败>",
            "code<59972>", "code<59972传输失败fthttp pick body fail>",
            "code<59973>", "code<59973传输未知类型fthttp unknown type>",
            "code<59974>", "code<59974传输文件不存在fthttp file not exist>",
            "code<59975>", "code<59975传输文件过期fthttp file expired>",
            "code<59976>", "code<59976传输错误响应fthttp bad response>",
            "code<59977>", "code<59977传输文件服务不可用fthttp server unavail>",
            "code<59978>", "code<59978传输文件请求被禁止fthttp request forbidden>",
            "code<59979>", "code<59979传输文件请求超时fthttp request timeout>"
        ]
    }
]

"""
    filterRules 使用说明：
    功能：筛选出自己有需要的信息
    示例 ：
    filterRules = [
        {
            "filterName" : "名称1",
            "markCondition" : "found",
            "rule" : ["正则A"]
        },
        {
            "filterName" : "名称2",
            "rule" : ["正则B", "正则C", ...]
        }
    ]
    最终输出的html中会有一个日志筛选按钮，里面又会有名称1和名称2两个子按钮
    点击名称1按钮，会出现符合正则A字符串；点击名称2按钮，会出现符合正则B和正则C的字符串
    markCondition字段的值为：found（筛选到符合条件的值则标记红点），notFound（未筛选到符合条件的值则标记红点），no（无论筛选结果如何均不标记红点），未设置该字段则默认为found
"""
filterRules = [
    {
        "filterName": "回调成功",
        "markCondition": "found",
        "rule":
            [
                r"((.*)notify cp@(.*)ok.)",
                r"((.*)Mtc_CapCbGetCapQOk(.*))",
                r"((.*)SprocOnRieEvntP call PMsgSendOk(.*))",
                r"((.*)SprocOnRieEvntL call LMsgSendOk msg(.*))",
                r"((.*)SprocOnRieEvntFtrsf call FileSendOk sess(.*))",
                r"((.*)SprocOnRieEvntFresume call SendOk sess(.*))",
                r"((.*)SprocOnRleEvnt call PushGInfoShareOk sess(.*))",
                r"((.*)SprocOnRieEvntFtHttp call FtHttpUplaodOk sess(.*))",
                r"((.*)SprocOnRieEvntP call PMsgRecvMsg msg(.*))",
                r"((.*)SprocOnRieEvntL call LMsgRecvMsg msg(.*))",
                r"((.*)SprocOnRieEvntFtHttp call FtHttpDownloadOk sess(.*))",
                r"((.*)SprocOnRieEvntFtHttp call FtHttpRefreshOk sess(.*))",
                r"((.*)SprocOnRieEvntN call ImdnRecvDeliNtfy imdn(.*))",
                r"((.*)SprocOnRieEvntHttp call ChatbotQryLst OK sess(.*))",
                r"((.*)SprocOnRieEvntHttp call ChatbotQryInfo OK sess(.*))",
                r"((.*)SprocOnRieEvntP call PMsgSendOk msg(.*))",
                r"((.*)SprocOnRieEvntP call PMsgRecvMsg msg(.*))",
                r"((.*)SprocOnRieEvntP call PMsgSendOk msg(.*))"
            ]
    },
    {
        "filterName": "自动配置/开通错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)notify cp(.*)failed(.*))"
            ]
    },
    {
        "filterName": "注册错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)MtcCliCbLoginFailed:(.*))"
            ]
    },
    {
        "filterName": "能力查询错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)query failed cookie(.*))"
            ]
    },
    {
        "filterName": "发送消息错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)SprocOnRieEvntP call PMsgSendFailed(.*))",
                r"((.*)SprocOnRieEvntL call LMsgSendFailed msg(.*))",
                r"((.*)SprocOnRieEvntFtrsf call FileSendFailed sess(.*))",
                r"((.*)SprocOnRieEvntFresume call SendFailed sess(.*))",
                r"((.*)SprocOnRleEvnt call PushGInfoShareFailed sess(.*))"
            ]
    },
    {
        "filterName": "文件传输错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)SprocOnRieEvntFtHttp call FtHttpUploadFailed sess(.*))",
                r"((.*)SprocOnRieEvntP call PMsgSendFailed msg(.*))",
                r"((.*)SprocOnRieEvntFtHttp call FtHttpDwonloadFailed sess(.*))",
                r"((.*)SprocOnRieEvntFtHttp call FtHttpRefreshFailed sess(.*))"
            ]
    },
    {
        "filterName": "消息递送错误",
        "markCondition":"found",
        "rule":
            [
                r"(.*)SprocOnRieEvntN call ImdnRecvDeliFailed mdn(.*)"
            ]
    },
    {
        "filterName": "Maap功能错误",
        "markCondition":"found",
        "rule":
            [
                r"((.*)SprocOnRieEvntHttp call ChatbotQryLst Failed sess(.*))",
                r"((.*)SprocOnRieEvntHttp call ChatbotQryInfo Failed sess(.*))",
                r"((.*)SprocOnRieEvntP call PMsgSendFailed msg(.*))"
            ]
    }
]

"""
    processRules 使用说明：
    功能：获取流程中的日志以及发现异常流程
    示例：
    processRules = [
        {
            "processName" : "流程1",
            "only": True,
            "steps": 
            [
                {
                    "stepName" : "步骤1",
                    "rule" : ["能够匹配步骤1的正则A"],
                    "necessary" : True
                },
                {
                    "stepName" : "步骤2",
                    "rule" : ["能够匹配步骤2的正则B"， “能够匹配步骤2的正则C”],
                    "necessary" : True
                },
                {
                    "stepName" : "步骤3",
                    "rule" : ["能够匹配步骤3的正则D"],
                    "necessary" : True
                }
            ]
        },
        {
            "processName" : "流程2",
            "only": False,
            "beforeKey" : "string1",
            "afterKey" : "string2",
            "steps": 
            [
                {
                    "stepName" : "步骤1",
                    "rule" : ["能够匹配步骤1的正则A"],
                    "necessary" : True
                },
                {
                    "stepName" : "步骤2",
                    "rule" : ["能够匹配步骤2的正则B"， “能够匹配步骤2的正则C”],
                    "necessary" : False
                },
                {
                    "stepName" : "步骤3",
                    "rule" : ["能够匹配步骤2的正则E"],
                    "necessary" : True
                }
            ]
        }
    ]
    processName 表示流程名称，最终html文件中的流程按钮中会出现"流程1"、"流程2"的子按钮;
    only 表示该流程是否是唯一的，如果不是唯一的，还需要额外提供key值来进行区分;
    beforeKey 和 afterKey 用来获取 key 值，仅当 only 为 True 时有效。比如"流程2"有字符串 string1ABCDEFstring2，那么就能得到中间的key值为 ABCDEF。比如通话流程可以同时存在多个，那么它的 key 值就是 MtcCallIdKey。
    steps 表示流程步骤。stepName 表示步骤名称，rule 表示能匹配这个步骤的正则表达式，necessary表示这个步骤是不是必须的
"""
processRules = [
    {
        "processName": "自动配置/开通流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用自动配置接口：",
                    "rule": [r"((.*)Mcf_Cp bAutoCp(.*)server type(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "自动配置结果：",
                    "rule": [r"((.*)notify cp(.*)ok.)", r"((.*)notify cp(.*)failed code(.*))"],
                    "necessary": True
                }
            ]
    },
    {
        "processName": "注册流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用注册接口：",
                    "rule": [r"((.*)endp start register via(.*)server(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "注册结果：",
                    "rule": [r"((.*)MtcCliCbLoginOk(.*))", r"((.*)MtcCliCbLoginFailed(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "能力查询流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用能力查询接口：",
                    "rule": [r"((.*)CapQryOneViaPresImd cap(.*)ok.)"],
                    "necessary": True
                },
                {
                    "stepName": "能力查询结果：",
                    "rule": [r"((.*)Mtc_CapCbGetCapQOk(.*))", r"((.*)query failed cookie(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "Pager点对点消息流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用Pager点对点消息接口：",
                    "rule": [r"((.*)send message(.*)iMsgType(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "Pager点对点消息结果：",
                    "rule": [r"((.*)SprocOnRieEvntP call PMsgSendOk msg(.*))",
                             r"((.*)SprocOnRieEvntP call PMsgSendFailed msg(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "Lager点对点消息流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用Lager点对点消息接口：",
                    "rule": [r"((.*)large msg(.*)send to one partp.)"],
                    "necessary": True
                },
                {
                    "stepName": "Lager点对点消息结果：",
                    "rule": [r"((.*)SprocOnRieEvntP call LMsgSendOk msg(.*))",
                             r"((.*)SprocOnRieEvntP call LMsgSendFailed msg(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "http文件传输流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用http文件传输接口：",
                    "rule": [r"((.*)FtHttpUpload send FtHttp(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "http文件传输结果：",
                    "rule": [r"((.*)SprocOnRieEvntFtHttp call FtHttpUplaodOk sess(.*))",
                             r"((.*)SprocOnRieEvntFtHttp call FtHttpUploadFailed sess(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "Chatbot列表查询流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用Chatbot列表查询接口：",
                    "rule": [r"((.*)ChatbotQryList send Http(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "Chatbot列表查询结果：",
                    "rule": [r"((.*)SprocOnRieEvntHttp call ChatbotQryLst OK sess(.*))",
                             r"((.*)SprocOnRieEvntHttp call ChatbotQryLst Failed sess(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "Chatbot详情查询流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用Chatbot详情查询接口：",
                    "rule": [r"((.*)ChatbotQryInfo send Http(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "Chatbot详情查询结果：",
                    "rule": [r"((.*)SprocOnRieEvntHttp call ChatbotQryInfo OK sess(.*))",
                             r"((.*)SprocOnRieEvntHttp call ChatbotQryInfo Failed sess(.*))"],
                    "necessary": True
                },
            ]
    },
    {
        "processName": "Chatbot上行流程",
        "only": True,
        "steps":
            [
                {
                    "stepName": "调用Chatbot上行接口：",
                    "rule": [r"((.*)send message(.*)iMsgType(.*))"],
                    "necessary": True
                },
                {
                    "stepName": "Chatbot上行结果：",
                    "rule": [r"((.*)SprocOnRieEvntP call PMsgSendOk msg(.*))",
                             r"((.*)SprocOnRieEvntP call PMsgSendFailed msg(.*))"],
                    "necessary": True
                },
            ]
    }
]

# def getMediaChannelInformation(text):
#     if (
#         re.match(r"(.*)JCSDK:(.*)MtcConfJoinOkNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfJoinDidFailNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfJoinedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfDidLeaveNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfCancelReservationOkNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfCancelReservationDidFailNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfLeavedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfErrorNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfPropertyChangedNotfication(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfDataReceivedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfBypassDataReceivedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfTextReceivedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcSgwDeliInviteOkNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcSgwDeliInviteDidFailNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfInviteReceivedNotification(.*)", text) != None or
#         re.match(r"(.*)JCSDK:(.*)MtcConfCancelReceivedNotification(.*)", text) != None or
#         re.match(r"(.*)ConfJoinRoom(.*)", text) != None or
#         re.match(r"(.*)Leave conf(.*)", text) != None or
#         re.match(r"(.*)ConfCancelReservation(.*)", text) != None
#     ):
#         if (re.match(r"(.*)JCSDK:(.*)MtcConfDidLeaveNotification(.*)", text) != None or re.match(r"(.*)JCSDK:(.*)MtcConfLeavedNotification(.*)", text) != None):
#             return text + "<br/>"
#         return text
#     return None

