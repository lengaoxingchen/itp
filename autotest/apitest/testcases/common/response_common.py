def read_res(res, res_check):
    response = res.decode().replace('":"', "=").replace('":', "=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in response:
            pass
        else:
            return '错误,返回参数和预期结果不一致' + s
        return 'pass'
