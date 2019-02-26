from requests import post
from json2html import json2html
from io import BytesIO
from json import dumps

class Mail(): 

    def sendmail(self, to, subject, text, html, attachmentpath, dataAsJson):
        with BytesIO() as fp:
        #json.dump(dataAsJson,fp, indent=3, sort_keys=True)
            
            fp.write(dumps(dataAsJson,indent=3,sort_keys=False, ensure_ascii=False).encode('utf8')) 
        
            dataAsHtml = json2html.convert(json = dataAsJson)
            body = "<html><h2>Claim Data</h2><br/><br/>{}</html>".format(dataAsHtml)
            print(body)

            return post(
                "https://api.mailgun.net/v3/sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org/messages",
                auth=("api", "4265b502b1f2ee3ddcea73e8bae9c555-b9c15f4c-4d9f8672"),
                files=[("attachment", ("attachment.zip",open(attachmentpath),"application/octet-stream")),
                    ("attachment",("data.txt", fp.getvalue(), "text/plain"))],
                data={"from": "Python <noreply@sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org>",
                "to": [to],
                "subject": subject,
                "text":text,
                "html": body})   

    def sendmail_simple(self, to, subject, text):
          return post(
            "https://api.mailgun.net/v3/sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org/messages",
            auth=("api", "4265b502b1f2ee3ddcea73e8bae9c555-b9c15f4c-4d9f8672"),
            data={"from": "Python <noreply@sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org>",
            "to": [to],
            "subject": subject,
            "text": text})    

    def sendmail_singleattach(self, to, subject, html, attachmentpath):
          return post(
            "https://api.mailgun.net/v3/sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org/messages",
            auth=("api", "4265b502b1f2ee3ddcea73e8bae9c555-b9c15f4c-4d9f8672"),
            files=[("attachment", open(attachmentpath))],
            data={"from": "Python <noreply@sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org>",
            "to": [to],
            "subject": subject,
            "html": html},
            headers={'Content-type': 'multipart/form-data;'})              

    def send_test_message(self):
        
        return post(
            "https://api.mailgun.net/v3/sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org/messages",
            auth=("api", "4265b502b1f2ee3ddcea73e8bae9c555-b9c15f4c-4d9f8672"),
            data={"from": "Python <noreply@sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org>",
            "to": ["oscar.aagren@dk.ey.com", "noreply@sandbox75b0b73afea34ac59f5ba0bfd522b75a.mailgun.org"],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!"})    

