import os
from pikepdf import Pdf
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog

#import cowsay


# def unlock(fs, contain):
#     cowsay.ghostbusters("lul locks... ")
#     print("\n")
#     password = input("Enter Password: ")
#     os.getcwd
#     files = os.listdir(fs)  # Get all the files in that directory
#     if contain == '0':
#         for x in files:
#             if x.endswith("pdf"):
#                 print(x)
#                 with Pdf.open(x, password) as pdf:
#                     pdf.save(x.replace(".pdf", "(unlocked).pdf"))  #
#     else:
#         for x in files:
#             if x.endswith("pdf") and x.find(contain) > 0:
#                 print(x)
#                 with Pdf.open(x, password) as pdf:
#                     pdf.save(x.replace(".pdf", "(unlocked).pdf"))  #
#
#
# def merge(fs, contain):
#     cowsay.cow("I merge")
#     print("\n")
#     print("For merging the files must be sorted in a way you want them to be merged.")
#     print("There are 2 options:")
#     print(
#         "1. You will let python decide how to sort the files. For this every filename must begin with a number (min 0, max 999).")
#     print("For this option press (1) when prompted. (RECOMMENDED)")
#     print("2. You don't care about order or correctness. This option merges the files without numbers in the filename.")
#     print("That means the files will be sorted alphabetically. This is not recommended!")
#
#     y = input("Select merging option (1/2): ")
#     if contain == '0':
#         if y == '1':
#             files = os.listdir(fs)  # Get all the files in that directory
#             di = {'1': [], '2': [], '3': []}
#             for x in files:
#                 if x.endswith("pdf"):
#                     try:
#                         int(list(x)[0])
#                         int(list(x)[1])
#                         int(list(x)[2])
#                         di['3'].append(x)
#                     except:
#                         try:
#                             int(list(x)[0])
#                             int(list(x)[1])
#                             di['2'].append(x)
#                         except:
#                             try:
#                                 int(list(x)[0])
#                                 di['1'].append(x)
#                             except:
#                                 None
#             pdf = Pdf.new()
#             for xi in di['1']:
#                 print(xi)
#                 src = Pdf.open(xi)
#                 pdf.pages.extend(src.pages)
#             if len(di['2']) > 0:
#                 for xi in di['2']:
#                     print(xi)
#                     src = Pdf.open(xi)
#                     pdf.pages.extend(src.pages)
#             if len(di['3']) > 0:
#                 for xi in di['3']:
#                     print(xi)
#                     src = Pdf.open(xi)
#                     pdf.pages.extend(src.pages)
#             pdf.save('merged.pdf')
#         elif y == '2':
#             print("Brave...")
#
#             files = os.listdir(fs)  # Get all the files in that directory
#             pdf = Pdf.new()
#             for x in files:
#                 if x.endswith("pdf"):
#                     print(x)
#                     src = Pdf.open(x)
#                     pdf.pages.extend(src.pages)
#             pdf.save('merged.pdf')
#     else:
#         if y == '1':
#
#             files = os.listdir(fs)  # Get all the files in that directory
#             di = {'1': [], '2': [], '3': []}
#             for x in files:
#                 if x.endswith("pdf") and x.find(contain) > 0:
#                     try:
#                         int(list(x)[0])
#                         int(list(x)[1])
#                         int(list(x)[2])
#                         di['3'].append(x)
#                     except:
#                         try:
#                             int(list(x)[0])
#                             int(list(x)[1])
#                             di['2'].append(x)
#                         except:
#                             try:
#                                 int(list(x)[0])
#                                 di['1'].append(x)
#                             except:
#                                 None
#             pdf = Pdf.new()
#             for xi in di['1']:
#                 print(xi)
#                 src = Pdf.open(xi)
#                 pdf.pages.extend(src.pages)
#             if len(di['2']) > 0:
#                 for xi in di['2']:
#                     print(xi)
#                     src = Pdf.open(xi)
#                     pdf.pages.extend(src.pages)
#             if len(di['3']) > 0:
#                 for xi in di['3']:
#                     print(xi)
#                     src = Pdf.open(xi)
#                     pdf.pages.extend(src.pages)
#             pdf.save('merged.pdf')
#         elif y == '2':
#             print("Brave...")
#
#             files = os.listdir(fs)  # Get all the files in that directory
#             pdf = Pdf.new()
#             for x in files:
#                 if x.endswith("pdf") and x.find(contain) > 0:
#                     print(x)
#                     src = Pdf.open(x)
#                     pdf.pages.extend(src.pages)
#             pdf.save('merged.pdf')
#
#
# def rotate(fs, contain):
#     cowsay.cow("I rotate")
#     print("\n")
#
#     files = os.listdir(fs)  # Get all the files in that directory
#     if contain == '0':
#         for x in files:
#             if x.endswith("pdf"):
#                 my_pdf = Pdf.open(x)
#                 rot = input("select degree (90/180/270) to rotate {}: ".format(x))
#                 for page in my_pdf.pages:
#                     page.Rotate = int(rot)
#                 my_pdf.save(x.replace(".pdf", "(rotated{}).pdf".format(rot)))
#     else:
#         for x in files:
#             if x.endswith("pdf") and x.find(contain) > 0:
#                 my_pdf = Pdf.open(x)
#                 rot = input("select degree (90/180/270) to rotate {}: ".format(x))
#                 for page in my_pdf.pages:
#                     page.Rotate = int(rot)
#                 my_pdf.save(x.replace(".pdf", "(rotated{}).pdf".format(rot)))
#
#
# def cut(fs, contain):
#     cowsay.cow("I cut")
#     print("\n")
#
#     files = os.listdir(fs)  # Get all the files in that directory
#     if contain == '0':
#         for x in files:
#             if x.endswith("pdf"):
#                 pdf = Pdf.open(x)
#                 print("Current pdf: {}".format(x))
#                 lengthPDF = len(pdf.pages)
#                 print("The PDF has {} pages".format(lengthPDF))
#                 print("Enter an interval to be cut from pdf (From and To are inclusive)")
#                 print("If entered 0 0 the pdf will be skipped!")
#                 intervalX = input("Cut From page: ")
#                 intervalY = input("To page: ")
#                 if intervalX == '0' and intervalY == '0':
#                     continue
#                 pdsplit = []
#                 for n, page in enumerate(pdf.pages):
#                     pdsplit.append(page)
#
#                 i = 0
#                 pdfcut = Pdf.new()
#                 for n, f in enumerate(pdsplit):
#                     if (i == int(intervalX) - 1) or (i > int(intervalX) - 1 and i < int(intervalY)):
#                         i += 1
#                     else:
#                         pdfcut.pages.append(f)
#                         i += 1
#                 intervalCut = intervalX + "-" + intervalY
#                 pdfcut.save(x.replace(".pdf", "(cut {}).pdf".format(intervalCut)))
#     else:
#         for x in files:
#             if x.endswith("pdf") and x.find(contain) > 0:
#                 pdf = Pdf.open(x)
#                 print("Current pdf: {}".format(x))
#                 lengthPDF = len(pdf.pages)
#                 print("The PDF has {} pages".format(lengthPDF))
#                 print("Enter an interval to be cut from pdf (From and To are inclusive)")
#                 print("If entered 0 0 the pdf will be skipped!")
#                 intervalX = input("Cut From page: ")
#                 intervalY = input("To page: ")
#                 if intervalX == '0' and intervalY == '0':
#                     continue
#                 pdsplit = []
#                 for n, page in enumerate(pdf.pages):
#                     pdsplit.append(page)
#
#                 i = 0
#                 pdfcut = Pdf.new()
#                 for n, f in enumerate(pdsplit):
#                     if (i == int(intervalX) - 1) or (i > int(intervalX) - 1 and i < int(intervalY)):
#                         i += 1
#                     else:
#                         pdfcut.pages.append(f)
#                         i += 1
#                 intervalCut = intervalX + "-" + intervalY
#                 pdfcut.save(x.replace(".pdf", "(cut {}).pdf".format(intervalCut)))
#
#
# def split(fs, contain):
#     cowsay.cow("I split")
#     print("\n")
#
#     files = os.listdir(fs)  # Get all the files in that directory
#     if contain == '0':
#         for f in files:
#             if f.endswith("pdf"):
#                 pdf = Pdf.open(f)
#                 print("Current pdf: {}".format(f))
#                 lengthPD = len(pdf.pages)
#                 print("The PDF has {} pages.\n".format(lengthPD))
#                 print("The split is inclusive the left pdf.")
#                 print("So Split on 5 means 1 to 5 are one pdf and 6 to 10 (pdf has 10 pages) is the second pdf.")
#                 intervalX = int(input("Split on page: "))
#
#                 pdsplit = []
#                 for n, page in enumerate(pdf.pages):
#                     pdsplit.append(page)
#
#                 i = 0
#                 pdfsplit1 = Pdf.new()
#                 pdfsplit2 = Pdf.new()
#                 for n, x in enumerate(pdsplit):
#                     if i <= intervalX - 1:
#                         pdfsplit1.pages.append(x)
#                         i += 1
#                     else:
#                         pdfsplit2.pages.append(x)
#                         i += 1
#                 pdfsplit1.save(f.replace(".pdf", "(split 1 to {}).pdf".format(intervalX)))
#                 st = str(intervalX + 1)
#                 p = st + " - " + str(lengthPD)
#                 pdfsplit2.save(f.replace(".pdf", "(split {}).pdf".format(p)))
#     else:
#         for f in files:
#             if f.endswith("pdf") and f.find(contain) > 0:
#                 pdf = Pdf.open(f)
#                 print("Current pdf: {}".format(f))
#                 lengthPD = len(pdf.pages)
#                 print("The PDF has {} pages.\n".format(lengthPD))
#                 print("The split is inclusive the left pdf.")
#                 print("So Split on 5 means 1 to 5 are one pdf and 6 to 10 (pdf has 10 pages) is the second pdf.")
#                 intervalX = int(input("Split on page: "))
#
#                 pdsplit = []
#                 for n, page in enumerate(pdf.pages):
#                     pdsplit.append(page)
#
#                 i = 0
#                 pdfsplit1 = Pdf.new()
#                 pdfsplit2 = Pdf.new()
#                 for n, x in enumerate(pdsplit):
#                     if i <= intervalX - 1:
#                         pdfsplit1.pages.append(x)
#                         i += 1
#                     else:
#                         pdfsplit2.pages.append(x)
#                         i += 1
#                 pdfsplit1.save(f.replace(".pdf", "(split 1 to {}).pdf".format(intervalX)))
#                 st = str(intervalX + 1)
#                 p = st + " - " + str(lengthPD)
#                 pdfsplit2.save(f.replace(".pdf", "(split {}).pdf".format(p)))


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

if __name__ == '__main__':
    # cowsay.stegosaurus("Henlo I do pdf stuff..")
    # print("\n")
    # print("This is a pdf mastery tool!\n")
    # print("Python will now ask you for the Directory with the PDF files you wish to modify.")
    # input("Press enter to proceed.")

    root = Tk()
    root.geometry('260x230')
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


    # root.withdraw()
    # fs = str(filedialog.askdirectory()).replace("/","\\")
    # os.chdir(fs)

    # print("Selected Directory: {}".format(fs))

    root.mainloop()

    # files = filedialog.askopenfiles()
    #
    # pdf = Pdf.new()
    # for x in files:
    #     path = str(x.name).replace("/", "\\")
    #     print(path)
    #     with Pdf.open(path) as pd:
    #         pdf.pages.extend(pd.pages)
    #
    # pdf.save('yeet.pdf')

    # while False:
    #     action = input("Select operation (unlock/merge/rotate/cut/split/quit): ")
    #     if action == 'quit':
    #         break
    #     contain = input("Filename contains string (0/string): ")
    #     if action == 'rotate':
    #         rotate(fs,contain)
    #     elif action == 'merge':
    #         merge(fs,contain)
    #     elif action == 'unlock':
    #         unlock(fs,contain)
    #     elif action == 'cut':
    #         cut(fs,contain)
    #     elif action == 'split':
    #         split(fs,contain)
    #     else:
    #         print("Invalid Action!")
    #
    #     input("Done press Enter.")
