# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

carousel_section = """<!-- AI ASSIST CAROUSEL -->
<style>
  .ai-carousel-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;-ms-overflow-style:none;}
  .ai-carousel-wrap::-webkit-scrollbar{display:none;}
  .ai-carousel{display:flex;gap:20px;padding:4px 24px 12px;scroll-snap-type:x mandatory;max-width:1148px;margin:0 auto;}
  .ai-card{flex:0 0 auto;width:min(340px,82vw);scroll-snap-align:start;background:var(--bg1);border:1px solid var(--border2);border-radius:var(--radius);padding:28px;}
  .ai-card-icon{width:40px;height:40px;border-radius:11px;background:var(--accent-soft);border:1px solid var(--accent-line);display:flex;align-items:center;justify-content:center;margin-bottom:18px;color:var(--accent2);}
  .ai-card h3{font-size:18px;font-weight:700;color:var(--text);margin-bottom:8px;letter-spacing:-0.2px;}
  .ai-card p{font-size:14px;color:var(--text2);line-height:1.65;font-weight:300;}
  .ai-card-tag{display:inline-block;margin-top:14px;font-size:11px;font-weight:600;color:var(--accent2);letter-spacing:.5px;text-transform:uppercase;}
  @media (min-width:1180px){.ai-carousel{justify-content:center;}}
</style>
<section class="section" style="padding-top:56px;padding-bottom:56px;">
  <div class="container">
    <div style="text-align:center;margin-bottom:36px;">
      <div class="section-label reveal" style="text-align:center;">AI throughout</div>
      <h2 class="section-title reveal" style="text-align:center;max-width:680px;margin:0 auto 12px;">Iron does the busy work.<br>You stay the coach.</h2>
      <p class="reveal" style="font-size:16px;color:var(--text2);text-align:center;font-weight:300;max-width:520px;margin:0 auto;">Every AI feature in Trayn drafts, calculates, or suggests \u2014 you always review and approve before anything reaches a client.</p>
    </div>
  </div>
  <div class="ai-carousel-wrap">
    <div class="ai-carousel">
      <div class="ai-card reveal stagger-1">
        <div class="ai-card-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="9" width="3" height="6" rx="1"/><rect x="19" y="9" width="3" height="6" rx="1"/><line x1="6" y1="12" x2="18" y2="12"/><rect x="6" y="7" width="3" height="10" rx="1"/><rect x="15" y="7" width="3" height="10" rx="1"/></svg></div>
        <h3>Iron, your AI coach</h3>
        <p>Ask about any client \u2014 compliance, BMI, TDEE, diet alignment, weight trend \u2014 and Iron answers with the same numbers on their profile. It can even draft a nudge or check-in message for you to send.</p>
        <span class="ai-card-tag">Assists, you decide</span>
      </div>
      <div class="ai-card reveal stagger-2">
        <div class="ai-card-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2v10l6.5 6.5"/></svg></div>
        <h3>AI diet plans, drafted in seconds</h3>
        <p>Describe what you want \u2014 "high protein bulk" or "1800 cal cut" \u2014 and Iron drafts a full Indian meal plan at the exact calorie target for that client, respecting their dietary preference. You review and assign.</p>
        <span class="ai-card-tag">Drafts the plan for you</span>
      </div>
      <div class="ai-card reveal stagger-3">
        <div class="ai-card-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4v16M18 4v16M6 8h12M6 16h12M3 8h3M18 8h3M3 16h3M18 16h3"/></svg></div>
        <h3>AI workout plans, built from your library</h3>
        <p>Type "leg day, intermediate" and Iron pulls a complete session \u2014 sets, reps, rest times \u2014 from your exercise library, matched to the client's level. Tweak anything before it's assigned.</p>
        <span class="ai-card-tag">Built from your exercises</span>
      </div>
    </div>
  </div>
</section>

"""

old = """    <span class="ticker-item">Offline Support</span>
  </div>
</div>


<!-- TWO SIDES -->"""

new = """    <span class="ticker-item">Offline Support</span>
  </div>
</div>

""" + carousel_section + """<!-- TWO SIDES -->"""

src = src.replace(old, new, 1)

if src == orig:
    print("WARNING: anchor not found \u2014 no changes made.")
else:
    open(path, "w", encoding="utf-8").write(src)
    print("Patched index.html with AI carousel section.")
