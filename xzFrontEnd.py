import os
import wx

print "Which file do you want to un-xz?"
fileName = raw_input()
os.system("xz -d " + fileName)
print "whats up?"

