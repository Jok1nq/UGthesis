import os

# 编译
os.system("xelatex -f zjuthesis.tex")
os.system("latexmk -c")
os.system("move .\\zjuthesis.pdf  ..\\ ")