.PHONY: all

all:
	mkdir -p output/pdf
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=output/pdf main.tex
