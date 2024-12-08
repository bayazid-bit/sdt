import os 
import sys

def showBanner():
    banner = """
    ==============================================
                S D T v1.0
                       by
                MD.Bayazid
    ----------------------------------------------
    A tool to securely delete files and folders
    ----------------------------------------------
    USAGE:
        -f <file_path>        Securely delete a specific file
        -r <folder_path>      Securely delete all files in a folder
        -R <repeat_times>     Number of overwrite passes (default: 5)

    EXAMPLES:
        python3 sdt.py -f myfile.txt
        python3 sdt.py -r myfolder -R 7

    IMPORTANT:
        * Please run this script as a superuser!
        * Ensure you have the necessary permissions.

    ==============================================
    """
    print(banner)

if not os.geteuid() == 0:
    showBanner()
    print("\n")
    print("Please run this script as super (root) user!\n\n")
    sys.exit()

class start:
    def getval(self,key):
        try:
            val = self.a[self.a.index(key)+1]
            
            return val 
        except: 
            return None 

    def get_tree(self ,  path) -> list:
        f = []  
        de = []
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    de.append(entry.path)
                    t , g = self.get_tree(entry.path)
                     
                    for h in g:
                        de.append(h)
                    for i in t:
                        f.append(i)
                    
                else:
                    f.append(entry.path)  
                
        return f , de


    def __init__(self):
        self. a = sys.argv
        
        if len(self.a) <2:
            showBanner()
            sys.exit()
        

        self.file_path = self.getval("-f")
        
        self.folder_path = self.getval("-r")
        self.repeat = self.getval("-R")

        if self.repeat:
            self.repeat=int(self.repeat)

        cmd  = input("> are you sure to do this operation ? (y/n): ")
        print(cmd.encode())

        if  cmd.strip().lower() !='y':
            print("[!] Exiting.......")
            sys.exit()



        if self.file_path and not self.folder_path :
            if self.repeat:
                    work(self.file_path, self.repeat)
            else:
                work(self.file_path)

        elif self.folder_path and not self.file_path :
            if not os.path.exists(self.folder_path):
                print(f"[!] [error] folder: {self.folder_path} does not  exists!\n[*] exiting......")
                sys.exit()
            print(f"[*] scaning the folder................" , end='')
            try:
                files , dirs = self.get_tree(self.folder_path)
            except Exception as e:
                print(f"\n[!] [error] {e}")
                sys.exit()

            print('done')
            print(f"[*] total dirs: {len(dirs)}")
            print(f"[*] total files: {len(files)}")
            
            for file in files:
            
                self.file_path = file 
                if self.repeat:
                    work(self.file_path, self.repeat)
                else:
                    work(self.file_path)

            dirs.reverse()
            for d in dirs:
                print(f"[*] [deleting_folder] {d} ..............." , end='')
                os.rmdir(d)
                print(dirs.index(d) , end='')
                print('ok')
        
        else:
            showBanner()
            sys.exit()

        


        os.rmdir(self.folder_path)
class work:
    def __init__(self , path , repeat=5):
        
        self.path = path 
        if os.path.exists(self.path) and os.path.isfile(self.path):
            print(f'[*] [deleting_file] {self.path}...........',end='')
            try:
                for i in range(repeat ):
                    
                    self.overwrite()
                        
                os.remove(self.path)
                print("ok")
            except Exception as e :
                    print(f"\n[!] [error] {e}")
                    print('[*] skiping ......')
        else:
            print(f"file: {self.path} does not exists!")
            sys.exit() 

    def overwrite(self ):
            with open(self.path , 'wb') as file :
                file.write(os.urandom(1024))
        

if __name__=="__main__":
    
        start()
    
