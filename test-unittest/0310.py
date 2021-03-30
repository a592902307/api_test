import requests
import json

app_key='Z8X4SWwBTiCuiN8Yk1e6naEG'
secret_key='KR7SsW8AKF91xPOvd4XiA3GakEtiONAB'
img_url = 'http://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpn.gexing.com%2Fshaitu%2F20120730%2F1635%2F5016475970b26.jpg&refer=http%3A%2F%2Fpn.gexing.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1617948930&t=d4d2f6f74a1adf96d7b37724373713c2'

#获取token
get_token_url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
token=requests.get(url=get_token_url).json().get('access_token')
# print(token)

#识别图片文字
ocr_url='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token={}'.format(token)
data={"url":img_url}
res=requests.post(url=ocr_url,data=data)
print(json.dumps(res.json(),indent=2,ensure_ascii=False))

