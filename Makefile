report:
	pdflatex --shell-escape report.tex

clean:
	rm -rf *.log *.aux *.out _minted*
