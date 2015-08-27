def get_next_target(page):
    page = ''
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find("'", start_quote + 1)
    url = page[start_quote+1 : end_quote]
    return url, end_quote
