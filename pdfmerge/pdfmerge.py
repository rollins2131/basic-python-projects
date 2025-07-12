import PyPDF2

pdfiles = ["1.pdf", "2.pdf"]

merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdffile = open(filename,'rb')
    pdfreader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfreader)
pdffile.close()
merger.write("merge.pdf") # its merges both pdf and create a new pdf called merge.pdf