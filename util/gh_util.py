# -*- coding: utf-8 -*-
import re
import subprocess

'''
Problem  - Problem
Issue - #Number
'''
def createpy(min_row, max_row, nstart):
  '''
  min_row: inclusive of starting problem.
  max_row: last problem + 1.
  nstart : GH problem number to start.
  '''
  with open('util/pe.csv','r') as csv:
    for line in csv.readlines()[min_row:max_row]:
      items = line.split(",")
      id = items[0]
      title =  items[1].replace('"',"")
      ltitle = re.sub(r'[\"|\-|:]',"", items[1]).lower()
      fname = re.sub(r'\s', "_", ltitle)
      name = str.format("0{0}_{1}.py", id, fname)
      print(id, title, name)
      with open(name,'w') as pyfile:
        pyfile.write("# -*- coding: utf-8 -*-\n")
        pyfile.write("\n")
        pyfile.write("'''\n")
        pyfile.write(str.format("Problem - {0}\n", title))
        pyfile.write(str.format("Issue - #{0}\n", nstart))
        pyfile.write("'''\n")
      nstart += 1

def creategh(min_row, max_row):
  '''
  min_row: inclusive of starting problem.
  max_row: last problem + 1.
  '''
  with open('util/pe.csv','r') as csv:
    for line in csv.readlines()[min_row:max_row]:
      items = line.split(",")
      id = items[0]
      title =  items[1].replace('"',"")
      print(id)
      print(title)
      body = str.format('https://projecteuler.net/problem={0}', id)
      cmd = ['gh', 'issue', 'create', '-a', '@me', '-l', 'New Feature', '-m', 'Milestone3', '-t', title, '-b', body]
      out = subprocess.check_output(cmd, universal_newlines=True)
      print(out)

if __name__ == "__main__":
  createpy(55, 101, 59)