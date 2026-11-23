#!/usr/bin/env python3
"""Copy every game from /mnt/project-files into the site repo, wrapping artifact fragments in a full HTML page."""
import os,re,sys,shutil
SRC='/mnt/project-files'; DST=sys.argv[1] if len(sys.argv)>1 else '/home/claude/korokke-games'
HEAD=('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
 '<style data-fix="hidden">[hidden]{display:none!important}</style>\n')
for d in sorted(os.listdir(SRC)):
    f=os.path.join(SRC,d,'index.html')
    if not os.path.isfile(f): continue
    t=open(f,encoding='utf-8').read()
    if not re.match(r'\s*<!doctype',t,re.I):
        t=re.sub(r'<meta[^>]*name="viewport"[^>]*>\s*','',t)
        t=re.sub(r'<meta charset="utf-8">\s*','',t,flags=re.I)
        t=HEAD+t+'\n</html>\n'
    os.makedirs(os.path.join(DST,d),exist_ok=True)
    open(os.path.join(DST,d,'index.html'),'w',encoding='utf-8').write(t)
    for x in os.listdir(os.path.join(SRC,d)):
        if x!='index.html' and os.path.isfile(os.path.join(SRC,d,x)): shutil.copy2(os.path.join(SRC,d,x),os.path.join(DST,d,x))
    print('synced',d)
