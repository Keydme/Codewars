# coding:utf-8
import requests
import time
from multiprocessing.dummy import Pool
import re

def get_content(url):
    print("正在获取：", url)
    # get方法是一个阻塞的方法
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        name = url.split("/")[-1]
        with open(f"D:\m3u8\{name}.ts", "wb") as f:
            f.write(resp.content)
        print(name + "下载成功")

headers = {
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36(KABUL, like Gecko) "
                            "Chrome/86.0.4240.198Safari/537.36 "
        }
url = "https://web-vod-xdrive.xunlei.com/ts_downloader?client_id=Xqp0kJBXWhwaTpB6&url=https%3A%2F%2Fvod1493-aliyun06-vip-lixian.xunlei.com%2Fdownload%2F%3Ffid%3DSEx4T-*ABSVh8Ctu0ycAob98TrFQvxoAAAAAAPfdbRWx7ftUsYizwT2C0aYpn5ly%26mid%3D666%26threshold%3D251%26tid%3D2976FF163A1DDF9DC0ADBED8EBF9A955%26srcid%3D0%26verno%3D2%26pk%3Dxdrive%26e%3D1676312004%26g%3DF7DD6D15B1EDFB54B188B3C13D82D1A6299F9972%26i%3D484C784FFF80052561F02B6ED32700A1BF7C4EB1%26ui%3D795288450%26t%3D1%26hy%3D0%26ms%3D1312470%26th%3D131247%26pt%3D0%26f%3D1752912%26alt%3D0%26pks%3D654%26rts%3D%26tras%3D1%26fileid%3DVMSIG5xS7AxiGo3pJfTlmu-0A1%26clientid%3DXqp0kJBXWhwaTpB6%26cliplugver%3D%26userid%3D795288450%26projectid%3D2rvk4e3gkdnl7u1kl0k%26vip%3DFREE%26clientver%3D%26spr%3Dplaytrans%26vc%3Dhevc%26fext%3Dmp4%26at%3D13536823A954CEC67A3498889714F16A"
resp = requests.get(url=url, headers=headers).text
index_list = re.findall(r'https(.*?).ts', resp)
ts_urls = []
for i in index_list:
    title = i.split("/")[-1]
    ts_url = "https" + i + ".ts"
    ts_urls.append(ts_url)
start_time = time.time()

# 实例化一个线程池对象
pool = Pool(30)
# 将列表中的每一个列表元素传递给get_content中进行处理。
content = pool.map(get_content, ts_urls)

end_time = time.time()
print('%d second'% (end_time-start_time))
pool.close()
pool.join()
