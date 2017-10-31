from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class IaiaMacro(BrowserView):
    """ """



class Send_mail(BrowserView):
    template = ViewPageTemplateFile('template/send_mail.pt')

    def __call__(self):
        email=self.request.form['email']
        message=self.request.form['message']
        user_default = 'iaia.content.browser.UserDefault.IUserDefault'
        recipe_email= api.portal.get_registry_record('%s.email' % user_default)

        api.portal.send_email(
            recipient=str(recipe_email),
            sender=email,
            subject="Some Trouble",
            body=message,
        )
        return  
        