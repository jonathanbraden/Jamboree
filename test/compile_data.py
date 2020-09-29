#!/usr/bin/env python
from glob import glob
import json
import os

template_dir = 'templates/'

sections = [
    { 'title' : 'Introduction',    'people' : [] },
    { 'title' : 'Radio Astronomy', 'people' : ['Ue-Li Pen' ] },
    { 'title' : 'Cosmology',       'people' : ['Dick Bond', 'Jonathan Braden', 'Thomas Morrison', 'Pavel Motloch', 'Alex Lagu\u00eb', 'Nathan Carlson', 'Martine Lokken'] },
    { 'title' : 'General Astro',   'people' : [] },
    { 'title' : 'Other',           'people' : [] }
    ]

def read_presenter_data(dir='Data'):
    """
    Read the presenter data (stored as a bunch of individual JSON files),
    and return a list

    Input:
      dir - Directory storing the JSON files
    Output:
      people - A list of dictionaries.  Each dictionary contains the JSON info for a single person
    """
    files = glob(dir+'/*.json')
    people = []
    for fc in files:
        with open(fc) as f:
            people.append(json.load(f))
    # Add in sorting into groups here
    return people

def group_people(people):
    # 1. Start by popping off current person
    # 2. See if they are in each section
    # 3. 
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

def create_program(people):
    """
    Write a LaTeX file with the program metadata.
    Stored in program.tex.

    Note: Any existing program.tex file is overwritten
    """

    # These first two lines are horrendous code style.  Fix them.
    os.system('cat {}program_header.tex > program.tex'.format(template_dir))
    prog = open('program.tex','a')
    slides = [] # This will store the ordered list of slides
    _make_section(prog,people)
    prog.write('\\end{document}\n')
    prog.close()

    #os.system('pdflatex progam')
    #os.system('rm -f program.log program.aux')
    return

def _make_section(prog,sec_people):
    """
    Input
      prog - The program tex file we're writing
    """
    prog.write('\\textbf{\\huge Temporary Heading}')
    prog.write('\\newline\n')
    prog.write('\\begin{center}\n')
    for p in sec_people:
        _write_program_entry(prog,p)
    prog.write('\\end{center}\n\n')
    return

def _write_program_entry(prog,info):
    """
    Input:
      prog - The program tex file we're writing
      info - JSON info for the person we're including  
    """
    prog.write('\\begin{tabular}{|m{5cm}|m{10cm}|}\n')
    prog.write('\\hline\n')
    tmpStr = '{\\bf '+info['name']+' } \\newline ' \
             +info['email'] \
             +' & {\\bf '+info['title']+' } \\newline ' \
             +info['abstract']+' \\\\ \n'
    prog.write(tmpStr.encode("utf8"))
    prog.write('\\hline\n')
    prog.write('\\end{tabular}\n')
    return

def create_slides():
    return

if __name__=="__main__":
    people = read_presenter_data()
    create_program(people)
    pass
