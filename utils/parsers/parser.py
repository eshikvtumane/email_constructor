from bs4 import BeautifulSoup

class Parser():
    def __init__(self,template):
        self.html = template
        self.template1_out = "generated_templates/template1.html"
        self.template2_out = "generated_templates/template2.html"


    def generateTemplates(self):
        self.__generateTemplate1(self.html,self.template1_out)
        self.__generateTemplate2(self.html,self.template2_out)


    def __generateTemplate1(self,html,template1_out):
        with open(html,"r") as html:
            soup = BeautifulSoup(html.read())
            images = soup.findAll("img",{"class":"image"})
            count = 1
            for image in images:
                new_wrapper_tag = soup.new_tag("div")
                new_wrapper_tag["class"] = "file-input-wrapper"
                new_button_tag =  soup.new_tag("button")
                new_input_tag = soup.new_tag("input")
                new_input_tag["name"] = "image"
                new_input_tag["class"] = "btn-file-input"

                count += 1

            text_fields = soup.findAll("div",{"class":"text"})
            count = 1
            for text in text_fields:
                new_tag = soup.new_tag("textarea")
                new_tag["name"] = "text"

                text.insert(0,new_tag)
                count += 1

            with open(template1_out,"w") as template1_out:
                template1_out.write(soup.prettify().encode("utf8"))


    def __generateTemplate2(self,html,template2_out):

        with open(html,"r") as html:
            soup = BeautifulSoup(html.read())
            images = soup.findAll("img",{"class":"image"})
            count = 1
            for image in images:
                image["src"] = "{{%s%d}}"%("image",count)
                count += 1

            text_fields = soup.findAll("div",{"class":"text"})
            count = 1
            for text in text_fields:
                text.insert(0,"{{%s%d}}"%("text",count))
                count += 1
            with open(template2_out,"w") as template2_out:
                template2_out.write(soup.prettify().encode("utf8"))


# parser =Parser("template1_1.html")
# parser.generateTemplates()





