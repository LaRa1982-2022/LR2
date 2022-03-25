Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def getContent(url, regex):
    current_proxy = proxy.get_proxy()
    print(current_proxy)
    headers = {'User-Agent': ua.random}
    proxy.get_proxy_list()
    r = requests.get(url, headers=headers, proxies={'http': 'https://' + current_proxy})
    obj = html.fromstring(r.content)
    list = obj.xpath(regex)
    if len(list) == 0:
        proxy.delete_proxy(current_proxy)
        getContent(url, regex)
    else:
        return list