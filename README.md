Note: this code is an older version. If you're trying to download a catalog, use my [catalog downloader tool](https://github.com/bclevine/DECaLS_catalog_downloader/tree/f438973ebe4cd5c5995edf98ba20b740f5d71366) instead. 

Cutout Syntax: 
> python3 get_cutout.py -c [cutout file] -d [output directory] -l [catalog layer] -s [pixel scale] -t [file type]

Defaults: 
- cutout file = 'cutouts.txt'
- output directory = 'cutouts'
- catalog layer = 'ls-dr9' (DECALS DR9)
- pixel scale = 0.262 (native)
- file type = 'fits' (the alternative is 'jpeg')
    
Catalog Syntax: 
> python3 get_catalog.py -c [cutout file] -d [output directory] -l [catalog layer] -m [multithreaded?]

Defaults: 
- cutout file = 'cutouts.txt'
- output directory = 'catalogs'
- catalog layer = 'ls-dr9' (DECALS DR9)
- multithreaded = False
