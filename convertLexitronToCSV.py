#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# filename : convertLextironToCSV.py
# author : Phisan Sookkhe
# edited : 23 OCT 2016 : 11.00PM
# This program is used for read Lexitron Dictionary, telex-utf8
# and write data into CSV format
'''

from bs4 import BeautifulSoup

def getXMLElements(xml):
    # create soup object
    soup = BeautifulSoup(xml, 'html.parser')

    tsearch = ''
    tsyn = ''
    tsample = ''
    tentry = ''
    eentry = ''
    tcat = ''
    tdef = ''
    tant = ''
    tnum = ''

    lt = []

    lt.append(soup.find('id').get_text())

    if soup.find('tsearch'):
        lt.append('"'+soup.find('tsearch').get_text()+'"')

    if soup.find('tentry'):
        lt.append('"'+soup.find('tentry').get_text()+'"')

    if soup.find('eentry'):
        lt.append('"'+soup.find('eentry').get_text()+'"')

    if soup.find('tcat'):
        lt.append('"'+soup.find('tcat').get_text()+'"')

    if soup.find('tsyn'):
        lt.append('"'+soup.find('tsyn').get_text()+'"')

    if soup.find('tsample'):
        lt.append('"'+soup.find('tsample').get_text()+'"')

    if soup.find('tdef'):
        lt.append('"'+soup.find('tdef').get_text()+'"')

    if soup.find('tant'):
        lt.append('"'+soup.find('tant').get_text()+'"')

    if soup.find('tnum'):
        lt.append('"'+soup.find('tnum').get_text()+'"')


    line = ','.join(lt).encode('utf-8')
    line = line+'\n'

    return line

if __name__ == '__main__':
    fname = './dict/telex-utf8.txt'
    outfile_path = './csv/telex-utf8.csv'
    xml = ''

    # write CSV header
    header = ['id',
              'tsearch',
              'tentry',
              'eentry',
              'tcat',
              'tsyn',
              'tsample',
              'tdef',
              'tant',
              'tnum']

    header_str = ','.join(header).encode('utf-8')+'\n'
    with open(outfile_path, 'a') as outfile:
        outfile.write(header_str)

    with open(fname) as f:
        lines = f.readlines()
        for line in lines:
            if line.rstrip('\n') != '</Doc>':
                xml += line
            else:
                xml += line
                with open(outfile_path, 'a') as outfile:
                    outfile.write(getXMLElements(xml))
                xml = ''
