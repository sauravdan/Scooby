def union(a, b):
    return list(set(a)|set(b))

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            #print url
            links.append(url)
            #print links
            page = page[endpos:]
        else:
            #break
            #print links
            return links

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            #print(content)
            add_page_to_index(index, page, content)
            tocrawl = list(set(tocrawl)|set(get_all_links(content)))
            crawled.append(page)
    return index

def add_to_index(index, keyword, url):
    for value in index:
        if value[0] == keyword:
            value[1].append(url)
            return
    index.append([keyword,[url]])
    return

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for value in index:
        if value[0] == keyword:
            return value[1]
    return []


print(lookup(crawl_web('http://xkcd.com/353'), pant))
#print(get_all_links(get_page('http://xkcd.com/353')))
