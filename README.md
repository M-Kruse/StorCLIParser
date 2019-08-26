#Example usage

```
[root@localhost StorCLIParser]# python3
Python 3.6.8 (default, Apr 25 2019, 21:02:35) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from StorCLIParser import StorCLIParser
>>> s = StorCLIParser()
>>> s.generate_storcli_json()
{'controllers': [{'id': '0', 'model': 'AVAGO 3108 MegaRAID', 'serial': 'FW-AGATRHEAARBWA', 'firmware': '24.21.0-0028', 'virtual_drives': [], 'pd_list': [{'enc': '252', 'slot': '3', 'vendor': 'ATA', 'serial': 'S3HRNX0J601996P', 'model': 'SAMSUNG MZ7KM480HMHQ-00005', 'capacity': '447.130 GB [0x37e436b0 Sectors]', 'firmware': 'GXM5104Q', 'smart_error': 'No'}]}]}
>>> a = s.generate_storcli_json()
>>> a['controllers']
[{'id': '0', 'model': 'AVAGO 3108 MegaRAID', 'serial': 'FW-AGATRHEAARBWA', 'firmware': '24.21.0-0028', 'virtual_drives': [], 'pd_list': [{'enc': '252', 'slot': '3', 'vendor': 'ATA', 'serial': 'S3HRNX0J601996P', 'model': 'SAMSUNG MZ7KM480HMHQ-00005', 'capacity': '447.130 GB [0x37e436b0 Sectors]', 'firmware': 'GXM5104Q', 'smart_error': 'No'}]}]
>>> a['controllers'][0]
{'id': '0', 'model': 'AVAGO 3108 MegaRAID', 'serial': 'FW-AGATRHEAARBWA', 'firmware': '24.21.0-0028', 'virtual_drives': [], 'pd_list': [{'enc': '252', 'slot': '3', 'vendor': 'ATA', 'serial': 'S3HRNX0J601996P', 'model': 'SAMSUNG MZ7KM480HMHQ-00005', 'capacity': '447.130 GB [0x37e436b0 Sectors]', 'firmware': 'GXM5104Q', 'smart_error': 'No'}]}
>>> a['controllers'][0]['model']
'AVAGO 3108 MegaRAID'
>>> a['controllers'][0]['serial']
'FW-AGATRHEAARBWA'
>>> a['controllers'][0]['pd_list']
[{'enc': '252', 'slot': '3', 'vendor': 'ATA', 'serial': 'S3HRNX0J601996P', 'model': 'SAMSUNG MZ7KM480HMHQ-00005', 'capacity': '447.130 GB [0x37e436b0 Sectors]', 'firmware': 'GXM5104Q', 'smart_error': 'No'}]
>>> a['controllers'][0]['pd_list'][0]['serial']
'S3HRNX0J601996P'
```

