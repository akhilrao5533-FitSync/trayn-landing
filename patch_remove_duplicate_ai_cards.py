# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

old = """      <div class="feature-card reveal stagger-2">
        <div class="feature-icon-wrap"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <h3>Video Calls</h3>
        <p>Built-in video sessions via Google Meet \u2014 no Zoom, no separate links. 15 sessions/month on Verified and Certified. Unlimited on Pro. Session history tracked automatically.</p>
        <span class="feature-tag">Replaces Zoom</span>
      </div>
      <div class="feature-card reveal stagger-3">
        <div class="feature-icon-wrap"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="9" width="3" height="6" rx="1"/><rect x="19" y="9" width="3" height="6" rx="1"/><line x1="6" y1="12" x2="18" y2="12"/><rect x="6" y="7" width="3" height="10" rx="1"/><rect x="15" y="7" width="3" height="10" rx="1"/></svg></div>
        <h3>Iron \u2014 Your AI Coach</h3>
        <p>Ask Iron about any client: compliance, BMI, TDEE, diet alignment, weight trends. Get one-tap actions \u2014 new workout, new diet, send a nudge, or draft a check-in message. Speaks Hindi, Hinglish, Tamil, Telugu and English.</p>
        <span class="feature-tag">Your AI assistant coach</span>
      </div>
      <div class="feature-card reveal stagger-4">
        <div class="feature-icon-wrap"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/></svg></div>
        <h3>AI Plan Generator</h3>
        <p>Generate full workout or diet plans in seconds. Calorie targets calculated from each client's exact stats, dietary preference and health notes enforced, Indian food database built in.</p>
        <span class="feature-tag">Replaces manual planning</span>
      </div>
    </div>"""

new = """      <div class="feature-card reveal stagger-2">
        <div class="feature-icon-wrap"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <h3>Video Calls</h3>
        <p>Built-in video sessions via Google Meet \u2014 no Zoom, no separate links. 15 sessions/month on Verified and Certified. Unlimited on Pro. Session history tracked automatically.</p>
        <span class="feature-tag">Replaces Zoom</span>
      </div>
    </div>"""

src = src.replace(old, new, 1)

if src == orig:
    print("WARNING: anchor not found.")
else:
    open(path, "w", encoding="utf-8").write(src)
    print("Removed duplicate Iron / AI Plan Generator cards from Solution grid.")
