#-*- coding: utf8 -*-

import models
from django.template.loader import get_template
import  os
from django.template import  Context

class DatabaseGenerateTemplate():
    def __init__(self, email_id):
        self.dir = '/media'
        self.email_id = email_id
        self.email_obj = models.Email.objects.get(pk=email_id)

    def getEmailParameters(self):
        """ Получнение адресов для рассылки"""
        email_obj = self.email_obj
        emails_list = email_obj.users.values('company_email')
        emails = [ d['company_email'] for d in emails_list]

        subject = email_obj.subject
        from_email = email_obj.from_email
        print emails_list
        return emails, subject, from_email


    def databaseTemplate(self):
        email_id = self.email_id
        email_obj = self.email_obj


        email_param = self.valueToDict(email_obj)

        texts_dict = models.Text.objects.filter(email=email_obj).values('text')
        texts = [t['text'] for t in texts_dict]

        imgs_dict = models.Image.objects.filter(email=email_obj).values('picture')
        imgs = [ email_param['domain_name']+img['picture'] for img in imgs_dict]
        template = self.generateTemplate(email_param, texts, imgs)

        return template

    def valueToDict(self, email_obj):
        template_id = email_obj.email_template.id
        subject = email_obj.subject
        footer = email_obj.footer
        social_btn = email_obj.social_buttons

        bg_color = email_obj.bg_color
        header_color = email_obj.header_color

        from_email = email_obj.from_email

        args = {
            'email_template': template_id,
            'subject': subject,
            'footer': footer,
            'from_email': from_email,
            'domain_name': email_obj.domain_name
        }

        bg_img = email_obj.bg_img.name
        if(bg_img):
            bg_img = os.path.join(email_obj.domain_name, 'media', bg_img)
            args['bg_img'] = bg_img

        if(bg_color):
            args['bg_color'] = bg_color
        if(header_color) :
            args['header_color'] = header_color


        header_img = email_obj.header_img.name
        if(header_img):
            header_img = os.path.join(email_obj.domain_name, 'media', header_img)
            args['header_img'] = header_img

        # социальные кнопки
        if social_btn == 'on':
            social_obj = models.Social.objects.all()
            for s in social_obj:
                s.icon = '/'.join([email_obj.domain_name, 'media', s.icon.name])

            args['social_buttons'] = social_obj
        return args

    def generateTemplate(self, param, texts, imgs):
        t = models.Template.objects.all().get(id=param['email_template']).template
        template_obj = get_template(t)

# добавление текста в шаблон
        text_count = 1
        for text in texts:
            key = 'text' + str(text_count)
            param[key] = text
            text_count += 1

# Добавление путей к изображениям
        image_path = imgs
        image_count = 1
        for img in image_path:
            img_key = 'image' + str(image_count)
            param[img_key] = img
            image_count += 1

        c = Context(param)
        return template_obj.render(c)



# изменение фона в тех блоках, где необходимо выбрать между изображением и цветом
    def __backgroundStyle(self,files, color, img_name, key_color, key_image):
        args = {}
        img = files.getlist(img_name)
        if color:
            args[key_color] = color
        if img:
            image_path = self.savingImg(img, 'tmp')
            args[key_image] = image_path[0]
        return args
