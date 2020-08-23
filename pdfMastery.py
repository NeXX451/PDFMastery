import os
from pikepdf import Pdf
from glob import glob


import cowsay

def unlock():
    cowsay.ghostbusters("lul locks... ")
    print("\n")
    password = input("Enter Password: ")
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    for x in files:
        if x.endswith("pdf"):
            print(x)
            with Pdf.open(x, password) as pdf:
                pdf.save(x.replace(".pdf", "(unlocked).pdf")) #

def merge():
    cowsay.cow("I merge")
    print("\n")
    print("The order with which the PDFs will be merged depends on the numbers. So rename the files in the sequence you wish to merge!\n")
    print("All PDFs must be named as follows:\n")
    print("\"i name.pdf\" (i SPACE name.pdf) where i is a number.\n")
    print("[\"0 name.pdf\", \"1 name.pdf\", \"2 name.pdf\"] is acceptable.\n")
    print("There shouldn't be any duplicates! [\"0 name.pdf\", \"0 name1.pdf\"], will be accepted, but\n")
    print("there is no guarantee the pdfs will be merged in the correct order!")
    

    while True:
        inp = input("Run File name test (y/n): ")
        if inp == 'y':
            cwd = os.getcwd()  # Get the current working directory (cwd)
            files = os.listdir(cwd)  # Get all the files in that directory
            #print("Files in %r: %s" % (cwd, files))
            for x in files:
                if x.endswith('pdf'):
                    print(x)
            print("\n")
            print("\n")
            print("Wenn alles in Ordnung, druecke (n)")
        else:
            break

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    pdf = Pdf.new()


    """ for x in files:
        if x.endswith("pdf"):
            fileAr.append(x) """
    for j in range(len(files)):
        #print(j)
        for x in files:
            if x.startswith("{} ".format(j)):
                print(x)
                src = Pdf.open(x)
                pdf.pages.extend(src.pages)
                
    pdf.save('merged.pdf')


def rotate():
    cowsay.cow("I rotate")
    print("\n")
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    for x in files:
        if x.endswith("pdf"):
            my_pdf = Pdf.open(x)
            rot = input("select degree (90/180/270) to rotate {}: ".format(x))
            for page in my_pdf.pages:
                page.Rotate = int(rot)
            my_pdf.save(x.replace(".pdf", "(rotated{}).pdf".format(rot)))#x.replace(".pdf", "(rotated{}).pdf".format(rot))

def cut():
    cowsay.cow("I cut")
    print("\n")

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory

    for x in files:
        if x.endswith("pdf"):
            pdf = Pdf.open(x)
            print("Current pdf: {}".format(x))
            lengthPDF = len(pdf.pages)
            print("The PDF has {} pages".format(lengthPDF))
            print("Enter an interval to be cut from pdf (From and To are inclusive)\n")
            print("If entered 0 0 the pdf will be skipped!")
            intervalX = input("Cut From page: ")
            intervalY = input("To page: ")
            if intervalX == '0' and intervalY == '0':
                continue
            pdsplit = []
            for n, page in enumerate(pdf.pages):
                pdsplit.append(page)

            i = 0
            pdfcut = Pdf.new()
            for n, f in enumerate(pdsplit):
                if (i == int(intervalX)-1) or (i > int(intervalX)-1 and i<int(intervalY)):
                    i+=1
                else:
                    pdfcut.pages.append(f)
                    i+=1
            intervalCut = intervalX + "-" + intervalY
            pdfcut.save(x.replace(".pdf", "(cut {}).pdf".format(intervalCut)))
    
def split():
    cowsay.cow("I split")
    print("\n")

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory

    for f in files:
        if f.endswith("pdf"):
            pdf = Pdf.open(f)
            print("Current pdf: {}".format(f))
            lengthPD = len(pdf.pages)
            print("The PDF has {} pages.\n".format(lengthPD))
            print("The split is inclusive the left pdf.\n")
            print("So Split on 5 means 1 to 5 are one pdf and 6 to 10 (pdf has 10 pages) is the second pdf.")
            intervalX = int(input("Split on page: "))

            pdsplit = []
            for n, page in enumerate(pdf.pages):
                pdsplit.append(page)

            i = 0
            pdfsplit1 = Pdf.new()
            pdfsplit2 = Pdf.new()
            for n, x in enumerate(pdsplit):
                if i <= intervalX-1:
                    pdfsplit1.pages.append(x)
                    i+=1
                else:
                    pdfsplit2.pages.append(x)
                    i+=1
            pdfsplit1.save(f.replace(".pdf", "(split 1 to {}).pdf".format(intervalX)))
            st = str(intervalX+1)
            p = st + " - "+str(lengthPD)
            pdfsplit2.save(f.replace(".pdf", "(split {}).pdf".format(p)))

if __name__ == '__main__':
    cowsay.stegosaurus("Henlo I do pdf stuff..")
    print("\n")
    print("This is a pdf mastery tool!\n")

    while True:
        action = input("Select operation (unlock/merge/rotate/cut/split/quit): ")
        if action == 'quit':
            break
        if action == 'rotate':
            rotate()
        elif action == 'merge':
            merge()
        elif action == 'unlock':
            unlock()
        elif action == 'cut':
            cut()
        elif action == 'split':
            split()
        else:
            print("Invalid Action!")

        input("Done press Enter.")

