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
            links.append(url)
            page = page[endpos:]
        else:
            break
            return links

def get_page(url):
    try:
        import urllib
        return urllib.open(url).read()
    except:
        return ""

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

def add_to_index(index, keyword, url):
    for value in index:
        if value[0] == keyword:
            value[1].append(url)
            return
    index.append([keyword,[url]])
    return

def lookup(index, keyword):
    for value in index:
        if value[0] == keyword:
            return value[1]
    return []

get_all_links('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')


