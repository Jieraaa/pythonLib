# coding=utf-8
import urllib2
import urllib
import sys
import time
from bs4 import BeautifulSoup

# 获取某段时间某个词语的搜索条目数
# start_str 开始日期 '2012-04-02 00:00:00'
# end_str   结束日期 '2012-04-09 00:00:00'
# wb        搜索词   'test'
def get_baidu_search_nums(start_str, end_str, wb):
    start_arr = time.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    start = str(int(time.mktime(start_arr)))
    end_arr = time.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    end = str(int(time.mktime(end_arr)))
    gpc = 'stf=' + start + ',' + end + '|stftype=2'
    url = 'http://www.baidu.com/s?wd=' + urllib.quote(wb.decode(sys.stdin.encoding).encode('gbk')) \
          + '&gpc=' + urllib.quote(gpc.decode(sys.stdin.encoding).encode('gbk'))
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read(), "html.parser")
    text = soup.select('div.nums')[0].get_text()
    return filter(str.isdigit, text.encode('utf-8'))
