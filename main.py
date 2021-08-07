#coding:utf-8
from url_maker import link
from get_url import get_url
from spyder import craw
from html_outputer import html_outputer

def main(web_url = 'https://doupocangqiong1.com/1/list_piaotian/'):
    param, zhangjie_name = get_url(web_url)
    url = 'https://doupocangqiong1.com/'
    full_url_list = link(url, param)
    length = len(full_url_list)
    bid = 1
    cid = 873530
    print(len(param))
    print(len(zhangjie_name))
    # for zhangjie in full_url_list:
    #     # with open('folder/')
    #     # content = craw(zhangjie, bid,cid)
    #     # cid+=1
    #     print(zhangjie)
    #     break
    c=1
    for item in range(1929):
        with open('folder/{0}.txt'.format(c), 'w', encoding='UTF-8-sig') as file:
            content = craw(full_url_list[item], bid, cid)
            file.write(content)
            file.close()
        cid+=1
        c+=1



if __name__ == '__main__':
    main()