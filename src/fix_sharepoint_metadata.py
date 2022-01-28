# Clean Sharepoint metadata (especially managed metadata)
# Content from Sharepoint can contain weird data like
# myfirst=345|Business

FIELDS=['myfirst','mysecond','mythird']

def get_safe_meta_data(meta_data_name):
    safe_meta = ''
    meta_data_value = document.get_meta_data_value(meta_data_name)
    if len(meta_data_value) > 0:
        safe_meta = meta_data_value
    return safe_meta
 
def cleanValues(values):
  cleaned=[]
  for value in values:
    if '#' in value:
      clean = value.split('#')[-1].split('|')[0]
      cleaned.append(clean)
    else:
      clean = value.split('|')[0]
      cleaned.append(clean)
  return cleaned

def fix_fields(field):
  values = get_safe_meta_data(field)
  if len(values)>0:
    document.add_meta_data({field:cleanValues(values)})

for field in FIELDS:
  fix_fields(field)