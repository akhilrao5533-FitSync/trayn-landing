# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

old_media = """  @media (max-width:860px){.ai-tabs-wrap{grid-template-columns:1fr;gap:32px;}}"""

new_media = """  @media (max-width:860px){
    .ai-tabs-wrap{grid-template-columns:1fr;gap:20px;}
    .ai-tabs-wrap > div:first-child{order:2;}
    .ai-tabs-wrap > div:last-child{order:1;}
    .ai-tab{padding:14px 16px;margin-bottom:8px;}
    .ai-tab-title{margin-bottom:0;}
    .ai-tab.active .ai-tab-title{margin-bottom:6px;}
    .ai-tab:not(.active) .ai-tab-desc{display:none;}
  }"""

src = src.replace(old_media, new_media, 1)

if src == orig:
    print("WARNING: anchor not found.")
else:
    open(path, "w", encoding="utf-8").write(src)
    print("Patched mobile layout for AI tabs section.")
