view: paper.pdf
	evince paper.pdf

paper.pdf: paper.tex img/*.eps fig/*.eps references.bib table/*.tex
	pdflatex -shell-escape paper.tex
	bibtex paper.aux
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex
	make clean
clean:
	rm -rf *.log *.aux *.out _minted* *.blg *.bbl *.spl
