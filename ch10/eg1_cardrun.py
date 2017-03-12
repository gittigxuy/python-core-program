 # -*- coding: utf-8 -*-
__author__ = 'xuy'
def safe_float(obj):#安全的float转化
    try:
        result=float(obj)
    except(TypeError,ValueError),e:
        result=str(e)
    return result
def main():
    log=open('cardlog.txt','w')
    try:
        datafile=open('carddata.txt','r')
    except IOError,e:
        log.write("No carddata.txt")
        log.close()
        return
    txns = datafile.readlines()#读取文件中的数据
    datafile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):#isinstance(object, classinfo)   判断实例是否是这个类或者object是变量
            #在这里也就是说：判断result是否是float类型，如果是float类型的话那就将数字进行叠加
            total += result
            log.write('data... processed\n')
        else:#如果不是float类型，那么就将错误写入到日志中
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)
    log.close()

if __name__ == '__main__':
    main()


# def safe_float(object):#将数字进行安全的float转化
#     'safe version of float()'
#     try:
#         retval = float(object)
#     except (TypeError, ValueError), diag:
#         retval = str(diag)
#     return retval#返回转化结果，然后如果是正常的float类型，那么就说明可以正常转化
#
# def main():
#     'handles all the data processing'
#     log = open('cardlog.txt', 'wa')#将内容写入日志中
#     try:
#         ccfile = open('carddata.txt', 'r')#以只读的形式进行文件读取数据
#     except IOError, e:
#         log.write('no txns this month!!!\n')#如果没有carddata的文件的话，那就会产生异常,将异常写入到文件中
#
#     	log.close()
#         return
#     txns = ccfile.readlines()#读取文件中的数据
#     ccfile.close()
#     total = 0.00
#     log.write('account log:\n')
#
#     for eachTxn in txns:
#         result = safe_float(eachTxn)
#         if isinstance(result, float):#isinstance(object, classinfo)   判断实例是否是这个类或者object是变量
#             #在这里也就是说：判断result是否是float类型，如果是float类型的话那就将数字进行叠加
#             total += result
#             log.write('data... processed\n')
#         else:
#             log.write('ignored: %s' % result)
#     print '$%.2f (new balance)' % (total)
#     log.close()
#
# if __name__ == '__main__':
#     main()