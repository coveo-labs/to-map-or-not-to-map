#calculate the geohash for a given lat/lon
#input: mylat, mylon fields
#output: geohash2, geohash3, geohash4, geohash5, geohash6, geohash7, geohash8

import json

log('V1.2')
__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = { }
for i in range(len(__base32)):
    __decodemap[__base32[i]] = i
del i

def encode(latitude, longitude, precision=12):
    """
    Encode a position given in float arguments latitude, longitude to
    a geohash which will have the character count precision.
    """
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    geohash = []
    bits = [ 16, 8, 4, 2, 1 ]
    bit = 0
    ch = 0
    even = True
    while len(geohash) < precision:
        if even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= bits[bit]
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= bits[bit]
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)
        even = not even
        if bit < 4:
            bit += 1
        else:
            geohash += __base32[ch]
            bit = 0
            ch = 0
    return ''.join(geohash)

#lat = 52.3777796784077
#lon = 4.90516680992096
# Get Lat/Lon
log(document.get_meta_data_value('objecttype')[0])
if (document.get_meta_data_value('objecttype')[0]=='House'):
  try:
    lat = float(document.get_meta_data_value('mylat')[0])
  except Exception as e: 
    log('Error with lat '+str(e))
    log(json.dumps(document.get_meta_data()))
  try:
     lon = float(document.get_meta_data_value('mylon')[0].strip())
  except Exception as e: 
    log('Error with lon '+str(e))
      
  #mylat = str(lat)
  #mylon = str(lon)
  #log(mylat)
  #log(mylon)
  # Calculate Hashes
  try:
     hash2 = encode(lat, lon, precision=2)
  except Exception as e: 
    log('Error with hash2 '+str(e))
    
  try:
     hash3 = encode(lat, lon, precision=3)
  except:
    log('Error with hash3')
    
  try:
     hash4 = encode(lat, lon, precision=4)
  except:
    log('Error with hash4')

  try:
     hash5 = encode(lat, lon, precision=5)
  except:
    log('Error with hash5')

  try:
     hash6 = encode(lat, lon, precision=6)
  except:
    log('Error with hash6')
  
  try:
  	hash7 = encode(lat, lon, precision=7)
  except:
    log('Error with hash7')

  try:
  	hash8 = encode(lat, lon, precision=8)
  except:
    log('Error with hash8')

  # Add Meta
  document.add_meta_data({'geohash2':hash2})
  document.add_meta_data({'geohash3':hash3})
  document.add_meta_data({'geohash4':hash4})
  document.add_meta_data({'geohash5':hash5})
  document.add_meta_data({'geohash6':hash6})
  document.add_meta_data({'geohash7':hash7})
  document.add_meta_data({'geohash8':hash8})