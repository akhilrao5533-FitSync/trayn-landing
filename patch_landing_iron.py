# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

# ────────────────────────────────────────────────────────────────────────────
# 1. New "Iron AI" showcase section — inserted right before "Progress tracking"
# ────────────────────────────────────────────────────────────────────────────

iron_section = """<!-- IRON AI -->
<section class="showcase" style="background:var(--bg1);">
  <div style="max-width:1100px;margin:0 auto;padding:0 24px;">
    <div class="showcase-inner">
      <div class="reveal">
        <div class="section-label" style="margin-bottom:12px;">AI coaching assistant</div>
        <h2 style="font-size:clamp(28px,4vw,44px);font-weight:700;letter-spacing:-1.5px;line-height:1.1;margin-bottom:20px;">Iron never lies.<br>Real numbers, every time.</h2>
        <p style="font-size:17px;color:var(--text2);line-height:1.7;font-weight:300;margin-bottom:32px;">Iron reads every client's full history \u2014 workouts, diet, weight, BMI, TDEE \u2014 and gives you the exact same numbers you'd see on their profile. No guessing, no spreadsheets, no separate ChatGPT tab.</p>
        <div class="feature-bullets">
          <div class="feature-bullet"><div class="feature-bullet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#818CF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div><div><div class="feature-bullet-title">Ground-truth numbers</div><div class="feature-bullet-desc">Compliance, BMI and TDEE always match what's on the client's profile</div></div></div>
          <div class="feature-bullet"><div class="feature-bullet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#818CF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div><div><div class="feature-bullet-title">One-tap actions</div><div class="feature-bullet-desc">Generate a new workout or diet, send a nudge, or draft a check-in message</div></div></div>
          <div class="feature-bullet"><div class="feature-bullet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#818CF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="feature-bullet-title">Speaks your language</div><div class="feature-bullet-desc">Hindi, Hinglish, Tamil, Telugu and English \u2014 auto-detected</div></div></div>
        </div>
      </div>
      <div class="reveal">
        <div class="phone-wrap">
          <div class="phone-showcase">
            <div class="phone-notch"></div>
            <div class="phone-body">
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
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

"""

old1 = """<section class="showcase">
  <div style="max-width:1100px;margin:0 auto;padding:0 24px;">
    <div class="showcase-inner">
      <div class="reveal">
        <div class="section-label" style="margin-bottom:12px;">Progress tracking</div>"""

new1 = iron_section + old1

src = src.replace(old1, new1, 1)

# ────────────────────────────────────────────────────────────────────────────
# 2. Two new feature-grid cards \u2014 inserted after "Video Calls" card
# ────────────────────────────────────────────────────────────────────────────

old2 = """      <div class="feature-card reveal stagger-2">
        <div class="feature-icon-wrap"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <h3>Video Calls</h3>
        <p>Built-in video sessions via Google Meet \u2014 no Zoom, no separate links. 15 sessions/month on Verified and Certified. Unlimited on Pro. Session history tracked automatically.</p>
        <span class="feature-tag">Replaces Zoom</span>
      </div>
    </div>"""

new2 = """      <div class="feature-card reveal stagger-2">
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

src = src.replace(old2, new2, 1)

if src == orig:
    print("WARNING: no changes made \u2014 anchors not found.")
else:
    open(path, "w", encoding="utf-8").write(src)
    changed1 = "WARNING" if old1 not in orig else "ok"
    changed2 = "WARNING" if old2 not in orig else "ok"
    print(f"Patched index.html. Section 1 (Iron showcase): {changed1}. Section 2 (feature cards): {changed2}.")
