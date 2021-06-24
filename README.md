Cutout Syntax: 
> python3 get_cutout.py -c [cutout file] -d [output directory] -l [catalog layer] -s [pixel scale] -t [file type]

Defaults: 
    cutout file = 'cutouts.txt'
    output directory = 'cutouts'
    catalog layer = 'ls-dr9' (DECALS DR9)
    pixel scale = 0.262 (native)
    file type = 'fits' (the alternative is 'jpeg')
    
Catalog Syntax: 
> python3 get_catalog.py -c [cutout file] -d [output directory] -l [catalog layer]

Defaults: 
    cutout file = 'cutouts.txt'
    output directory = 'catalogs'
    catalog layer = 'ls-dr9' (DECALS DR9)
