#!/usr/bin/env python
from glob import glob
import json
import os

template_dir = 'templates/'
slide_dir = '../Data_mv/'
data_dir = '../Data/'
noSlide = 'templates/noslides_2021.pdf'
headSlide = 'templates/collage_2021.pdf'

intro_data = { 'name' : 'Juna Kollmeier', 'email' : 'jak@cita.utoronto.ca', 'title' : 'Introduction to CITA', 'abstract' : 'Introduction to CITA', 'slide' : 'templates/intro2_header_2021.pdf' }

cosmo_1 = { 'title' : 'Cosmology and Extragalactic I', 
            'slide' : 'templates/cosmo_header_2021.pdf', 
            'time'  : 'Thursday : 12:15 - 13:00', 
            'people' : ['Jose Tomas Galvez Ghersi',
                        'Lukas Hergt',
                        'Dick Bond',
                        'Thomas Morrison',
                        'Zack Li',
                        'Nathan Carlson',
                        'Matthew Johnson',
                        'Pavel Motloch',
                        'James Taylor',
                        'Adrian Liu'],
            'data' : []
}

cosmo_2 = { 'title' : 'Cosmology and Extragalactic II',
            'slide' : 'templates/cosmo_header_2021.pdf',
            'time'  : 'Friday : 15:20 - 16:20',
            'people': ['Jennifer Y. H. Chan',
                       'Dongwoo Chung',
                       'Jonathan Braden',
                       'Alex Lague',
                       'Hongming Zhu',
                       'Martine Lokken',
                       'Jibran Haider',
                       'Levon Pogosian'],
            'data'  : []
}

gal_1 = { 'title'  : 'Galaxies I',
          'slide'  : 'templates/galaxy_header_2021.pdf',
          'time'   : 'Thursday : 15:20-16:20',
          'people' : ['Marta Reina-Campos',
                      'Seunghwan Lim',
                      'Rainer Weinberger',
                      'Denis Leahy',
                      'Neige Frankel',
                      'Lichen Liang'],
          'data' : []
}

gal_2 = { 'title'  : 'Galaxies II',
          'slide'  : 'templates/cosmo_header_2021.pdf',
          'time'   : 'Friday : 14:20 - 15:20',
          'people' : ['Aris Tritsis',
                      'Antoine Marchal',
                      'James McKee',
                      'Ted Mackereth',
                      'Peter Martin',
                      'Jiayi Sun'],
          'data' : []
}

planets = { 'title'  : 'Planets',
            'slide'  : 'templates/cosmo_header_2020.pdf',
            'time'   : 'Thursday : 13:00-14:00',
            'people' : ['Eve Lee',
                'Sam Hadden',
                        'Scott Tremaine',
                        'Fergus Horrobin',
                        'J. J. Zanazzi',
                        'Brett Gladman'],
            'data'   : []
}

he_1  = { 'title'  : 'High Energy / FRB I',
          'slide'  : 'templates/frb_header_2021.pdf',
          'time'   : 'Thursday : 14:20 - 15:20',
          'people' : ['Xinyu Li',
                      'Jonathan Zhang',
                      'Ashley Stock',
                      'Fang Xi Lin',
                      'Chris Thompson'],
          'data'   : []
}

he_2 = { 'title'   : 'High Energy / FRB II',
         'slide'   : 'templates/frb_header_2021.pdf',
         'time'    : 'TBD',
         'people'  : ['Dylan Jow',
                      'Almog Yalinewich',
                      'Daniel Baker', 
                      'Simon Blouin',
                      'Jing Santiago Luo',
                      'Evan McDonough'],
         'data'    : []
}

mm =  { 'title'    : 'Multimessenger and "Multitopic"',
        'slide'    : 'templates/multi_header_2021.pdf',
        'time'     : 'Friday : 12:00 - 1:00',
        'people'   : ['Sarah Gossan',
                      'Phil Landry',
                      'Jose Miguel Jauregui',
                      'Janosz Dewberry',
                      'Omar Contigiani'],
        'data'     : []
}

intro_data = { 'title'  : 'Introduction',
               'slide'  : 'templates/intro_header_2020.pdf',
               'time'   : 'Thursday : 12:00 - 12:15',
               'people' : [],
               'data'   : [intro_data]
}

sec_data = [intro_data,
    cosmo_1, planets, he_1, gal_1, 
    mm, he_2, gal_2, cosmo_2,
    { 'title' : 'Unclassified', 'slide' : noSlide, 'time' : 'unknown', 'people' : [], 'data' : [] }
]
sec_data_thur = [intro_data,
    cosmo_1, planets, he_1, gal_1, 
    { 'title' : 'Unclassified', 'slide' : noSlide, 'time' : 'unknown', 'people' : [], 'data' : [] }
]

sec_data_fri = [
    mm, he_2, gal_2, cosmo_2,
    { 'title' : 'Unclassified', 'slide' : noSlide, 'time' : 'unknown', 'people' : [], 'data' : [] }
]


def read_presenter_data(dir):
    """
    Read the presenter data (stored as a bunch of individual JSON files),
    and return a list

    Input:
      dir - Directory storing the JSON files
    Output:
      people - A list of dictionaries.  Each dictionary contains the JSON info for a single person
    """
    files = glob(dir+'*.json')
    people = []
    for fc in files:
        with open(fc) as f:
            people.append(json.load(f))
    return people

def group_people(people,sections):
    """
    Given a collection of people and sections specifying a set of people,
    place the people in the correct sections.
    """
    for i in range(len(people)):
        p_ = people.pop()
        found = False
        for s_ in sections[1:-1]:
            if p_['name'] in s_['people']:
                p_['order'] = s_['people'].index(p_['name'])
                s_['data'].append(p_)
                found = True
        if not found:
            sections[-1]['data'].append(p_)

    if (len(sections[-1]['data']) > 0):
        print('Warning, missing presenters')
        for p in sections[-1]['data']:
            print(p['name'])

    for s_ in sections[1:-1]:
        if len(s_['people']) != len(s_['data']):
            _add_missing_submissions(s_)
        s_['data'] = sorted(s_['data'], key = lambda i : i['order'])
    return

def _add_missing_submissions(sec):
    found_names = [ d_['name'] for d_ in sec['data'] ]
    for i_,name in enumerate(sec['people']):
        if name not in found_names:
            p_ = _make_null_submission(name)
            p_['order'] = i_
            sec['data'].append(p_)
    return

def _make_null_submission(name):
    p_ = { 'name' : name, 'type' : 'no', 'abstract' : 'TBA', 'title' : 'TBA', 'email' : '', 'slide' : noSlide }
    return p_

def compute_times(start,talk_len):
    """
    Input
      start - Start time (in ????)
      talk_len - Time assigned to each talk (in minutes)
    """
    tc = start
    for s_ in sections:
        s_['tstart'] = convert_time_to_string(tc)
        tc += 0  # Do this properly
    return

def convert_time_to_string(min):
    """
    Input is number of minutes since start.
    Outputs a string with the start.
    """
    return '{:d}:{:02d}'.format(min//60,min%60) 

def create_program(people,sections):
    """
    Write a LaTeX file with the program metadata.
    Stored in program.tex.

    Note: Any existing program.tex file is overwritten
    """
    slides = [] # Add the CITA jamboree slide here
    group_people(people,sections)

    os.system('cat {}program_header.tex > program.tex'.format(template_dir))
    prog = open('program.tex','a')
    slides = [] # This will store the ordered list of slides
    for i,s_ in enumerate(sections):
        new_slides = _make_section(prog,s_)
        slides = slides + new_slides
    prog.write('\\end{document}\n')
    prog.close()

    #os.system('pdflatex program.tex')
    #os.system('rm -f program.log program.aux')
    return slides

def _make_section(prog,sec):
    """
    Input
      prog - The program tex file we're writing
      sec  - Dictionary with section data
    """
    if ((len(sec['data']) == 0) & (sec['title'] != 'Introduction')):
        return []

    prog.write('\\textbf{\\LARGE %s - %s}' % (sec['title'],sec['time']))
    prog.write('\\newline\n')
    prog.write('\\begin{center}\n')
    slides=[sec['slide']]
    for p in sec['data']:
        _write_program_entry(prog,p)
        slides.append(p['slide'])
    prog.write('\\end{center}\n\n')
    return slides

def _write_program_entry(prog,info):
    """
    Input:
      prog - The program tex file we're writing
      info - JSON info for the person we're including  
    """
    prog.write('\\begin{tabular}{|m{5.5cm}|m{10.5cm}|}\n')
    prog.write('\\hline\n')
    tmpStr = '{\\bf '+info['name']+' } \\newline ' \
             +info['email'] \
             +' & {\\bf '+info['title']+' } \\newline ' \
             +info['abstract']+' \\\\ \n'
    prog.write(tmpStr.encode("utf8"))
    prog.write('\\hline\n')
    prog.write('\\end{tabular}\n')
    return

def create_slide_pdf(files,name="cita_jamboree_2021.pdf"):
    """
    Creates a compiled pdf of slides from a list.
    Includes a test to make sure the slide exists.
    """
    os.system('cp '+headSlide+' '+name)
    for f_ in files:
        try:
            with open(f_):
                fCur = f_.encode("utf8")
                print(fCur)
        except IOError:
            print("Warning, no slide for "+f_.encode("utf8"))
            fCur = noSlide
        command = "gs -q -dNOPAUSE -dBATCH -dCompressFonts=true -sDEVICE=pdfwrite -dPDFSETTING=/prepress -sOutputFile=temp.pdf "+name+" "+fCur
        os.system(command)
        os.system("mv temp.pdf "+name)
    return

import sys
if __name__=="__main__":
    people = read_presenter_data(data_dir)
    slides = create_program(people,sec_data)
    if (len(sys.argv) > 1):
        if sys.argv[1] in ["True" , "true" , "T" , "t"]:
            create_slide_pdf(slides,name="cita_jamboree_2021.pdf")
