# -*- coding: utf-8 -*-            
# @Author : 测试小牛
# @Time : 03/09/2023 11:32
import unittest
import requests
from BeautifulReport import BeautifulReport

from res import json_data


class APITestCase(unittest.TestCase):
    print("222211")

    def test_api(self):
        print("2222333")

        url = "http://117.72.72.134:8080/gateway/mcp/outChannel/validate?c=WI"

        headers = {"Content-Type": "application/json"}
        payload = {
    "requestId": "hebaojiaoyanma_3453946894536",
    "c": "WI",
    "data": {
        "productId": "A100000013",
        "outChannelOrderId": "66323958403338552251",
        "effDate": "2020-12-20",
        "applyDate": "2020-12-19",
        "totalPremium": "357.00",
        "isNoticeConfirm": "Y",
        "isShareCoverage": "N",
        "discount": "1",
        "applicant": {
            "name": "士发放",
            "birthday": "1980-01-01",
            "sex": "M",
            "idType": "1",
            "idno": "110101198001010117",
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
                "name": "华东师范",
                "birthday": "1998-12-22",
                "sex": "F",
                "idType": "2",
            "idno": "12321312312",
                "socialSecurity": "Y",
                "relationshipWithApplicant": "2",
                "relationshipWithPrimaryInsurant": "1",
                "contactInfo": {
                    "email": "123@qq.com"
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
                        "actualPrem": "357.00",
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
                "realCheck": "true"
            }
        ],
        "channelInfo": {
            "mainAgentNo": "H2604Z5I3H",
            "sellerCode": "H2604Z5I3H",
            "sellerName": "",
            "independentPromoter": "H2604Z5I1B"
        },
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
    }}

        response = requests.post(url, json=payload, headers=headers)
        print(response.status_code)

        self.assertEqual(response.status_code, 200)
        print("24444")



if __name__ == "__main__":


    suite = unittest.TestSuite()
    suite.addTest(APITestCase('test_api'))
    # 运行测试并生成报告
    result = BeautifulReport(suite)
    result.report(
        description='小牛的接口自动化测试用例报告',
        filename='test_report.html',
        report_dir='D:\\code\\pythonProject\\report'
    )

    print(result.filename)
