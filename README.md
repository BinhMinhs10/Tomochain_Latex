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
### 3. Format function
```bash
\begin{equation}
	f(x) = x^2
\end{equation}
```

### 4.Captioned images
```bash
\usepackage{graphicx}
\begin{document}
	\begin{figure}[h!]
		\includegraphics[width=\linewidth]{1.png}
		\caption{Tomochain}
	\end{figure}
\end{document}
```

- h (here) - same location
- t (top) - top of page
- b (bottom) - bottom of page
- p (page) - on an extra page
- ! (override) - will force the specified location

### 5. Table of contents
Tự động tạo table content\figure\table dựa trên section\begin{figure}\begin{table} định nghĩa bên dưới
```bash
\begin{document}
	\tableofcontents
	\listoffigures
	\listoftables
	\newpage
\end{document}
```
### 6. Table
```bash
\begin{table}[h!]
	\begin{center}
		\caption{Your first table.}
		\label{tab:table1}
		\begin{tabular}{l|c|r} % <-- Alignments: 1st column left, 2nd middle and 3rd right, with vertical lines in between
			\textbf{Value 1} & \textbf{Value 2} & \textbf{Value 3}\\
			$\alpha$ & $\beta$ & $\gamma$ \\
			\hline
			1 & 1110.1 & a\\
			2 & 10.1 & b\\
			\hline
			3 & 23.113231 & c\\
		\end{tabular}
	\end{center}
\end{table}
```
### 7.List
- Unordered lists
```bash
\begin{itemize}
	\item One
	\item Two
	\item Three
\end{itemize}
```

- Unordered lists
```bash
\begin{enumerate}
	\item One
	\item Two
	\item Three
\end{enumerate}
```
### 8. Hyperlinks
```bash
\usepackage{graphicx}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    pdftitle={Sharelatex Example},
    bookmarks=true,
    pdfpagemode=FullScreen,
}
\begin{document}
	\href{http://www.latex-tutorial.com}{LaTeX-Tutorial}.
	URLs without an additional description: \url{http://www.latex-tutorial.com}
\end{document}
```
### 9. Font Style
```bash
Some of the \textbf{greatest}
discoveries in \underline{science} 
were made by \textbf{\textit{accident}}.
```