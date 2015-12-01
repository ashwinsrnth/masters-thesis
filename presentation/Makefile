doc:
	pdflatex -shell-escape presentation.tex
	pdflatex -shell-escape presentation.tex
	evince presentation.pdf&
backup:
	pdflatex -shell-escape backups.tex
	pdflatex -shell-escape backups.tex
	evince backups.pdf
clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.nav
	rm -f *.snm
	rm -f *.toc
	rm -f *.out
	rm -f *.bcf
	rm -f *.blg
	rm -f *.run.xml
	rm -f *.vrb
	rm -f *.bbl
	rm -f *blx.bib
	
