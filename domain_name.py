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
    else:
        index = url.find('.')
        return url[:index]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
