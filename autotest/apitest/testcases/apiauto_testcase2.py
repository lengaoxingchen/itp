# -*- coding:utf-8 -*-
import requests, time, sys, re
import urllib.request, zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

from autotest.apitest.testcases.apiauto_testcase3 import readRes

HOSTNAME = '127.0.0.1'


def readSQLCase():  # 读取数据库中相应的接口用例数据
    sql = "select * from autotest.apitest_apis"
    conn = pymysql.connect(user='root', password='123456', db='autotest', host='123.57.135.88', port='3306',
                           charset='utf-8')
    cursor = conn.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    case_list = []
    for ii in info:
        case_list.append(ii)
        interfaceTest(case_list)
    conn.commit()
    cursor.close()
    conn.close()


def interfaceTest(case_list):
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{seturl}')
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[3]
            url = case[2]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return '测试用例格式不正确%s' % e
        if param == '':
            new_url = 'http://' + 'api.test.com.cn' + url
        elif param == 'null':
            new_url = strinfo.sub(str(seturl('seturl')), url)
        else:
            url = strinfo.sub(str(seturl('seturl')), url)
            new_url = 'http://' + '127.0.0.1' + url
            request_urls.append(new_url)
        if method.upper() == 'GET':
            headers = {'Authorization': '', 'Content_Type': 'application/json'}
            if "=" in urlParam(param):
                data = None
                print(str(case_id) + 'request is get' + new_url + '?' + urlParam(param).encode('utf-8'))
                results = requests.get(new_url + '?' + urlParam(param).enncode('utf-8'), data, headers=headers).text
                print('response is get' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, '')
            else:
                print('request is get' + new_url + 'body is' + urlParam(param).encode('utf-8'))
                data = None
                req = urllib.request.Request(url=new_url, data=data, headers=headers, method="GET")
                try:
                    results = urllib.request.urlopen(req).read()
                    print('response is get')
                    print(results)
                except Exception as e:
                    return caseWriteResult(case_id, '0')
                res = readRes(results, '')
                # print results
                if 'pass' == res:
                    res_flags.append('pass')
                    writeResult(case_id, '1')
                    caseWriteResult(case_id, '1')
                else:
                    res_flags.append('fail')
                    writeResult(case_id, '0')
                    caseWriteResult(case_id, '0')
        if method.upper() == 'PUT':
            headers = {'Host': HOSTNAME, 'Connection': 'keep-alive', 'CredentialId': id,
                       'Content-Type': 'application/json'}
            body_data = param
            results = requests.put(url=url, data=body_data, headers=headers)
            responses.append(results)
            res = readRes(results, res_check)
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
        if method.upper() == "PATCH":
            headers = {'Authorization': '', 'CredentialId ': id, 'Content-Type': 'application/json'}
            data = None
            results = requests.patch(new_url + '?' + urlParam(param).encode('utf-8'), data, headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
        if method.upper() == "POST":
            headers = {'Authorization': '', 'CredentialId ': id, 'Content-Type': 'application/json'}
            if "=" in urlParam(param):
                data = None
                results = requests.patch(new_url + '?' + urlParam(param).encode('utf-8'), data, headers=headers).text
                print(' response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, '')
            else:
                print(str(case_id) + ' request is ' + new_url + ' body is ' + urlParam(param).encode(
                    'utf-8'))

                results = requests.post(new_url, data=urlParam(param).encode('utf-8'), headers=headers).text
                print(' response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, res_check)
                if 'pass' == res:
                    writeResult(case_id, '1')
                    res_flags.append('pass')
                else:
                    res_flags.append('fail')
                    writeResult(case_id, '0')


def caseWriteResult(case_id, param):
    pass


def writeResult(case_id, result):
    pass


def TaskId(results):
    pass


def taskno(results):
    pass


def urlParam(param):
    param1 = param.replace('&quot;', '"')
    return param1


def seturl(set):
    global setvalue
    sql = "select * from autotest.set_set"
    conn = pymysql.connect(user='root', password='123456', db='autotest', host='123.57.135.88', port='3306',
                           charset='utf-8')
    cursor = conn.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    print(info)
    conn.commit()
    cursor.close()
    conn.close()
    if info[0][0] == set:
        setvalue = info[0][1]
        print(setvalue)
    return setvalue
