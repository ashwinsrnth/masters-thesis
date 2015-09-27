report:
	pdflatex --shell-escape report.tex
	bibtex report.aux
	pdflatex --shell-escape report.tex
	pdflatex --shell-escape report.tex
	evince report.pdf

clean:
	rm -rf *.pdf *.log *.aux *.out _minted* *.blg *.bbl
