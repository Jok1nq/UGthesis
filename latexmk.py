import os
os.system('xelatex -f zjuthesis.tex')
os.system('latexmk -c')
