# -*- coding: utf-8 -*-
path = "index.html"
src = open(path, encoding="utf-8").read()
orig = src

# ── Card 1: Iron chat mockup ────────────────────────────────────────────────
old1 = """<p>Ask about any client \u2014 compliance, BMI, TDEE, diet alignment, weight trend \u2014 and Iron answers with the same numbers on their profile. It can even draft a nudge or check-in message for you to send.</p>"""

new1 = old1 + """
        <div style="background:#08090B;border:1px solid var(--border2);border-radius:10px;padding:10px;margin-top:14px;">
          <div style="display:flex;justify-content:flex-end;margin-bottom:6px;"><div style="background:#3d4dff;border-radius:8px 8px 2px 8px;padding:5px 9px;"><span style="font-size:9px;color:#fff;font-weight:600;">Her compliance?</span></div></div>
          <div style="font-size:8.5px;color:#C7C7D1;line-height:1.5;margin-bottom:6px;">Only 3/12 workouts done in 30 days (25%). Last session incomplete.</div>
          <div style="background:#15171C;border-radius:6px;padding:5px 8px;display:flex;justify-content:space-between;align-items:center;"><span style="font-size:8px;color:#9CA3AF;">Compliance (30d)</span><span style="font-size:8.5px;font-weight:800;color:#F87171;">25% (3/12)</span></div>
        </div>"""

src = src.replace(old1, new1, 1)

# ── Card 2: AI diet plan mockup ──────────────────────────────────────────────
old2 = """<p>Describe what you want \u2014 "high protein bulk" or "1800 cal cut" \u2014 and Iron drafts a full Indian meal plan at the exact calorie target for that client, respecting their dietary preference. You review and assign.</p>"""

new2 = old2 + """
        <div style="background:#08090B;border:1px solid var(--border2);border-radius:10px;padding:10px;margin-top:14px;">
          <div style="font-size:9px;font-weight:700;color:#F4F4F5;margin-bottom:6px;">South Indian Thali Bulk Plan \u00b7 2592 kcal</div>
          <div style="display:flex;flex-direction:column;gap:4px;">
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Breakfast \u00b7 Idli (4), Sambar</span><span style="font-size:7.5px;color:#6B7280;">420 kcal</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Lunch \u00b7 Rice, Dal, Chicken</span><span style="font-size:7.5px;color:#6B7280;">680 kcal</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Dinner \u00b7 Roti (3), Paneer</span><span style="font-size:7.5px;color:#6B7280;">590 kcal</span></div>
          </div>
        </div>"""

src = src.replace(old2, new2, 1)

# ── Card 3: AI workout plan mockup ───────────────────────────────────────────
old3 = """<p>Type "leg day, intermediate" and Iron pulls a complete session \u2014 sets, reps, rest times \u2014 from your exercise library, matched to the client's level. Tweak anything before it's assigned.</p>"""

new3 = old3 + """
        <div style="background:#08090B;border:1px solid var(--border2);border-radius:10px;padding:10px;margin-top:14px;">
          <div style="font-size:9px;font-weight:700;color:#F4F4F5;margin-bottom:6px;">Leg Day \u00b7 Intermediate</div>
          <div style="display:flex;flex-direction:column;gap:4px;">
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Barbell Squat</span><span style="font-size:7.5px;color:#818cf8;font-weight:700;">4 \u00d7 10</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Leg Press</span><span style="font-size:7.5px;color:#818cf8;font-weight:700;">3 \u00d7 12</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;background:#15171C;border-radius:6px;padding:5px 8px;"><span style="font-size:8px;color:#E5E7EB;">Walking Lunges</span><span style="font-size:7.5px;color:#818cf8;font-weight:700;">3 \u00d7 12</span></div>
          </div>
        </div>"""

src = src.replace(old3, new3, 1)

if src == orig:
    print("WARNING: no changes made.")
else:
    open(path, "w", encoding="utf-8").write(src)
    c1 = "ok" if old1 in orig else "MISS"
    c2 = "ok" if old2 in orig else "MISS"
    c3 = "ok" if old3 in orig else "MISS"
    print(f"Patched. Card 1: {c1}, Card 2: {c2}, Card 3: {c3}")
