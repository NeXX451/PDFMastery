# PDF Mastery
- This is a simple Python Script to "edit" pdf files. It can unlock them, if they are password protected.
  It can merge, rotate, cut and split pdf files.

- All the pdf files to be modified must be in the same folder as pdfMastery.py.

- Requirements are (if you want to use source code):
  python 3. 
  pikepdf
  tkinter

- To create an exe 

  ```bash
  pyinstaller --noconfirm --onefile --console --log-level "ERROR" --debug "all" --add-data ~/Python/Python310/Lib/site-packages/pptx;pptx/ pdfMastery.py
  ```

  or use with pptx
  
  ```bash
  auto-py-to-exe
  ```
  
  
