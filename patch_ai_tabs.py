# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

new_section = """<!-- AI THROUGHOUT -->
<style>
  .ai-tabs-wrap{display:grid;grid-template-columns:380px 1fr;gap:56px;align-items:center;max-width:1100px;margin:0 auto;padding:0 24px;}
  @media (max-width:860px){.ai-tabs-wrap{grid-template-columns:1fr;gap:32px;}}
  .ai-tab{display:block;width:100%;text-align:left;background:transparent;border:1px solid var(--border2);border-radius:var(--radius-sm);padding:18px 20px;margin-bottom:12px;cursor:pointer;transition:background .2s,border-color .2s;color:var(--text);font-family:inherit;}
  .ai-tab.active{background:var(--accent-soft);border-color:var(--accent-line);}
  .ai-tab-title{font-size:15px;font-weight:700;margin-bottom:6px;display:flex;align-items:center;gap:10px;}
  .ai-tab-desc{font-size:13px;color:var(--text2);font-weight:300;line-height:1.55;}
  .ai-tab-icon{width:28px;height:28px;border-radius:8px;background:var(--accent-soft);border:1px solid var(--accent-line);display:flex;align-items:center;justify-content:center;color:var(--accent2);flex-shrink:0;}
  .ai-panel{display:none;}
  .ai-panel.active{display:block;}
</style>
<section class="section" style="background:var(--bg1);">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <div class="section-label reveal" style="text-align:center;">AI throughout</div>
      <h2 class="section-title reveal" style="text-align:center;max-width:680px;margin:0 auto 12px;">Iron does the busy work.<br>You stay the coach.</h2>
      <p class="reveal" style="font-size:16px;color:var(--text2);text-align:center;font-weight:300;max-width:520px;margin:0 auto;">Every AI feature in Trayn drafts, calculates, or suggests \u2014 you always review and approve before anything reaches a client.</p>
    </div>
  </div>
  <div class="ai-tabs-wrap reveal">
    <div>
      <button class="ai-tab active" onclick="trnAiTab(0)" id="ai-tab-0" type="button">
        <div class="ai-tab-title"><span class="ai-tab-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="9" width="3" height="6" rx="1"/><rect x="19" y="9" width="3" height="6" rx="1"/><line x1="6" y1="12" x2="18" y2="12"/><rect x="6" y="7" width="3" height="10" rx="1"/><rect x="15" y="7" width="3" height="10" rx="1"/></svg></span>Iron, your AI coach</div>
        <div class="ai-tab-desc">Ask about any client and get ground-truth compliance, BMI, TDEE and diet alignment \u2014 plus one-tap nudges and check-in drafts.</div>
      </button>
      <button class="ai-tab" onclick="trnAiTab(1)" id="ai-tab-1" type="button">
        <div class="ai-tab-title"><span class="ai-tab-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2v10l6.5 6.5"/></svg></span>AI diet plans, drafted in seconds</div>
        <div class="ai-tab-desc">Describe what you want \u2014 Iron drafts a full Indian meal plan at the exact calorie target, respecting dietary preference. You review and assign.</div>
      </button>
      <button class="ai-tab" onclick="trnAiTab(2)" id="ai-tab-2" type="button">
        <div class="ai-tab-title"><span class="ai-tab-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4v16M18 4v16M6 8h12M6 16h12M3 8h3M18 8h3M3 16h3M18 16h3"/></svg></span>AI workout plans, from your library</div>
        <div class="ai-tab-desc">Type "leg day, intermediate" and Iron pulls a complete session from your exercise library, matched to the client's level.</div>
      </button>
    </div>
    <div>
      <div class="phone-wrap">
        <div class="phone-showcase">
          <div class="phone-notch"></div>
          <div class="phone-body">
            <div class="ai-panel active" id="ai-panel-0">
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:10px;">
                <div style="width:22px;height:22px;border-radius:7px;background:rgba(61,77,255,.15);border:1px solid rgba(61,77,255,.3);display:flex;align-items:center;justify-content:center;">
                  <svg width="13" height="9" viewBox="0 0 26 16" fill="none"><rect x="0" y="5" width="5" height="6" rx="2.5" fill="#818cf8" opacity="0.7"/><rect x="5" y="6.5" width="16" height="3" rx="1.5" fill="#818cf8" opacity="0.7"/><rect x="21" y="5" width="5" height="6" rx="2.5" fill="#818cf8" opacity="0.7"/><rect x="10" y="3" width="6" height="10" rx="1.5" fill="#3d4dff"/></svg>
                </div>
                <span style="font-size:12px;font-weight:800;letter-spacing:2.5px;color:#F4F4F5;">IRON</span>
              </div>
              <div style="background:#15171C;border:1px solid #1B1E24;border-radius:12px;padding:10px;margin-bottom:8px;display:flex;align-items:center;gap:8px;">
                <div style="width:30px;height:30px;border-radius:50%;background:#374151;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#818cf8;">A</div>
                <div style="flex:1;"><div style="font-size:11px;font-weight:700;color:#F4F4F5;">Adeeba</div><div style="font-size:8px;color:#6B7280;">80 kg \u00b7 165 cm</div></div>
                <span style="background:rgba(61,77,255,.15);border:1px solid rgba(61,77,255,.3);border-radius:999px;padding:3px 8px;font-size:8px;font-weight:700;color:#818cf8;">BULK</span>
              </div>
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:5px;margin-bottom:10px;">
                <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:9px;padding:6px 5px;text-align:center;"><div style="font-size:11px;font-weight:800;color:#F87171;">25%</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;letter-spacing:.5px;">Workout</div></div>
                <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:9px;padding:6px 5px;text-align:center;"><div style="font-size:11px;font-weight:800;color:#F87171;">13%</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;letter-spacing:.5px;">Diet</div></div>
                <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:9px;padding:6px 5px;text-align:center;"><div style="font-size:11px;font-weight:800;color:#FBBF24;">0.0kg</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;letter-spacing:.5px;">Wt chg</div></div>
                <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:9px;padding:6px 5px;text-align:center;"><div style="font-size:11px;font-weight:800;color:#34D399;">2550</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;letter-spacing:.5px;">Kcal</div></div>
              </div>
              <div style="display:flex;justify-content:flex-end;margin-bottom:8px;"><div style="background:#3d4dff;border-radius:12px 12px 2px 12px;padding:7px 11px;max-width:72%;"><span style="font-size:9px;color:#fff;font-weight:600;">Her compliance?</span></div></div>
              <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:12px;padding:10px;">
                <div style="font-size:9px;color:#E5E7EB;line-height:1.6;margin-bottom:8px;">Only 3/12 workouts done in 30 days (25%). Last session was incomplete. Muscle gain is impossible at this rate.</div>
                <div style="background:#15171C;border:1px solid #1B1E24;border-radius:8px;padding:7px 9px;display:flex;justify-content:space-between;align-items:center;margin-bottom:7px;"><span style="font-size:8px;color:#9CA3AF;">Compliance (30d)</span><span style="font-size:9px;font-weight:800;color:#F87171;">25% (3/12)</span></div>
                <div style="background:rgba(61,77,255,.1);border:1px solid rgba(61,77,255,.25);border-radius:9px;padding:8px;display:flex;justify-content:space-between;align-items:center;"><div><div style="font-size:9px;font-weight:700;color:#F4F4F5;">Send nudge now</div><div style="font-size:7.5px;color:#9CA3AF;">3 days inactive</div></div><span style="background:#3d4dff;border-radius:6px;padding:4px 8px;font-size:8px;font-weight:700;color:#fff;white-space:nowrap;">Nudge \u2192</span></div>
              </div>
            </div>
            <div class="ai-panel" id="ai-panel-1">
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:10px;">
                <div style="width:22px;height:22px;border-radius:7px;background:rgba(61,77,255,.15);border:1px solid rgba(61,77,255,.3);display:flex;align-items:center;justify-content:center;">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2v10l6.5 6.5"/></svg>
                </div>
                <span style="font-size:12px;font-weight:800;letter-spacing:1.5px;color:#F4F4F5;">AI DIET GENERATOR</span>
              </div>
              <div style="background:#15171C;border:1px solid #1B1E24;border-radius:10px;padding:8px 10px;margin-bottom:10px;">
                <div style="font-size:8px;color:#6B7280;margin-bottom:3px;text-transform:uppercase;letter-spacing:.5px;">Prompt</div>
                <div style="font-size:10px;color:#E5E7EB;font-weight:600;">"High protein bulk, avoid dairy"</div>
              </div>
              <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:12px;padding:10px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
                  <div><div style="font-size:11px;font-weight:700;color:#F4F4F5;">South Indian Thali Bulk</div><div style="font-size:8px;color:#6B7280;margin-top:2px;">For Adeeba \u00b7 Dairy-free</div></div>
                  <span style="background:rgba(52,211,153,.12);border:1px solid rgba(52,211,153,.25);border-radius:999px;padding:3px 8px;font-size:9px;font-weight:800;color:#34D399;white-space:nowrap;">2592 kcal</span>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;margin-bottom:8px;">
                  <div style="background:#15171C;border-radius:7px;padding:5px;text-align:center;"><div style="font-size:10px;font-weight:800;color:#F4F4F5;">180g</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;">Protein</div></div>
                  <div style="background:#15171C;border-radius:7px;padding:5px;text-align:center;"><div style="font-size:10px;font-weight:800;color:#F4F4F5;">280g</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;">Carbs</div></div>
                  <div style="background:#15171C;border-radius:7px;padding:5px;text-align:center;"><div style="font-size:10px;font-weight:800;color:#F4F4F5;">70g</div><div style="font-size:6.5px;color:#6B7280;text-transform:uppercase;">Fat</div></div>
                </div>
                <div style="display:flex;flex-direction:column;gap:4px;margin-bottom:10px;">
                  <div style="display:flex;justify-content:space-between;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:9px;color:#E5E7EB;">Breakfast \u00b7 Poha + peanuts</span><span style="font-size:8px;color:#6B7280;">420 kcal</span></div>
                  <div style="display:flex;justify-content:space-between;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:9px;color:#E5E7EB;">Lunch \u00b7 Rice, dal, chicken</span><span style="font-size:8px;color:#6B7280;">780 kcal</span></div>
                  <div style="display:flex;justify-content:space-between;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:9px;color:#E5E7EB;">Snack \u00b7 Banana + almonds</span><span style="font-size:8px;color:#6B7280;">320 kcal</span></div>
                  <div style="display:flex;justify-content:space-between;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:9px;color:#E5E7EB;">Dinner \u00b7 Roti, soya, sabzi</span><span style="font-size:8px;color:#6B7280;">650 kcal</span></div>
                </div>
                <div style="background:#3d4dff;border-radius:9px;padding:8px;text-align:center;"><span style="font-size:10px;font-weight:700;color:#fff;">Assign to Adeeba</span></div>
              </div>
            </div>
            <div class="ai-panel" id="ai-panel-2">
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:10px;">
                <div style="width:22px;height:22px;border-radius:7px;background:rgba(61,77,255,.15);border:1px solid rgba(61,77,255,.3);display:flex;align-items:center;justify-content:center;">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4v16M18 4v16M6 8h12M6 16h12M3 8h3M18 8h3M3 16h3M18 16h3"/></svg>
                </div>
                <span style="font-size:12px;font-weight:800;letter-spacing:1.5px;color:#F4F4F5;">AI WORKOUT GENERATOR</span>
              </div>
              <div style="background:#15171C;border:1px solid #1B1E24;border-radius:10px;padding:8px 10px;margin-bottom:10px;">
                <div style="font-size:8px;color:#6B7280;margin-bottom:3px;text-transform:uppercase;letter-spacing:.5px;">Prompt</div>
                <div style="font-size:10px;color:#E5E7EB;font-weight:600;">"Leg day, intermediate, 45 min"</div>
              </div>
              <div style="background:#0E1013;border:1px solid #1B1E24;border-radius:12px;padding:10px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
                  <div><div style="font-size:11px;font-weight:700;color:#F4F4F5;">Leg Day</div><div style="font-size:8px;color:#6B7280;margin-top:2px;">For Adeeba \u00b7 Intermediate</div></div>
                  <span style="background:rgba(129,140,248,.12);border:1px solid rgba(129,140,248,.25);border-radius:999px;padding:3px 8px;font-size:9px;font-weight:800;color:#818cf8;white-space:nowrap;">~45 min</span>
                </div>
                <div style="display:flex;flex-direction:column;gap:4px;margin-bottom:10px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:6px 8px;"><span style="font-size:9px;color:#E5E7EB;">Barbell Squat</span><span style="font-size:8.5px;color:#818cf8;font-weight:700;">4 \u00d7 10</span></div>
                  <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:6px 8px;"><span style="font-size:9px;color:#E5E7EB;">Leg Press</span><span style="font-size:8.5px;color:#818cf8;font-weight:700;">3 \u00d7 12</span></div>
                  <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:6px 8px;"><span style="font-size:9px;color:#E5E7EB;">Walking Lunges</span><span style="font-size:8.5px;color:#818cf8;font-weight:700;">3 \u00d7 12</span></div>
                  <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:6px 8px;"><span style="font-size:9px;color:#E5E7EB;">Leg Curl</span><span style="font-size:8.5px;color:#818cf8;font-weight:700;">3 \u00d7 15</span></div>
                  <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:6px 8px;"><span style="font-size:9px;color:#E5E7EB;">Standing Calf Raise</span><span style="font-size:8.5px;color:#818cf8;font-weight:700;">4 \u00d7 20</span></div>
                </div>
                <div style="background:#3d4dff;border-radius:9px;padding:8px;text-align:center;"><span style="font-size:10px;font-weight:700;color:#fff;">Assign to Adeeba</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<script>
function trnAiTab(i){
  for(var j=0;j<3;j++){
    document.getElementById('ai-tab-'+j).classList.toggle('active', j===i);
    document.getElementById('ai-panel-'+j).classList.toggle('active', j===i);
  }
}
</script>

"""

start1 = src.find('<!-- AI ASSIST CAROUSEL -->')
end1 = src.find('<!-- TWO SIDES -->')

start2 = src.find('<!-- PROGRESS -->')
end2_marker = '<section class="showcase">\n  <div style="max-width:1100px;margin:0 auto;padding:0 24px;">\n    <div class="showcase-inner">\n      <div class="reveal">\n        <div class="section-label" style="margin-bottom:12px;">Progress tracking</div>'
end2 = src.find(end2_marker)

if -1 in (start1, end1, start2, end2):
    print(f"WARNING: marker not found. start1={start1} end1={end1} start2={start2} end2={end2}")
else:
    new_src = src[:start1] + new_section + src[end1:start2] + src[end2:]
    open(path, "w", encoding="utf-8").write(new_src)
    print(f"Patched. Removed carousel ({end1-start1} chars), removed Iron showcase ({end2-start2} chars), inserted tabbed section ({len(new_section)} chars).")
