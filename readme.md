```
sudo add-apt-repository universe
sudo apt update
sudo apt install texlive-luatex texlive-latex-extra
```

```
docker run --rm -v "$PWD:/work" -w /work texlive/texlive:latest \
  latexmk -lualatex main.tex
```

`sudo apt install -y poppler-utils`
`python -m venv .venv`
`pip install pdf2image`
