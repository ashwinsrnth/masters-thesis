view: paper.pdf
	evince paper.pdf

paper.pdf: paper.tex
	pdflatex paper.tex
	bibtex paper.aux
	pdflatex paper.tex
	pdflatex paper.tex

clean:
	rm -rf *.pdf *.log *.aux *.out _minted* *.blg *.bbl
