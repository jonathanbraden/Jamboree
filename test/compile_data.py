#!/usr/bin/env python
from glob import glob
import json
import os

template_dir = 'templates/'
slide_dir = '../Data/'
data_dir = 'Data/'

sec_data = [
    { 'title' : 'Introduction',    'people' : [], 'time' : '15:00-15:20' },
    { 'title' : 'Early Universe, Cosmology, and Galaxies', 'time' : '15:20-15:35', 'people' : [u'Alex Lagu\xeb', 'Dongwoo Chung', 'Emily Tyhurst','James Willis','Jennifer Chan','Martine Lokken','Nathan Carlson','Pavel Motloch','Jonathan Braden'] },
    { 'title' : 'Scintillometry, FRBs, and Pulsars', 'time' : '15:35-15:45', 'people' : ['Dylan Jow', 'Hsiu-Hsien Lin','Jonathan Zhang','Parasar Thulasiram','Ted Mackereth'] },
    { 'title' : 'Stars, Compact Objects, and Planets', 'time' : '15:45-16:00', 'people' : ['Almog Yalinewich','Alysa Obertas','Eric Poisson','Janosz Dewberry','Norman Murray','Scott Tremaine','Wei Zhu','Chris Thompson','J. J. Zanazzi'] },
    { 'title' : 'Misclassified', 'time' : 'unknown' }
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
    sec_list = [ [] for i in range(len(sections)) ]
    for i in range(len(people)):
        p_ = people.pop()
        if p_['name'] in sections[1]['people']:
            sec_list[1].append(p_)
        elif p_['name'] in sections[2]['people']:
            sec_list[2].append(p_)
        elif p_['name'] in sections[3]['people']:
            sec_list[3].append(p_)
        else:
            sec_list[4].append(p_)

    if (len(sec_list[-1]) > 0):
        print('Warning, missing presenters')
        for p in sec_list[-1]:
            print(p['name'])
    return sec_list

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

def create_program(people,sections=sec_data):
    """
    Write a LaTeX file with the program metadata.
    Stored in program.tex.

    Note: Any existing program.tex file is overwritten
    """
    # Start by grouping people into sections
    sec_list = group_people(people,sections)

    # These first two lines are horrendous code style.  Fix them.
    os.system('cat {}program_header.tex > program.tex'.format(template_dir))
    prog = open('program.tex','a')
    slides = [] # This will store the ordered list of slides
    for i,s_ in enumerate(sec_list):
        _make_section(prog,s_,sections[i]['title'],sections[i]['time'])
    prog.write('\\end{document}\n')
    prog.close()

    #os.system('pdflatex progam')
    #os.system('rm -f program.log program.aux')
    return

def _make_section(prog,sec_people,title,time):
    """
    Input
      prog - The program tex file we're writing
    """
    prog.write('\\textbf{\\LARGE %s - %s}' % (title,time))
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

def create_slides(files):
    """
    Creates a compiled pdf of slides
    """
    return

if __name__=="__main__":
    people = read_presenter_data('Data/')
    create_program(people)
    pass
