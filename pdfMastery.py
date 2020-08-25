import os
from pikepdf import Pdf
from tkinter import filedialog
from tkinter import *
import cowsay





def unlock(fs):
    cowsay.ghostbusters("lul locks... ")
    print("\n")
    password = input("Enter Password: ")
    os.getcwd
    files = os.listdir(fs)  # Get all the files in that directory

    for x in files:
        if x.endswith("pdf"):
            print(x)
            with Pdf.open(x, password) as pdf:
                pdf.save(x.replace(".pdf", "(unlocked).pdf")) #
    

def merge(fs):
    cowsay.cow("I merge")
    print("\n")
    print("For merging the files must be sorted in a way you want them to be merged.")
    print("There are 2 options:")
    print("1. You will let python decide how to sort the files. For this every filename must begin with a number (min 0, max 999).")
    print("For this option press (1) when prompted. (RECOMMENDED)")
    print("2. You don't care about order or correctness. This option merges the files without numbers in the filename.")
    print("That means the files will be sorted alphabetically. This is not recommended!")
    
    y = input("Select merging option (1/2): ")
    if y == '1':
        
        files = os.listdir(fs)  # Get all the files in that directory
        di ={'1': [],'2':[] , '3':[]}
        for x in files:
            if x.endswith("pdf"):
                try:
                    int(list(x)[0])
                    int(list(x)[1])
                    int(list(x)[2])
                    di['3'].append(x)
                except:
                    try:
                        int(list(x)[0])
                        int(list(x)[1])
                        di['2'].append(x)
                    except:
                        try:
                            int(list(x)[0])
                            di['1'].append(x)
                        except:
                            None
        pdf = Pdf.new()
        for xi in di['1']:
            print(xi)
            src = Pdf.open(xi)
            pdf.pages.extend(src.pages)
        if len(di['2']) >0:
            for xi in di['2']:
                print(xi)
                src = Pdf.open(xi)
                pdf.pages.extend(src.pages)
        if len(di['3']) >0:
            for xi in di['3']:
                print(xi)
                src = Pdf.open(xi)
                pdf.pages.extend(src.pages)
        pdf.save('merged.pdf')
    elif y=='2':
        print("Brave...")
        
        files = os.listdir(fs)  # Get all the files in that directory
        pdf = Pdf.new()
        for x in files:
            if x.endswith("pdf"):
                print(x)
                src = Pdf.open(x)
                pdf.pages.extend(src.pages)
        pdf.save('merged.pdf')

def rotate(fs):
    cowsay.cow("I rotate")
    print("\n")
    
    files = os.listdir(fs)  # Get all the files in that directory
    for x in files:
        if x.endswith("pdf"):
            my_pdf = Pdf.open(x)
            rot = input("select degree (90/180/270) to rotate {}: ".format(x))
            for page in my_pdf.pages:
                page.Rotate = int(rot)
            my_pdf.save(x.replace(".pdf", "(rotated{}).pdf".format(rot)))#x.replace(".pdf", "(rotated{}).pdf".format(rot))

def cut(fs):
    cowsay.cow("I cut")
    print("\n")

    
    files = os.listdir(fs)  # Get all the files in that directory

    for x in files:
        if x.endswith("pdf"):
            pdf = Pdf.open(x)
            print("Current pdf: {}".format(x))
            lengthPDF = len(pdf.pages)
            print("The PDF has {} pages".format(lengthPDF))
            print("Enter an interval to be cut from pdf (From and To are inclusive)")
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
    
def split(fs):
    cowsay.cow("I split")
    print("\n")

    
    files = os.listdir(fs)  # Get all the files in that directory
    
    for f in files:
        if f.endswith("pdf"):
            pdf = Pdf.open(f)
            print("Current pdf: {}".format(f))
            lengthPD = len(pdf.pages)
            print("The PDF has {} pages.\n".format(lengthPD))
            print("The split is inclusive the left pdf.")
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
    print("Python will now ask you for the Directory with the PDF files you wish to modify.")
    input("Press enter to proceed.")
    

    root = Tk()
    root.withdraw()
    fs = str(filedialog.askdirectory()).replace("/","\\")
    os.chdir(fs)
    
    print("Selected Directory: {}".format(fs))

    while True:
        action = input("Select operation (unlock/merge/rotate/cut/split/quit): ")
        if action == 'quit':
            break
        if action == 'rotate':
            rotate(fs)
        elif action == 'merge':
            merge(fs)
        elif action == 'unlock':
            unlock(fs)
        elif action == 'cut':
            cut(fs)
        elif action == 'split':
            split(fs)
        else:
            print("Invalid Action!")

        input("Done press Enter.")

