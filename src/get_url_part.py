#Get parts of the url and put that into metadata
#For example:
#  https://www.yoururl.com/1/2/home/invest-retire/investments/asset-allocation-solutions
#Will put:
#    @mynav1: Invest Retire
#    @mynav2: Investments

import string

def getUrlPartNoTitle(field, nr, fieldtoset):
    #Clean up
    result=''
    content=field
    content=content.replace("-"," ").title()
    parts=content.split('/')
    if (len(parts)>nr and len(parts)-1!=nr):
        result = parts[nr]
        document.add_meta_data({fieldtoset:result})
        document.log(fieldtoset+' set to: '+result)
    return result
    
def getUrlPart(field, nr, fieldtoset):
    #Clean up
    result=''
    content=field
    content=content.replace("-"," ")
    parts=content.split('/')
    if (len(parts)>nr and len(parts)-1!=nr):
        result = parts[nr]
        document.add_meta_data({fieldtoset:result})
        document.log(fieldtoset+' set to: '+result)
    return result
    
URL=document.get_meta_data_value('clickableuri')[0]
document.log(URL)

getUrlPartNoTitle(URL,2,'mynav1')
getUrlPart(URL,3,'mynav2')
