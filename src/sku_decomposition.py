#SKU decomposition script
#
#Define input metadata field:
# sku_meta = 'unit_metadata_field'
#
#Define output metadata field:
# Make sure that the unit_decomposed_field is 'Free Text Enabled'
# unit_decomposed_field = 'unit_decomposed'

# Examples:
# ML 5000 E P → ML5000 E P, ML5000E P, ML5000EP

def get_safe_meta_data(meta_data_name):
    safe_meta = ''
    meta_data_value = document.get_meta_data_value(meta_data_name)
    if len(meta_data_value) > 0:
        safe_meta = meta_data_value[-1]
    return safe_meta
 
 
def splitSKU(meta):
    keywords = meta.split()
    searchableKeywords = []
    for keyword in keywords:
        print(keyword)
        letters = list(keyword)
        searchableKeyword = []
        previousChar = ""
        for letter in letters:
            previousChar += letter
            # starting at 3 characters
            if (len(previousChar) > 1):
                searchableKeyword.append(previousChar)
        searchableKeywords += searchableKeyword
    return ';'.join(searchableKeywords)

def splitSpace(prod):
  parts=prod.split(' ')
  newparts = ''
  for nr in range(1,len(parts)):
     newparts+=prod.replace(' ','',nr)+';'
  return newparts
 
 
try:
 
    sku_meta = 'masterproductname'
    sku_meta_decomposed = 'masterproductname_decomposed'
 
    sku = get_safe_meta_data(sku_meta)
    splitSpace = splitSpace(sku)
    split_sku = splitSKU(sku)+';'+splitSpace
    log('split_sku: ' + split_sku)
    document.add_meta_data({sku_meta_decomposed: split_sku})
except Exception as e:
    log(str(e))