from BeautifulSoup import BeautifulSoup
html = open("template.html","r")
soup = BeautifulSoup(html.read())
new_html = open("template_new.html","w")
new_html.write(soup.prettify().encode("utf8"))

