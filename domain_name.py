def domain_name(url):
    if 'http://' in url and 'www' not in url:
        first_index = url.find('http://') + 7
        second_index = url[first_index:].find('.') + first_index
        return url[first_index: second_index]
    elif 'https://' in url and 'www' not in url:
        first_index = url.find('https://') + 8
        second_index = url[first_index:].find('.') + first_index
        return url[first_index: second_index]
    elif 'www' in url:
        first_index = url.find('www') + 4
        second_index = url[first_index:].find('.') + first_index
        return url[first_index: second_index]


print(domain_name('http://github.com/carbonfive/raygun'))
print(domain_name('http://www.zombie-bites.com'))
print(domain_name('https://www.cnet.com'))
print(domain_name('http://google.com'))
print(domain_name('http://google.co.jp'))
print(domain_name('www.xakep.ru'))
print(domain_name('https://youtube.com'))
