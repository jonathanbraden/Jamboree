#!/usr/bin/env python
from glob import glob
import json
import os

template_dir = 'templates/'
slide_dir = '../Data/'
data_dir = '../Data/'
noSlide = 'templates/noslides_2020.pdf'
headSlide = 'templates/collage_2019.pdf'

intro_data = { 'name' : 'Norm Murray', 'email' : 'murray@cita.utoronto.ca', 'title' : 'Introduction to CITA', 'abstract' : 'Introduction to CITA', 'slide' : 'templates/intro2_header_2020.pdf' }

sec_data = [
    { 'title' : 'Introduction', 'slide' : 'templates/intro_header_2020.pdf', 'time' : '15:00-15:20' , 'people' : [], 'data' : [intro_data] },
    { 'title' : 'Early Universe, Cosmology, and Galaxies', 'slide' : 'templates/cosmo_header_2020.pdf', 'time' : '15:20-15:35', 'people' : [u'Alex Lagu\xeb', 'Dongwoo Chung', 'Emily Tyhurst','James Willis','Jennifer Chan','Martine Lokkken','Nathan Carlson','Pavel Motloch','Jonathan Braden','Tom Morrison','Xinyu Li'], 'data' : [] },
    { 'title' : 'Scintillometry, FRBs, and Pulsars', 'slide' : 'templates/radio_header_2020.pdf', 'time' : '15:35-15:45', 'people' : ['Dylan Jow', 'Hsiu-Hsien Lin','Jonathan Zhang','Parasar Thulasiram','Ted Mackereth'], 'data' : [] },
    { 'title' : 'Stars, Compact Objects, and Planets', 'slide' : 'templates/ga_header_2020.pdf', 'time' : '15:45-16:00', 'people' : ['Almog Yalinewich','Alysa Obertas','Eric Poisson','Janosz Dewberry','Norman Murray','Scott Tremaine','Wei Zhu','Chris Thompson','John Zanazzi'], 'data' : [] },
    { 'title' : 'Misclassified', 'slide' : noSlide, 'time' : 'unknown', 'people' : [], 'data' : [] }
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
    for i in range(len(people)):
        p_ = people.pop()
        found = False
        for s_ in sections[1:-1]:
            if p_['name'] in s_['people']:
                s_['data'].append(p_)
                found = True
        if not found:
            sections[-1]['data'].append(p_)

    if (len(sections[-1]['data']) > 0):
        print('Warning, missing presenters')
        for p in sections[-1]['data']:
            print(p['name'])

    for s_ in sections:
        s_['data'] = sorted(s_['data'], key = lambda i : i['name'])
    return

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

    # These first two lines are horrendous code style.  Fix them.
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

def create_slide_pdf(files,name="cita_jamboree_2020.pdf"):
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
            create_slide_pdf(slides,name="cita_jamboree_2020.pdf")
