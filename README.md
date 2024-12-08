# Secure Delete Tool (SDT) v1.0

A Python-based tool for securely deleting files and folders by overwriting their content multiple times. This ensures that deleted data cannot be recovered.  

---

## **Features**
- **File Deletion:** Securely delete individual files using the `-f` option.
- **Folder Deletion:** Delete all files within a folder and its subdirectories using the `-r` option.
- **Custom Overwrite Passes:** Specify the number of overwrite passes using the `-R` option (default: 5).
- **Safety Confirmation:** Confirms with the user before performing any deletion operation.

---

## **Usage**

Run the script as a superuser for full functionality.  

### **Command-line Options:**
| Option | Description                              | Example                      |
|--------|------------------------------------------|------------------------------|
| `-f`   | Securely delete a specific file         | `python sdt.py -f myfile.txt` |
| `-r`   | Securely delete all files in a folder   | `python sdt.py -r myfolder` |
| `-R`   | Number of overwrite passes (optional)   | `python sdt.py -f myfile.txt -R 7` |

### **Examples:**
1. Delete a specific file:
   ```bash
   python sdt.py -f myfile.txt
