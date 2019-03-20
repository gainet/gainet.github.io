from glob import glob
import os

if __name__=="__main__":
    for f in glob("*.pdf"):
        new_filename = f[:-3]
        os.system("pdfimages -png {0} {1}".format(f, new_filename))
