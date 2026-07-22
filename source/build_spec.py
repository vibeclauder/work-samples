#!/usr/bin/env python3
"""Course-trailer spec sample — 100% original, rights-clean assets.

~35s, 1280x720@24fps. All assets generated here: kinetic typography over
animated gradient panels, plus an original synthesized underscore (soft
four-on-floor at 100 BPM with warm pads). Beat-synced cuts.
"""
import numpy as np
import os, wave, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SR = 44100
FPS = 24
W, H = 1280, 720
BPM = 100.0
BEAT = 60.0 / BPM
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- audio: soft underscore ----------

def env(n, a, d, curve=4.0):
    e = np.zeros(n)
    a_n = max(1, int(a * SR)); d_n = max(1, int(d * SR))
    e[:a_n] = np.linspace(0, 1, a_n)
    dec = np.exp(-curve * np.linspace(0, 1, d_n))
    end = min(n, a_n + d_n)
    e[a_n:end] = dec[:end - a_n]
    return e

def build_underscore(bars=15):
    bar = 4 * BEAT
    total_n = int(round(bars * bar * SR))
    mix = np.zeros(total_n)

    def add(s, at_s, g=1.0):
        i = int(round(at_s * SR))
        if i >= total_n: return
        s = s * g
        end = min(total_n, i + len(s))
        mix[i:end] += s[:end - i]

    # soft kick
    kn = int(0.25 * SR); t = np.arange(kn) / SR
    f = 120 * np.exp(-t * 20) + 45
    kick = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(kn, 0.002, 0.25, 5) * 0.5
    # warm pad chords: Cmaj7 -> Am9 -> Fmaj7 -> G6, one per bar, cycling
    chords = [[261.63, 329.63, 392.0, 493.88],
              [220.0, 261.63, 329.63, 493.88],
              [174.61, 220.0, 261.63, 329.63],
              [196.0, 246.94, 293.66, 329.63]]
    pn = int(bar * 1.05 * SR); tp = np.arange(pn) / SR
    fade = np.minimum(1, np.minimum(tp / 0.8, (pn / SR - tp) / 0.8))
    for b in range(bars):
        add(kick * (0.0 if b < 2 else 1.0), b * bar)          # pads only, first 2 bars
        add(kick * (0.0 if b < 2 else 0.9), b * bar + 2 * BEAT)
        ch = chords[b % 4]
        pad = sum(np.sin(2 * np.pi * fr * tp) * (0.8 - 0.12 * i) +
                  0.3 * np.sin(2 * np.pi * fr * 2 * tp + 0.5)
                  for i, fr in enumerate(ch)) / len(ch)
        # slow chorus shimmer
        pad *= (1 + 0.15 * np.sin(2 * np.pi * 0.7 * tp))
        add(pad * fade, b * bar, 0.22)
        # light hat on offbeats from bar 4
        if b >= 4:
            hn = int(0.05 * SR)
            noise = np.diff(np.random.randn(hn + 1))
            noise /= np.abs(noise).max() + 1e-9
            hat = noise * env(hn, 0.0005, 0.05, 7)
            for q in range(4):
                add(hat, b * bar + q * BEAT + BEAT / 2, 0.12)
    # final chord ring-out, then gentle master fade tail
    mix /= np.abs(mix).max() + 1e-9
    fade_n = int(2.0 * SR)
    mix[-fade_n:] *= np.linspace(1, 0, fade_n)
    return (mix * 0.85)

def write_wav(path, audio):
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)
    pcm = np.stack([pcm, pcm], axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())

# ---------- video: kinetic typography ----------

def find_font(bold=False):
    cands = (["/System/Library/Fonts/Helvetica.ttc",
              "/System/Library/Fonts/HelveticaNeue.ttc",
              "/System/Library/Fonts/SFNS.ttf",
              "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf"])
    for c in cands:
        if os.path.exists(c):
            return c
    return None

FONT_PATH = find_font()

def font(sz, bold=False):
    try:
        # Helvetica.ttc index 1 is Bold
        return ImageFont.truetype(FONT_PATH, sz, index=1 if bold else 0)
    except Exception:
        return ImageFont.truetype(FONT_PATH, sz)

def ease_out(t): return 1 - (1 - t) ** 3
def clamp(t): return max(0.0, min(1.0, t))

# scene copy — all original spec text, no real brand
SCENES = [
    (0.0,  4.0,  "grad", "You know your craft.", ""),
    (4.0,  8.0,  "grad", "Teaching it online", "is a different skill."),
    (8.0,  13.0, "panel", "A premium course needs", "structure · pacing · polish"),
    (13.0, 18.0, "panel", "Lesson edits that hold attention", "clean cuts · captions · consistent sound"),
    (18.0, 23.0, "panel", "Trailers that sell the transformation", "not just the table of contents"),
    (23.0, 28.0, "grad", "Built fast. Built clean.", "every platform, every aspect ratio"),
    (28.0, 34.5, "end",  "SPEC SAMPLE", "original assets · programmatic pipeline · 2026"),
]

BG_A = np.array([16, 18, 34]); BG_B = np.array([44, 24, 64])
ACCENT = (118, 255, 209)

def render_frame(tsec):
    # animated diagonal gradient
    yy, xx = np.mgrid[0:H, 0:W]
    ph = 0.5 + 0.5 * np.sin(2 * np.pi * (xx / W * 0.7 + yy / H * 0.3) - tsec * 0.35)
    img_arr = (BG_A[None, None, :] * (1 - ph[..., None]) + BG_B[None, None, :] * ph[..., None]).astype(np.uint8)
    img = Image.fromarray(img_arr, "RGB")
    draw = ImageDraw.Draw(img, "RGBA")

    # beat pulse bar at bottom (shows beat-sync)
    beat_phase = (tsec / BEAT) % 1.0
    pulse = max(0.0, 1 - beat_phase * 3)
    bw = int(W * 0.25 + W * 0.1 * pulse)
    draw.rectangle([(W - bw) // 2, H - 26, (W + bw) // 2, H - 20],
                   fill=(ACCENT[0], ACCENT[1], ACCENT[2], int(90 + 120 * pulse)))

    for (t0, t1, kind, line1, line2) in SCENES:
        if not (t0 <= tsec < t1 + 0.4):
            continue
        p_in = clamp((tsec - t0) / 0.6)
        p_out = clamp((t1 + 0.4 - tsec) / 0.4)
        alpha = int(255 * ease_out(p_in) * min(1.0, p_out))
        rise = int(30 * (1 - ease_out(p_in)))
        if kind == "panel":
            pw = int(W * 0.78 * ease_out(clamp((tsec - t0) / 0.45)))
            draw.rectangle([(W - pw) // 2, H // 2 - 110, (W + pw) // 2, H // 2 + 110],
                           fill=(255, 255, 255, int(14 * (alpha / 255))),
                           outline=(ACCENT[0], ACCENT[1], ACCENT[2], alpha // 2), width=2)
        f1 = font(64 if kind != "end" else 76, bold=True)
        f2 = font(30)
        w1 = draw.textlength(line1, font=f1)
        col1 = ACCENT if kind == "end" else (240, 240, 250)
        draw.text(((W - w1) / 2, H / 2 - 70 + rise), line1,
                  font=f1, fill=(col1[0], col1[1], col1[2], alpha))
        if line2:
            w2 = draw.textlength(line2, font=f2)
            draw.text(((W - w2) / 2, H / 2 + 24 + rise), line2,
                      font=f2, fill=(ACCENT[0], ACCENT[1], ACCENT[2], alpha))
    # subtle vignette
    return img

def main():
    np.random.seed(7)
    dur = 35.0
    audio = build_underscore(bars=15)  # 15 bars @100bpm = 36s, faded tail
    audio = audio[: int(dur * SR)]
    wav_path = os.path.join(OUT, "underscore.wav")
    write_wav(wav_path, audio)
    print("audio written:", len(audio) / SR, "s")

    import imageio
    silent_path = os.path.join(OUT, "spec_silent.mp4")
    wr = imageio.get_writer(silent_path, fps=FPS, codec="libx264",
                            output_params=["-crf", "20", "-pix_fmt", "yuv420p"])
    n_frames = int(dur * FPS)
    for i in range(n_frames):
        wr.append_data(np.asarray(render_frame(i / FPS)))
        if i % 120 == 0:
            print(f"frame {i}/{n_frames}", file=sys.stderr)
    wr.close()
    print("silent video written")

    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    final = os.path.join(OUT, "course_trailer_spec.mp4")
    subprocess.run([ff, "-y", "-i", silent_path, "-i", wav_path,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", final], check=True, capture_output=True)
    os.remove(silent_path)
    print("final:", final)

if __name__ == "__main__":
    main()
