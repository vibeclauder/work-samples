#!/usr/bin/env python3
"""Game-audio sample pack — synthesized, loop-exact original assets.

Warehouse-rave loop is built at an exact bar grid so the WAV loops
seamlessly by construction (no crossfade needed). SFX are one-shots.
44.1 kHz / 16-bit / stereo WAVs.
"""
import numpy as np
import wave
import os

SR = 44100
OUT = os.path.dirname(os.path.abspath(__file__))


def write_wav(name, audio):
    audio = np.clip(audio, -1.0, 1.0)
    pcm = (audio * 32767).astype(np.int16)
    if pcm.ndim == 1:
        pcm = np.stack([pcm, pcm], axis=1)
    path = os.path.join(OUT, name)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"wrote {name}: {pcm.shape[0]/SR:.3f}s")


def env(n, a, d, sustain=0.0, curve=4.0):
    """Attack-decay envelope, n samples total."""
    e = np.zeros(n)
    a_n = max(1, int(a * SR))
    d_n = max(1, int(d * SR))
    e[:a_n] = np.linspace(0, 1, a_n)
    dec = np.exp(-curve * np.linspace(0, 1, d_n))
    dec = sustain + (1 - sustain) * dec
    end = min(n, a_n + d_n)
    e[a_n:end] = dec[: end - a_n]
    e[end:] = e[end - 1] if end < n else 0
    return e


def kick(dur=0.30):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 150 * np.exp(-t * 18) + 48
    phase = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(phase) * env(n, 0.001, dur, curve=6)
    click = np.random.randn(n) * env(n, 0.0005, 0.004, curve=8) * 0.4
    return (body + click) * 0.95


def hat(dur=0.06, open_=False):
    if open_:
        dur = 0.22
    n = int(dur * SR)
    noise = np.random.randn(n)
    # crude high-pass: difference filter applied twice
    for _ in range(2):
        noise = np.diff(noise, prepend=0)
    noise /= np.abs(noise).max() + 1e-9
    return noise * env(n, 0.0005, dur, curve=7) * (0.35 if open_ else 0.30)


def saw(freq, n, detune=0.0):
    t = np.arange(n) / SR
    x = np.zeros(n)
    for dt in (-detune, 0, detune):
        f = freq * (1 + dt)
        x += 2 * ((t * f) % 1.0) - 1.0
    return x / 3


def lowpass(x, cutoff):
    """One-pole lowpass, cheap and cheerful."""
    alpha = 1 - np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += alpha * (v - acc)
        y[i] = acc
    return y


def warehouse_loop(bpm=126, bars=8):
    beat = 60.0 / bpm
    bar = 4 * beat
    total_n = int(round(bars * bar * SR))
    mix = np.zeros(total_n)

    def add(sound, at_s, gain=1.0):
        i = int(round(at_s * SR)) % total_n
        s = sound * gain
        end = i + len(s)
        if end <= total_n:
            mix[i:end] += s
        else:  # wrap over the loop point — keeps the loop seamless
            k = total_n - i
            mix[i:] += s[:k]
            mix[: end - total_n] += s[k:]

    k = kick()
    ch = hat()
    oh = hat(open_=True)

    # A-minor-ish techno: A1 bass root, stab Am add9 voicing
    bass_freq = 55.0
    for b in range(bars):
        for q in range(4):
            t0 = b * bar + q * beat
            add(k, t0)                       # four on the floor
            add(oh, t0 + beat / 2, 0.8)      # offbeat open hat
            for s16 in range(4):             # 16th closed hats
                add(ch, t0 + s16 * beat / 4, 0.5 if s16 % 2 else 0.7)
            # rolling eighth bass, ducked on the beat
            for e8, gain in ((beat * 0.5, 0.9), (beat * 0.75, 0.6)):
                n = int(beat * 0.22 * SR)
                bnote = lowpass(saw(bass_freq, n, 0.004), 300) * env(n, 0.004, 0.2, curve=5)
                add(bnote, t0 + e8, gain * 0.8)
        # dark stab on the "and" of 2 and 4, every other bar
        if b % 2 == 1:
            for pos in (1.5 * beat, 3.5 * beat):
                n = int(0.18 * SR)
                st = sum(lowpass(saw(f, n, 0.006), 900) for f in (220.0, 261.63, 329.63))
                st = st / 3 * env(n, 0.002, 0.18, curve=6)
                add(st, b * bar + pos, 0.55)
    # 4-bar noise riser into the loop point (ends exactly at wrap)
    rise_n = int(2 * bar * SR)
    noise = np.random.randn(rise_n)
    for _ in range(2):
        noise = np.diff(noise, prepend=0)
    noise /= np.abs(noise).max() + 1e-9
    riser = noise * np.linspace(0, 1, rise_n) ** 2 * 0.10
    add(riser, (bars - 2) * bar)

    mix /= np.abs(mix).max() + 1e-9
    mix *= 0.9
    # gentle stereo: hats slightly wider via 0.6ms haas on right
    delay = int(0.0006 * SR)
    right = np.roll(mix, delay)
    return np.stack([mix, right], axis=1)


def ui_click():
    n = int(0.045 * SR)
    t = np.arange(n) / SR
    tone = np.sin(2 * np.pi * 1800 * t) * env(n, 0.0005, 0.04, curve=8)
    tick = np.random.randn(n) * env(n, 0.0003, 0.006, curve=9) * 0.3
    return (tone * 0.7 + tick) * 0.8


def cash_register():
    # bell ding (coincident partials) + low mechanical thunk
    n = int(0.5 * SR)
    t = np.arange(n) / SR
    bell = sum(np.sin(2 * np.pi * f * t) * a for f, a in
               ((2093, 0.5), (2637, 0.35), (3520, 0.2)))
    bell *= env(n, 0.001, 0.45, curve=5)
    thunk_n = int(0.09 * SR)
    tt = np.arange(thunk_n) / SR
    thunk = np.sin(2 * np.pi * (90 * np.exp(-tt * 25) + 55) * tt) * env(thunk_n, 0.001, 0.09, curve=6)
    out = bell * 0.6
    out[:thunk_n] += thunk * 0.9
    # second softer ding, 120ms later (classic "ka-ching")
    d2 = int(0.12 * SR)
    out[d2:] += (bell[: n - d2]) * 0.35
    return out * 0.85


def level_up():
    # rising A-major arpeggio with sparkle
    notes = [440.0, 554.37, 659.25, 880.0]
    step = 0.11
    n = int((len(notes) * step + 0.5) * SR)
    out = np.zeros(n)
    for i, f in enumerate(notes):
        nn = int(0.4 * SR)
        t = np.arange(nn) / SR
        tone = (np.sin(2 * np.pi * f * t) * 0.6 +
                np.sin(2 * np.pi * f * 2 * t) * 0.25 +
                np.sin(2 * np.pi * f * 3 * t) * 0.1)
        tone *= env(nn, 0.004, 0.38, curve=4.5)
        i0 = int(i * step * SR)
        out[i0:i0 + nn] += tone * (0.5 + 0.12 * i)
    out /= np.abs(out).max() + 1e-9
    return out * 0.85


if __name__ == "__main__":
    np.random.seed(2026)
    write_wav("warehouse_rave_loop_126bpm.wav", warehouse_loop())
    write_wav("ui_click.wav", ui_click())
    write_wav("cash_register.wav", cash_register())
    write_wav("level_up.wav", level_up())
