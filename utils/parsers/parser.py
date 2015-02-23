from bs4 import BeautifulSoup

html = open("template1_1.html","r")


def template2():
    soup = BeautifulSoup(html.read())
    images = soup.findAll("img",{"class":"image"})
    count = 1
    for image in images:
        image["src"] = "{{image" + str(count) + "}}"
        print image
        count += 1


    count = 1
    text_fields = soup.findAll("div",{"class":"text"})
    for text in text_fields:
        text.insert(0,"{{text" + str(count) + "}}")
        print text
        count += 1


def template1():

    soup = BeautifulSoup(html.read())
    images = soup.findAll("img",{"class":"image"})
    new_tag = soup.new_tag("p")

    count = 1
    for image in images:

        image.parent.img.replace_with(new_tag)

        count += 1
    print soup.prettify()
#template1()

# <a href="http://example.com/">I linked to <b>example.net</b></a>


    # count = 1
    # text_fields = soup.findAll("div",{"class":"text"})
    # for text in text_fields:
    #     text.insert(0,"{{text" + str(count) + "}}")
    #     print text
    #     count += 1







# new_html = open("template_new.html","w")
# new_html.write(soup.prettify().encode("utf8"))




