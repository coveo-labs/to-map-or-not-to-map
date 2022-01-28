#Fix Colors
# based on a color name assign a familiy color name

def get_safe_meta_data(meta_data_name):
    safe_meta = ''
    meta_data_value = document.get_meta_data_value(meta_data_name)
    if len(meta_data_value) > 0:
        safe_meta = meta_data_value[-1]
    return safe_meta
 

def fixMeta(all, column):
  for val in all:
    if (val==column):
      return all[val]
  return ''

def fixColor(colorCode):
  colorCode=colorCode.split('(')[0].strip()

  colors =[]
  colors.append({'c':'gelb','f':'gelb'})
  colors.append({'c':'orange','f':'orange'})
  colors.append({'c':'pink','f':'pink'})
  colors.append({'c':'rotlila','f':'pink'})
  colors.append({'c':'lila','f':'pink'})
  colors.append({'c':'violett','f':'pink'})
  colors.append({'c':'verkehrspurpur','f':'pink'})
  colors.append({'c':'telemagenta','f':'pink'})
  colors.append({'c':'perlbrombeer','f':'pink'})
  colors.append({'c':'rot','f':'rot'})
  colors.append({'c':'rosa','f':'rot'})
  colors.append({'c':'rosé','f':'rot'})
  colors.append({'c':'blau','f':'blau'})
  colors.append({'c':'perlenzian','f':'blau'})
  colors.append({'c':'grün','f':'grün'})
  colors.append({'c':'oliv','f':'grün'})
  colors.append({'c':'türkis','f':'grün'})
  colors.append({'c':'grau','f':'grau'})
  colors.append({'c':'verkehrsgrau A','f':'grau'})
  colors.append({'c':'verkehrsgrau B','f':'grau'})
  colors.append({'c':'telegrau 1','f':'grau'})
  colors.append({'c':'telegrau 2','f':'grau'})
  colors.append({'c':'telegrau 4','f':'grau'})
  colors.append({'c':'graualuminium','f':'grau'})
  colors.append({'c':'grauweiß','f':'grau'})
  colors.append({'c':'braun','f':'braun'})
  colors.append({'c':'perlkupfer','f':'braun'})
  colors.append({'c':'schwarz','f':'schwarz'})
  colors.append({'c':'weiß','f':'weiß'})
  colors.append({'c':'weißaluminium','f':'weiß'})
  colors.append({'c':'anthrazit','f':'anthrazit'})

  for color in colors:
    if (colorCode.endswith(color['c']) ):
      #print ('Found Family:'+color['f'])
      return color['f'].title()

  return colorCode.title()

colorfamily=''
try:
    color = get_safe_meta_data('sfspec__color_value')
    log('Current color: '+color)
    colorfamily = fixColor(color)
    log('Color Family: '+colorfamily)
    document.add_meta_data({'color_family': colorfamily})
  
except Exception as e:
    log(str(e))
  
