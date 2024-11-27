import os
import mmap
#IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")
#NAVIGA NEL FILE SYSTEM
for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2}"
    files = ".format(root, len(dirs), len(files))"
    print(sToPrint)

def CercaStringaInFileContent(sFile,sString):
    sString = sString.lower()
    iLen = len(sString)
    #leggiamo il filename
    try:
        with open(sFile) as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            sAppo = s.readline()
            while len(sAppo)> 0 :
                sAppo = sAppo.lower()
                if(sAppo.find(sString.encode())!=-1):
                    return True
                else:
                        sAppo = s.readline()
    except:
        return False

def CercaStringaInFileName(sFile,sString):
    return False
for filename in files:
    iRet = CercaStringaInFileName(filename,sStringaDaCercare)
    if(iRet == True):
        print("Trovato file: ",filename)
        iNumFileTrovati = iNumFileTrovati + 1

def CercaStringaInFilename(sFilename,sStringToSearch):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    print("Cerco {0} in {1} ".format(sFilename1,sStringToSearch1))
    iRet = sFilename1.find(sStringToSearch1)
    if(iRet>-1):
        print("Trovato")
        return True
    return False

for filename in files:
#print(filename);
    iRet = CercaStringaInFileName(filename,sStringaDaCercare)
    if(iRet == True):
        print("Trovato file: ",filename)
        iNumFileTrovati = iNumFileTrovati + 1
    else:
        pathCompleto = os.path.join(root,filename)
        iRet = CercaStringaInFileContent(pathCompleto ,sStringaDaCercare)