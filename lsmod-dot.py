# -*- coding: utf-8 -*-
"""
based on python2.7 and Graphviz
"""
import os
os.system("lsmod >>/dev/shm/lsmod.txt")
OP = open ("/dev/shm/mod.dot", "w")
OP.write("digraph g {"+"\n")

with open ("/dev/shm/lsmod.txt","r") as gm:
    for line in gm:
        tube=str.split(line)
        if len(tube)> 3:
            tube3=str.split(tube[3],",")
            for mod in tube3:
                print tube[0]+"->"+mod+";"+"\n",
                OP.write(tube[0]+"->"+mod+";"+"\n")
        else:
            #pass
            OP.write(tube[0]+";"+"\n")
OP.write("}")             
OP.close()
os.system("dot -Tpng  /dev/shm/mod.dot -o /dev/shm/mod_out.png")
