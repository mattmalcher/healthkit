""" 
Call convert_xml_to_sqlite from a script where I can easily jump in via the debugger

Tried to configure vscode to jump into module code with "justMyCode": false but couldnt get this to work.

Instead just copied the utils file from the module and put it next to this script...
"""

import sqlite_utils
import zipfile
#from healthkit_to_sqlite import utils
import utils

zf = zipfile.ZipFile("export.zip")

db = sqlite_utils.Database("healthkit.db")

export_xml_path = 'apple_health_export/export.xml'

fp = zf.open(export_xml_path)

file_length = zf.getinfo(export_xml_path).file_size

utils.convert_xml_to_sqlite(fp, db, progress_callback=None, zipfile=zf)

