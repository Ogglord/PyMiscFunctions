##import frontendutils.fusession as session
##import frontendutils.fuzip as zip
##import frontendutils.config as cfg
import futil as f
import io ## remove this  import later
import json ## remove later

## Load config ###
appconfig = f.DevelopmentConfig
### appconfig = config.ProductionConfig ## PROD


cache = f.CacheRedis(appconfig)
s = f.Session(appconfig,"123123123",cache)

#read a single vlaue from previous request
name = s["name"]

print ("Name from previous request:{}".format(name))

# get all fields stored in session
all_date = s.getall()
print(all_date)


## zip some files...
files = [('1.txt', io.BytesIO(b'111')), ('2.txt', io.BytesIO(b'222'))]
zipfile = s.zipfiles(files)
print("Files zipped to tmp file:{}".format(zipfile))

# store link to file in session
s.set("attachments", zipfile)

#mail file
m = f.Mail()
#m.sendmail_simple("oscar.aagren@dk.ey.com","Hello World", "Hello World!")
#m.sendmail_singleattach("oscar.aagren@dk.ey.com","Hello World", "<html><b>Hello World</b></html>",zipfile)
data = '{"Name":"Oscar", "Address": "Nørregade 28A, 3th, 1165 Denmark", "Phone": {"Prefix":"+45","Number":"30782123"}}'
dataAsJson = json.loads(data)
result = m.sendmail("oscar.aagren@dk.ey.com","Hello World", "Hello World", "<html><b>Hello World</b></html>",zipfile,dataAsJson)
print(result)



# change name
s["name"] = "Oscar"





