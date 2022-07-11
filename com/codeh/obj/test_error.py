import time

try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件时产生异常，那么就会捕获到
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except Exception:
    print('不存在这个异常')
