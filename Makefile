keamanan.pdf:	*.tex
	pdflatex python.tex

bib:
	bibtex python

ALL:
	pdflatex python.tex
	pdflatex python.tex

