from get_url import get_url

def link(domain, param):
    list = []
    for right_param in param:
        list.append(domain+right_param)
    return list
if __name__ == '__main__':
    web_url = 'https://doupocangqiong1.com/1/list_piaotian/'
    param = get_url(web_url)
    link('https://doupocangqiong1.com/', param)