# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

# 1. Add position/overflow to .ai-tab + new progress bar CSS before </style>
old_css_close = """  .ai-panel{display:none;}
  .ai-panel.active{display:block;}
</style>"""

new_css_close = """  .ai-panel{display:none;}
  .ai-panel.active{display:block;}
  .ai-tab{position:relative;overflow:hidden;}
  .ai-tab-progress{position:absolute;bottom:0;left:0;height:2px;width:0;background:var(--accent2);}
  .ai-tab-progress.animate{animation:aiTabProgress 5s linear forwards;}
  @keyframes aiTabProgress{from{width:0;}to{width:100%;}}
</style>"""

src = src.replace(old_css_close, new_css_close, 1)

# 2. Manual-click flag on each tab's onclick + progress bar element before </button>
replacements = [
    ('onclick="trnAiTab(0)" id="ai-tab-0"', 'onclick="trnAiTab(0, true)" id="ai-tab-0"'),
    ('onclick="trnAiTab(1)" id="ai-tab-1"', 'onclick="trnAiTab(1, true)" id="ai-tab-1"'),
    ('onclick="trnAiTab(2)" id="ai-tab-2"', 'onclick="trnAiTab(2, true)" id="ai-tab-2"'),
    (
        'Ask about any client and get ground-truth compliance, BMI, TDEE and diet alignment \u2014 plus one-tap nudges and check-in drafts.</div>\n      </button>',
        'Ask about any client and get ground-truth compliance, BMI, TDEE and diet alignment \u2014 plus one-tap nudges and check-in drafts.</div>\n        <div class="ai-tab-progress" id="ai-tab-bar-0"></div>\n      </button>',
    ),
    (
        'Describe what you want \u2014 Iron drafts a full Indian meal plan at the exact calorie target, respecting dietary preference. You review and assign.</div>\n      </button>',
        'Describe what you want \u2014 Iron drafts a full Indian meal plan at the exact calorie target, respecting dietary preference. You review and assign.</div>\n        <div class="ai-tab-progress" id="ai-tab-bar-1"></div>\n      </button>',
    ),
    (
        '''Type "leg day, intermediate" and Iron pulls a complete session from your exercise library, matched to the client's level.</div>\n      </button>''',
        '''Type "leg day, intermediate" and Iron pulls a complete session from your exercise library, matched to the client's level.</div>\n        <div class="ai-tab-progress" id="ai-tab-bar-2"></div>\n      </button>''',
    ),
]

results = []
for old, new in replacements:
    found = old in src
    results.append(found)
    if found:
        src = src.replace(old, new, 1)

# 3. Replace script with auto-rotation logic
old_script = """<script>
function trnAiTab(i){
  for(var j=0;j<3;j++){
    document.getElementById('ai-tab-'+j).classList.toggle('active', j===i);
    document.getElementById('ai-panel-'+j).classList.toggle('active', j===i);
  }
}
</script>"""

new_script = """<script>
var aiTabIdx = 0;
var aiTabTimer = null;
var aiTabPaused = false;

function trnAiTab(i, manual){
  for(var j=0;j<3;j++){
    document.getElementById('ai-tab-'+j).classList.toggle('active', j===i);
    document.getElementById('ai-panel-'+j).classList.toggle('active', j===i);
    var bar = document.getElementById('ai-tab-bar-'+j);
    bar.classList.remove('animate');
    bar.style.width = '0';
  }
  aiTabIdx = i;
  if(manual){
    aiTabPaused = true;
    if(aiTabTimer){ clearInterval(aiTabTimer); aiTabTimer = null; }
    return;
  }
  var activeBar = document.getElementById('ai-tab-bar-'+i);
  void activeBar.offsetWidth;
  activeBar.classList.add('animate');
}

trnAiTab(0, false);
aiTabTimer = setInterval(function(){
  if(aiTabPaused) return;
  trnAiTab((aiTabIdx + 1) % 3, false);
}, 5000);
</script>"""

src = src.replace(old_script, new_script, 1)

if src == orig:
    print("WARNING: no changes made.")
else:
    open(path, "w", encoding="utf-8").write(src)
    css_ok = "ok" if old_css_close in orig else "MISS"
    script_ok = "ok" if old_script in orig else "MISS"
    print(f"Patched. CSS: {css_ok}. Tab anchors: {results}. Script: {script_ok}.")
