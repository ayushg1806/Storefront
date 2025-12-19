from django.core.cache import cache
from django.core.mail import send_mail, mail_admins, EmailMessage
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
import logging
import requests

# @cache_page(5 * 60)
# def say_hello(request):
#     # try:
#     #     # send_mail('subject', 'message', 'info@ayush.com', ['gautam@ayush.com'])
#     #     # mail_admins('subject', 'message', html_message='message')
#     #     # message = EmailMessage('subject', 'message', 'info@ayush.com', ['gautam@ayush.com'])
#     #     # message.attach_file('playground/static/images/demo.png')
#     #     # message.send()
#     #     message = BaseEmailMessage(
#     #         template_name='emails/hello.html',
#     #         context={'name': 'Ayush'}
#     #     )
#     #     message.send(['gautam@ayush.com'])
#     # except BadHeaderError:
#     #     pass
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})

logger = logging.getLogger(__name__) #playground.views

class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('Httpbin is offline')
        return render(request, 'hello.html', {'name': 'Ayush'})