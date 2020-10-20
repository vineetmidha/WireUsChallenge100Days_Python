# Problem statement in description

def change_filenames(path):
    import os

    files = os.listdir(path)

    n = 1

    for i in range(len(files)):
        if files[i][-4:] == ".jpg":
            prefix = '0'+str(n) if n < 10 else str(n)
            files[i] = prefix+files[i][0].upper()+files[i][1:]
            n+=1

    pngs = [files[i] for i in range(len(files)) if files[i][-4:]=='.png']
    jpgs = [files[i] for i in range(len(files)) if files[i][-4:]=='.jpg']

    print(pngs)
    print(jpgs)
    
