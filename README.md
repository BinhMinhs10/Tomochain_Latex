# Latex Tutorial
## Installer
[download](https://miktex.org/2.9/setup)
## Basic layout of a Latex file
```bash
\documentclass{article}

\title{TomoChain}
\date{20/11/2018}
\author{Nguyen Binh Minh}
\begin{document}
	\pagenumbering{gobble}
	\maketitle
	\newpage
	\pagenumbering{arabic}
	Hello world!
\end{document}
```

### 1. Hide page number for first page
```bash
\pagenumbering{gobble}
	content
\pagenumbering{arabic}
```
### 2. Sectioning element

```bash
\section{name}
	Content
	\subsection{sub name}
		Content
		\subsubsection{sub sub name}
			Content
```

```bash
\paragraph{name}
	Content
	\subparagraph{sub name}
		Content
		\subsubparagraph{sub sub name}
			Content
```

