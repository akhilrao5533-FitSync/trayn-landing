# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

old = """@media(max-width:768px){
  .showcase{padding:64px 0;}
  .showcase-inner{grid-template-columns:1fr !important;gap:48px;}
  .showcase-formcheck{grid-template-columns:1fr !important;gap:24px;}
  .showcase-arrow{transform:rotate(90deg);}
  .phone-showcase{width:300px !important;}
  .phone-showcase-sm{width:280px !important;}
  .phone-wrap{justify-content:center;}
}"""

new = """@media(max-width:768px){
  .showcase{padding:64px 0;}
  .showcase-inner{grid-template-columns:1fr !important;gap:48px;}
  .showcase-formcheck{grid-template-columns:1fr !important;gap:24px;}
  .showcase-arrow{transform:rotate(90deg);}
  .showcase-arrow div{color:var(--text2) !important;}
  .phone-showcase{width:300px !important;}
  .phone-showcase-sm{width:280px !important;}
  .phone-wrap{justify-content:center;}
}"""

src = src.replace(old, new, 1)

if src == orig:
    print("WARNING: anchor not found.")
else:
    open(path, "w", encoding="utf-8").write(src)
    print("Patched async/review caption color for mobile.")
