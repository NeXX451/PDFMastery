import os
from pikepdf import Pdf
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog



def mergeBT():
    # fs = str(filedialog.askdirectory()).replace("/","\\")

    lblMergeBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    pdf = Pdf.new()
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        name = path.split("\\")[-1]
        with Pdf.open(path) as pd:
            pdf.pages.extend(pd.pages)

    pdf.save('merged.pdf')
    lblMergeBTN.config(text="Done!")

def unlockBT():
    lblUnlockBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    password = simpledialog.askstring(title="Password", prompt="Enter Password")
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path, password) as pd:
            pd.save(path.split()[-1].replace(".pdf", "(unlocked).pdf"))
    lblUnlockBTN.config(text="Done!")

def splitBT():
    lblSplitBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path) as pd:
            length = len(pd.pages)
            name = path.split("\\")[-1]
            pr = "The PDF {}".format(name) + " has {} pages\n".format(length)
            promp = pr + "The splitting position. The split is inclusive the left pdf. \n So Split on 5 means 1 to 5 " \
                         "are one pdf and 6 to 10 ( pdf has 10 pages) is the second pdf. "
            intervalX = simpledialog.askstring(title="Length", prompt=promp)
            print(intervalX)
            intervalX = int(intervalX)
            pdsplit = []
            for n, page in enumerate(pd.pages):
                pdsplit.append(page)
            i = 0
            pdfsplit1 = Pdf.new()
            pdfsplit2 = Pdf.new()
            for n, x in enumerate(pdsplit):
                if i <= intervalX - 1:
                    pdfsplit1.pages.append(x)
                    i += 1
                else:
                    pdfsplit2.pages.append(x)
                    i += 1
            pdfsplit1.save(name.replace(".pdf", "(split 1 to {}).pdf".format(intervalX)))
            st = str(intervalX + 1)
            p = st + " - " + str(length)
            pdfsplit2.save(name.replace(".pdf", "(split {}).pdf".format(p)))
    lblSplitBTN.config(text="Done!")

def rotateBT():
    lblRotateBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path) as pd:
            name = path.split("\\")[-1]
            promp = "Select degree (90/180/270) to rotate {}: ".format(name)
            rot = simpledialog.askstring(title="Rotate", prompt=promp)
            for p in pd.pages:
                p.Rotate = int(rot)
            pd.save(name.replace(".pdf", "(rotated{}).pdf".format(rot)))
    lblRotateBTN.config(text="Done!")

def cutBT():
    lblCutBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path) as pd:
            name = path.split("\\")[-1]
            lengthPDF = len(pd.pages)
            pr = "Current PDF: {}.\n".format(name)
            prl = "Has {} pages.\n".format(lengthPDF)
            prs = "Enter an interval to be cut from pdf (From and To are inclusive).\n"
            pr0 = "If entered 0 0 the pdf will be skipped!\n"
            promp = pr + prl + prs + pr0 + "Cut From page:"
            intervalX = simpledialog.askstring(title="Cut from", prompt=promp)
            promp2 = pr + prl + "Cutting from page {} ".format(intervalX) +"Cut To page:"
            intervalY = simpledialog.askstring(title="Cut to", prompt=promp2)
            if intervalX == '0' and intervalY == '0':
                continue
            pdsplit = []
            for n, page in enumerate(pd.pages):
                pdsplit.append(page)
            i = 0
            pdfcut = Pdf.new()
            for n, f in enumerate(pdsplit):
                if (i == int(intervalX) - 1) or (i > int(intervalX) - 1 and i < int(intervalY)):
                    i += 1
                else:
                    pdfcut.pages.append(f)
                    i += 1
            intervalCut = intervalX + "-" + intervalY
            pdfcut.save(name.replace(".pdf", "(cut {}).pdf".format(intervalCut)))
    lblCutBTN.config(text="Done!")


def printBT():
    lblprintBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path) as pd:
            length = len(pd.pages)
            name = path.split("\\")[-1]

            pdsplit  = []
            pdsplit2 = []
            for n, page in enumerate(pd.pages):
                if n % 2 == 0:
                    pdsplit.append(page)
                else:
                    pdsplit2.append(page)
            i = 0
            pdfsplit1 = Pdf.new()
            pdfsplit2 = Pdf.new()
            for n, x in enumerate(pdsplit):
               pdfsplit1.pages.append(x)

            for n, x in enumerate(pdsplit2):
               pdfsplit2.pages.append(x)

            pdfsplit1.save(name.replace(".pdf", "xSplit1.pdf"))
            pdfsplit2.save(name.replace(".pdf", "xSplit2.pdf"))
    lblprintBTN.config(text="Done!")

def exclusiveBT():
    lblexclusiveBTN.config(text="Working!")
    files = filedialog.askopenfiles()
    p = str(files[0].name).replace("/", "\\").rsplit('\\', 1)[0]
    os.chdir(p)
    for x in files:
        path = str(x.name).replace("/", "\\")
        print(path)
        with Pdf.open(path) as pd:
            name = path.split("\\")[-1]
            lengthPDF = len(pd.pages)
            pr = "Current PDF: {}.\n".format(name)
            prl = "Has {} pages.\n".format(lengthPDF)
            prs = "Enter an interval to be cut from pdf (From and To are inclusive).\n"
            pr0 = "If entered 0 0 the pdf will be skipped!\n"
            promp = pr + prl + prs + pr0 + "Cut From page:"
            intervalX = simpledialog.askstring(title="Cut from", prompt=promp)
            promp2 = pr + prl + "Cutting from page {} ".format(intervalX) +"Cut To page:"
            intervalY = simpledialog.askstring(title="Cut to", prompt=promp2)
            if intervalX == '0' and intervalY == '0':
                continue
            pdsplit = []
            for n, page in enumerate(pd.pages):
                pdsplit.append(page)
            i = 0
            pdfcut = Pdf.new()
            for n, f in enumerate(pdsplit):
                if (i != int(intervalX) - 1) and (i <= int(intervalX) - 1 or i > int(intervalY) - 1 ):
                    i += 1
                else:
                    pdfcut.pages.append(f)
                    i += 1
            intervalCut = intervalX + "-" + intervalY
            pdfcut.save(name.replace(".pdf", "(cut {}).pdf".format(intervalCut)))
    lblexclusiveBTN.config(text="Done!")


if __name__ == '__main__':
    root = Tk()
    root.geometry('260x315')
    root.title('PDF Mastery')
    root['bg'] = '#3c1b7d'
    root.resizable(False, False)

    mergeBTN = Button(root, text="Merge PDFs", command=mergeBT)
    mergeBTN.grid(row=9, column=0, stick=W, pady=10, padx=50)

    unlockBTN = Button(root, text="Unlock PDFs", command=unlockBT)
    unlockBTN.grid(row=19, column=0, stick=W, pady=10, padx=50)

    splitBTN = Button(root, text="Split PDFs", command=splitBT)
    splitBTN.grid(row=29, column=0, stick=W, pady=10, padx=50)

    rotateBTN = Button(root, text="Rotate PDFs", command=rotateBT)
    rotateBTN.grid(row=39, column=0, stick=W, pady=10, padx=50)

    cutBTN = Button(root, text="Cut PDFs", command=cutBT)
    cutBTN.grid(row=49, column=0, stick=W, pady=10, padx=50)

    printBTN = Button(root, text="Print Split", command=printBT)
    printBTN.grid(row=59, column=0, stick=W, pady=10, padx=50)

    exclusiveCUTBTN = Button(root, text="Exclusive Cut", command=exclusiveBT)
    exclusiveCUTBTN.grid(row=69, column=0, stick=W, pady=10, padx=50)

    lblMergeBTN = Label(root, text='', width=10)
    lblMergeBTN.grid(row=9, column=1)

    lblCutBTN = Label(root, text='', width=10)
    lblCutBTN.grid(row=49, column=1)

    lblSplitBTN = Label(root, text='', width=10)
    lblSplitBTN.grid(row=29, column=1)

    lblRotateBTN = Label(root, text='', width=10)
    lblRotateBTN.grid(row=39, column=1)

    lblUnlockBTN = Label(root, text='', width=10)
    lblUnlockBTN.grid(row=19, column=1)

    lblprintBTN = Label(root, text='', width=10)
    lblprintBTN.grid(row=59, column=1)

    lblexclusiveBTN = Label(root, text='', width=10)
    lblexclusiveBTN.grid(row=69, column=1)

    root.mainloop()

   
