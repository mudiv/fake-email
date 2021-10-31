import requests,time
from .ruks import EMAIL, MESSAGE_A, MESSAGE_C
class Email(object):
    def __init__(self):
        self.session = requests.session()
        self.mes_count = 0
        self.messages = []
        self.email = self.session.get(EMAIL).json()['address']

    def new_email(self):        
        return self.email

    def call_up_message(self):

        return self.messages
       
    def new_message(self):
        return self.session.get(MESSAGE_C).json()['messageCount'] != self.mes_count
        		
    def get_message(self):
        res = self.session.get(MESSAGE_A + str(self.mes_count)).json()
        self.mes_count += len(res)        
        self.messages += res        
        return self.messages
    def __str__(self):
        return self.email


if __name__ == "__main__":
    mail = Email()
    print(mail.new_email())    
    while True:
        time.sleep(2)
        