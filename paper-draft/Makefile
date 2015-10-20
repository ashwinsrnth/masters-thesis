view: paper.pdf
	evince paper.pdf

paper.pdf: paper.tex img/*.eps references.bib
	pdflatex paper.tex
	bibtex paper.aux
	pdflatex paper.tex
	pdflatex paper.tex
	make clean
clean:
	rm -rf *.log *.aux *.out _minted* *.blg *.bbl *.spl
