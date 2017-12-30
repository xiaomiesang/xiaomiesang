##import re
##text = "Hi,i am shirly Hilton. i am his wfe."
##m = re.findall(r"hi",text)
##if m:
##    print (m)
##else:
##    print ("not match")



##import re
##text = "Hi,i am shirly Hilton. i am his wfe."
##m = re.findall(r"[Hh]i",text)
##if m:
##    print (m)
##else:
##    print ("not match")


##import re
##text = "Hi,i am shirly Hilton. i am his wfe."
##m = re.findall(r"\S",text)
##if m:
##    print (m)
##else:
##    print ("not match")


import re
text = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*?e\b",text)
if m:
    print (m)
else:
    print ("not match")
