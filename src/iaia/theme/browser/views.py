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

        api.portal.send_email(
            recipient="henry@mingtak.com.tw",
            sender=email,
            subject="Trappist",
            body=message,
        )
        return  

        