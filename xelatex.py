import os

# 编译
os.system("xelatex -f zjuthesis.tex")
os.system("biber zjuthesis")
os.system("xelatex -f zjuthesis.tex")
os.system("xelatex -f zjuthesis.tex")