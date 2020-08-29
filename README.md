The following steps apply to MAC OS system:
1. Put the files needed to be renamed in a folder called ‘target’
2. Put ‘pdf_rename.py’ and ‘target’ into a same folder (let's call this folder 'pdf_rename')
3. Open Terminal, go to the folder that contains ‘pdf_rename.py’ and ‘target’
```
cd path_to_your_pdf_renamefolder_directory
```
4. Install needed packages
```
pip install pdfrw
```
5. Execute pdf_rename.py
```
python -m pdf_rename
```
If Error occurs saying 'zsh: permission denied', try this instead:
```
sudo python -m pdf_rename
```
after this line being executed, you need to enter password of your device
6. Files in 'target' folders are renamed. Done!
