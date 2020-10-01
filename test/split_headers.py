import os

full_headers = 'all_headers_2020.pdf'
name=['intro_header','intro2_header','cosmo_header','radio_header','ga_header','noslides']
suffix = '_2020.pdf'

for i in range(6):
    command = 'gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dFirstPage={} -dLastPage={} -sOUTPUTFILE={} {}'.format(i+1,i+1,name[i]+suffix,full_headers)
    os.system(command)
