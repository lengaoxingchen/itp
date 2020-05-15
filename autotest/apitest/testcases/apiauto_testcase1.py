from urllib import request

from autotest.apitest.testcases.common.response_common import read_res

if __name__ == '__main__':
    url = 'http://' + '127.0.0.1:8000/' + 'login'
    headers = {'Authorization': '', 'Content_Type': 'application/json'}
    data = None
    req = request.Request(url=url, headers=headers, data=data, method='GET')
    print('request is ' + url)
    results = None
    try:
        results = request.urlopen(req).read()
        print('response is get:')
        print(results)
    except SystemError as e:
        print('error')
    res = read_res(results, 'login')
    print(res)
    print('Done!')
