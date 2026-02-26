#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: ceshixiaoniu
@Contact: 904653439@qq.com
@File: test1.py
@Time: 2024/12/21 15:15
@Last Modified by: ceshixiaoniu
@Last Modified time: 2024/12/21 15:15
@Description:

"""
import requests
import json

# 目标URL
url = 'http://117.72.72.134:8080/gateway/mcp/outChannel/validate'

# 入参数据
data = {
    "requestId": "hebaojiaoyanma_3453946894536",
    "c": "WI",
    "data": {
        "productId": "A100000013",
        "outChannelOrderId": "66323958403338552251",
        "effDate": "2020-02-20",
        "applyDate": "2020-12-19",
        "totalPremium": "624.00",
        "isNoticeConfirm": "Y",
        "isShareCoverage": "N",
        "discount": "1",
        "applicant": {
            "name": "刘建汉",
            "birthday": "1948-12-07",
            "sex": "M",
            "idType": "1",
            "idno": "51310119881207121X",
            "contactInfo": {
                "mobile": "16351656161",
                "email": "123@qq.com",
                "contactAddress": {
                    "provinceCode": "110000",
                    "cityCode": "110000",
                    "areaCode": "110101"
                }
            },
            "extend": {
                "taxType": "null",
                "realCheckType": "1"
            }
        },
        "insurants": [
            {
                "seqno": "1",
                "name": "刘建汉",
                "birthday": "1988-12-07",
                "sex": "M",
                "idType": "1",
                "idno": "51310119881207121X",
                "socialSecurity": "Y",
                "relationshipWithApplicant": "1",
                "relationshipWithPrimaryInsurant": "1",
                "contactInfo": {
                    "email": "11123@qq.com"
                },
                "coverages": [
                    {
                        "planType": "0",
                        "sumInsured": "100000.00",
                        "benLevel": "09",
                        "period": "12",
                        "periodDay": "0",
                        "paymentPeriod": "12",
                        "paymentPeriodDay": "0",
                        "actualPrem": "624.00",
                        "units": ""
                    }
                ],
                "healthNotes": [
                    {
                        "questionId": "P19100001",
                        "answer": "Y",
                        "healthNoteSeq": "1"
                    }
                ],
                "isRenewal": "N",
                "extend": {
                    "realCheckType": "1"
                },
                "realCheck": True
            }
        ],
        "serviceAgreementInfo": {
            "premType": "5"
        },
        "authInfo": {
            "initialChargeMode": "9"
        },
        "others": {
            "imgCheckType": "1",
            "assignEffdate": "Y",
            "extraInfo": {}
        }
    }
}

# 将数据转换为JSON格式
json_data = json.dumps(data)

# 设置请求头部，指定发送JSON数据
headers = {
    'Content-Type': 'application/json'
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json_data)

# 打印响应内容
print(response.text)