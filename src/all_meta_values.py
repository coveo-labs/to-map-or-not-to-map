# Will put all metadata values inside a field
# Output: allmetadatavalues

import json
document.add_meta_data({"allmetadatavalues": json.dumps(document.get_meta_data())})