#Unit decomposition script
#
#Define input metadata field:
# unit_meta = 'unit_metadata_field'
#
#Define output metadata field:
# Make sure that the unit_decomposed_field is 'Free Text Enabled'
# unit_decomposed_field = 'unit_decomposed'

# Examples:
# 120m → 120 m;120m;0.12 km;0.12km;12000 cm;12000cm;120000 mm;120000mm;0.0746 mi;0.0746mi;0.0746 mile;0.0746mile;0.0746 miles;0.0746miles;393 feet;393feet;393 ft;393ft;4724 inch;4724inch;4724 inches;4724inches
# 100g → 100 g;100g;0.1 kg;0.1kg

import re

units=[]

def UnitConversion(s_to, s_from, number, decimals):
   units.append({'from':s_from, 'to':s_to,'number':number,'decimals':decimals})


UnitConversion('hl', 'l', 1/100,0)
UnitConversion('l', 'hl', 100,0)
UnitConversion('km', 'm', 1/1000,3)
UnitConversion('cm', 'm', 100,0)
UnitConversion('mm', 'm', 1000,0)
UnitConversion('cm', 'mtr', 100,0)
UnitConversion('mm', 'mtr', 1000,0)
UnitConversion('m', 'km', 1000,0)
UnitConversion('m', 'cm', 1/100,3)
UnitConversion('m', 'mm', 1/1000,4)
UnitConversion('m', 'mi', 1609.344,0)
UnitConversion('m', 'mile', 1609.344,0)
UnitConversion('m', 'miles', 1609.344,0)
UnitConversion('m', 'feet', 0.3048,1)
UnitConversion('m', 'ft', 0.3048,1)
UnitConversion('m', 'in', 0.0254,1)
UnitConversion('m', 'inch', 0.0254,2)
UnitConversion('m', 'inches', 0.0254,2)
UnitConversion('mm', 'in', 25.4,1)
UnitConversion('mm', 'inch', 25.4,1)
UnitConversion('mm', 'inches', 25.4,1)
UnitConversion('in', 'mm', 0.0393701,1)
UnitConversion('inch', 'mm',  0.0393701,1)
UnitConversion('"', 'mm',  0.0393701,1)
UnitConversion('”', 'mm',  0.0393701,1)
UnitConversion('mm', '"', 25.4,1)
UnitConversion('mm', '"', 25.4,1)
UnitConversion('mm', '"', 25.4,1)
UnitConversion('mm', '”', 25.4,1)
UnitConversion('mm', '”', 25.4,1)
UnitConversion('mm', '”', 25.4,1)
UnitConversion( 'mi','m', 0.000621371,4)
UnitConversion( 'mile','m', 0.000621371,4)
UnitConversion( 'miles','m', 0.000621371,4)
UnitConversion( 'feet','m', 3.28084,0)
UnitConversion( 'ft','m', 3.28084,0)
UnitConversion( 'inch','m', 39.3701,0)
UnitConversion( 'inches','m', 39.3701,0)

UnitConversion( 'inch','ft', 12,0)
UnitConversion( 'inches','ft', 12,0)
UnitConversion( 'inch','feet', 12,0)
UnitConversion( 'inches','feet', 12,0)

UnitConversion( 'ft',  'inch', 0.0833333,2)
UnitConversion( 'ft','inches', 0.0833333,2)
UnitConversion( 'feet','inch', 0.0833333,2)
UnitConversion( 'feet','inches', 0.0833333,2)


UnitConversion('g', 'lbs', 453.59237,0)
UnitConversion('g', 'lb', 453.59237,0)
UnitConversion('g', 'oz', 28.34952,0)
UnitConversion('g', 'kg', 1000,0)
UnitConversion('kg', 'g', 1/1000,3)


def get_safe_meta_data(meta_data_name):
    safe_meta = ''
    meta_data_value = document.get_meta_data_value(meta_data_name)
    if len(meta_data_value) > 0:
        safe_meta = meta_data_value[-1]
    return safe_meta
 
 
def splitUnits(meta):
    regex = r'(\d[\d.,\/]*) ?(["”\w]+)'
    matches = re.finditer(regex, meta, re.MULTILINE)
    searchableKeywords = []

    for matchNum, match in enumerate(matches, start=1):
      my_value = match.group(1)
      my_units = match.group(2)
      searchableKeywords.append(my_value+' '+my_units)
      searchableKeywords.append(my_value+''+my_units)
      #print (my_value)
      #print (my_units)
      for unit in units:
        if unit['from']==my_units:
          try:
            my_new_value = float(my_value)*unit['number']
            if (unit['decimals']==0):
              my_new = int(my_new_value)
            else:
              my_new = round(my_new_value,unit['decimals'])
            searchableKeywords.append(str(my_new)+' '+unit['to'])
            searchableKeywords.append(str(my_new)+''+unit['to'])
          except:
            pass
    return ';'.join(searchableKeywords)


 
try:

    unit_meta = 'unit_metadata_field'
    unit_decomposed_field = 'unit_decomposed'
 
    unit = get_safe_meta_data(unit_meta)
    split_unit = splitUnits(unit)
    #print (split_unit)
    log('split_unit: ' + split_unit)
    document.add_meta_data({unit_decomposed_field: split_unit})
except Exception as e:
    #print (str(e))
    log(str(e))