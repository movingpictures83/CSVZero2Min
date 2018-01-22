import sys
import numpy
import random

# Scaling is done to make median=1
class CSVZero2MinPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')

      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')

      self.n = len(self.bacteria)
      self.ADJ = []#numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1].strip())
               self.ADJ[i].append(value)#[j] = value
            i += 1


  
   def output(self, filename):
      for i in range(self.m):
         minimumA = 100000
         for j in range(self.n):
            if (self.ADJ[i][j] != 0 and self.ADJ[i][j] < minimumA):
               minimumA = self.ADJ[i][j]
         for j in range(self.n):
            if (self.ADJ[i][j] == 0):
               self.ADJ[i][j] = minimumA

      filestuff2 = open(filename, 'w')
      filestuff2.write(self.firstline)
      
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



