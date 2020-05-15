# -*- coding:utf-8 -*-
import requests, time, sys, re
import urllib, zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

HOSTNAME = '127.0.0.1'


def readSQLCase():  # 读取数据库中相应的接口用例数据
    sql = "select * from autotest.apitest_apistep where ApiTest_id=3"
    conn = pymysql.connect(user='root', password='123456', db='autotest', host='127.0.0.1', port='3306',
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
    strinfo = re.compile('{TaskId}')
    strinfo1 = re.compile('{AssertId}')
    strinfo2 = re.compile('{PointId}')
    assertinfo = re.compile('{assertno}')
    tasknoinfo = re.compile('{taskno}')
    schemainfo = re.compile('{schema}')
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
            new_url = 'http://' + url
        else:
            url = strinfo.sub(TaskId, url)
            param = strinfo.sub(TaskId, param)
            param = tasknoinfo.sub(taskno, param)
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
                results = urllib.request.urlopen(req).read()
                print('response is get')
                print(results)
                res = readRes(results, '')
            # print results
            if 'pass' == res:
                writeResult(case_id, '1')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, '0')


def writeResult(case_id, result):
    pass


def TaskId(results):
    pass


def taskno(results):
    pass


def urlParam(param):
    pass


def readRes(result, done):
    pass
