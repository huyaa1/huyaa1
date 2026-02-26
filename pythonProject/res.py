import requests
import json

# 定义请求的URL和报文数据
url = 'http://117.72.72.134:8080/gateway/mcp/outChannel/validate?c=WI'
data = {
    "requestId":"hebaojiaoyanma_3453946894536",
    "c":"WI",
    "data":{
        "productId":"A100000013",
        "outChannelOrderId":"66323958403338552251",
        "effDate":"2020-12-20",
        "applyDate":"2020-12-19",
        "totalPremium":"357.00",
        "isNoticeConfirm":"Y",
        "isShareCoverage":"N",
        "discount":"1",
        "applicant":{
            "name":"士发放",
            "birthday":"1980-01-01",
            "sex":"M",
            "idType":"1",
            "idno":"110101198001010117",
            "contactInfo":{
                "mobile":"16351656161",
                "email":"123@qq.com",
                "contactAddress":{
                    "provinceCode":"110000",
                    "cityCode":"110000",
                    "areaCode":"110101"
                }
            },
            "extend":{
                "taxType":"null",
                "realCheckType":"1"
            }
        },
        "insurants":[
            {
                "seqno":"1",
                "name":"华东师范",
                "birthday":"1998-12-22",
                "sex":"F",
                "idType":"2",
                "idno":"4115190221",
                "socialSecurity":"Y",
                "relationshipWithApplicant":"2",
                "relationshipWithPrimaryInsurant":"1",
                "contactInfo":{
                    "email":"123@qq.com"
                },
                "coverages":[
                    {
                        "planType":"0",
                        "sumInsured":"100000.00",
                        "benLevel":"09",
                        "period":"12",
                        "periodDay":"0",
                        "paymentPeriod":"12",
                        "paymentPeriodDay":"0",
                        "actualPrem":"357.00",
                        "units":""
                    }
                ],
                "healthNotes":[
                    {
                        "questionId":"P19100001",
                        "answer":"Y",
                        "healthNoteSeq":"1"
                    }
                ],
                "isRenewal":"N",
                "extend":{
                    "realCheckType":"1"
                }
            }
        ],
        "channelInfo":{
            "mainAgentNo":"H2604Z5I3H",
            "sellerCode":"H2604Z5I3H",
            "sellerName":"",
            "independentPromoter":"H2604Z5I1B"
        },
        "serviceAgreementInfo":{
            "premType":"5"
        },
        "authInfo":{
            "initialChargeMode":"9"
        },
        "others":{
            "imgCheckType":"1",
            "assignEffdate":"Y",
            "extraInfo":{

            }
        }
    }
}

# 将字典类型的 data 转换为 JSON 字符串
json_data = json.dumps(data)

# 设置请求头部
headers = {'Content-Type': 'application/json'}

# 发送 POST 请求，获取响应
response = requests.post(url, data=json_data, headers=headers)

# 输出响应的内容
print(response.text)