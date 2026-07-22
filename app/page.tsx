const linkClass =
  'inline-flex items-center gap-1.5 rounded-sm font-medium text-sky-400 underline decoration-sky-400/40 underline-offset-4 transition-colors hover:text-sky-300 hover:decoration-sky-300 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-sky-400';

const audioSamples = [
  { label: 'Club loop — 126 BPM', src: 'media/club_loop_126bpm.wav' },
  { label: 'UI click', src: 'media/ui_click.wav' },
  { label: 'Cash register', src: 'media/cash_register.wav' },
  { label: 'Level up', src: 'media/level_up.wav' },
];

const capabilities = [
  'Agent operations — durable handoffs, progress detection, restart boundaries, audit ledgers, and human checkpoints for long-running coding agents',
  'Agent reliability — offline log triage for silent failures, dead-end runs, retry storms, tool-contract errors, loops, latency tails, and duplicate side effects',
  'Workflow reliability — local n8n export analysis, secret-hygiene checks, retry/error-path review, and prioritized remediation',
  'Programmatic video — Python, Pillow, and FFmpeg pipelines for typography-driven motion pieces, delivered as H.264/AAC',
  'Audio synthesis — NumPy DSP for music loops and UI sound effects, delivered as WAV',
  'Web — Next.js, React, TypeScript, and Tailwind CSS; static sites deployed on GitHub Pages',
  'Automation — scripted, repeatable media-processing and build pipelines',
];

export default function Home() {
  return (
    <div className="mx-auto max-w-6xl px-5 sm:px-8">
      <header className="border-b border-zinc-800 py-14 sm:py-20">
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-50 sm:text-4xl">
          William Bradway
        </h1>
        <p className="mt-3 text-lg text-zinc-400">
          Work samples — AI implementation, programmatic media &amp; web
        </p>
        <p className="mt-6 max-w-3xl text-base leading-relaxed text-zinc-300">
          Everything below is an original system, spec sample, or shipped public
          site. No client case studies are shown.
        </p>
      </header>

      <main>
        <section
          aria-labelledby="agent-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-emerald-400 uppercase">
            AI implementation
          </p>
          <h2
            id="agent-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Agent Continuity Kit
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-zinc-300">
            A reference implementation for a costly operational failure: an
            unattended coding-agent loop looked alive while making no material
            progress. The kit separates process liveness from useful output,
            preserves structured context across restarts, and keeps commercial
            activity distinct from settled revenue.
          </p>

          <div className="mt-8 grid max-w-5xl gap-4 sm:grid-cols-3">
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Failure addressed
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Silent stalls, context loss, duplicate work, and ambiguous
                progress during long-running agent sessions.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Controls built
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Handoff validation, watchdog recovery, stall quarantine,
                explicit stop control, and append-only audit history.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Verification
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Four end-to-end test files with 26 passing checks, including
                failure simulations and strict revenue-state validation.
              </p>
            </article>
          </div>

          <p className="mt-6 flex flex-wrap gap-x-8 gap-y-2">
            <a
              href="https://github.com/vibeclauder/flagship-agent-continuity"
              className={linkClass}
            >
              Source, architecture &amp; tests
            </a>
          </p>
        </section>

        <section
          aria-labelledby="n8n-audit-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-emerald-400 uppercase">
            Workflow reliability
          </p>
          <h2
            id="n8n-audit-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            n8n Reliability Audit
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-zinc-300">
            A dependency-free CLI that audits sanitized n8n workflow exports
            locally. It identifies embedded-secret risk, missing error
            workflows, disconnected nodes, brittle retry behavior, coupled
            webhook acknowledgements, and handoff ambiguity—without uploading
            the workflow or reproducing parameter values in its report.
          </p>

          <div className="mt-8 grid max-w-5xl gap-4 sm:grid-cols-3">
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Privacy boundary
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Runs locally, makes no network requests, and reports finding
                metadata rather than workflow values or credential contents.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Actionable output
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Markdown and JSON scorecards include evidence, severity, a
                recommended fix, and a SHA-256 source fingerprint.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Verification
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Four automated tests cover risky and hardened workflows,
                multi-workflow exports, invalid input, and secret redaction.
              </p>
            </article>
          </div>

          <p className="mt-6 flex flex-wrap gap-x-8 gap-y-2">
            <a
              href="https://github.com/vibeclauder/n8n-reliability-audit"
              className={linkClass}
            >
              Source, sample report &amp; fixed-price review
            </a>
          </p>
        </section>

        <section
          aria-labelledby="agent-triage-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-emerald-400 uppercase">
            Agent reliability
          </p>
          <h2
            id="agent-triage-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Agent Reliability Triage
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-zinc-300">
            An offline, dependency-free CLI that turns JSONL or JSON agent logs
            into an evidence-backed reliability brief. It separates observed
            defects from instrumentation gaps, maps each finding to a concrete
            fix, and gives before/after remediation work a reproducible baseline.
          </p>

          <div className="mt-8 grid max-w-5xl gap-4 sm:grid-cols-3">
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Failure taxonomy
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Detects 11 operational failure classes, including silent
                successes, dead-end runs, retry storms, repeated tool calls,
                truncation, and duplicate outbound actions.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Safe evidence
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                Runs without network access, reports missing telemetry instead
                of guessing, and redacts common credential shapes from Markdown
                evidence excerpts by default.
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-5">
              <p className="text-xs font-medium tracking-widest text-zinc-500 uppercase">
                Verification
              </p>
              <p className="mt-3 leading-relaxed text-zinc-200">
                44 end-to-end assertions exercise the real CLI across known-bad
                logs, a clean baseline, alternate field names, malformed input,
                report safety, and CI exit behavior.
              </p>
            </article>
          </div>

          <p className="mt-6 flex flex-wrap gap-x-8 gap-y-2">
            <a
              href="https://github.com/vibeclauder/agent-reliability-triage"
              className={linkClass}
            >
              Source, sample report &amp; bounded review options
            </a>
          </p>
        </section>

        <section
          aria-labelledby="video-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-zinc-500 uppercase">
            Video
          </p>
          <h2
            id="video-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Course-trailer motion piece (spec sample)
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-zinc-300">
            A 35-second trailer-style piece produced end-to-end with an original
            programmatic workflow — Python, Pillow, and FFmpeg: code-driven
            typography and panels, an original synthesized music bed, and
            beat-synced cuts. Built as a spec demonstration of the workflow; not
            client work.
          </p>
          <video
            controls
            preload="metadata"
            width={1280}
            height={720}
            src="media/course-trailer-spec.mp4"
            aria-label="Course-trailer motion piece, spec sample video"
            className="mt-8 w-full max-w-4xl rounded-lg border border-zinc-800 bg-black"
          />
          <p className="mt-6">
            <a href="source/build_spec.py" className={linkClass}>
              View the build script
            </a>
          </p>
        </section>

        <section
          aria-labelledby="audio-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-zinc-500 uppercase">
            Audio
          </p>
          <h2
            id="audio-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Game-audio sample pack (original, synthesized)
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-zinc-300">
            Four original game-ready assets synthesized in code with Python and
            NumPy, delivered as WAV: a 126 BPM club-style music loop built on an
            exact bar grid so it loops cleanly, plus three UI sound effects.
          </p>
          <ul className="mt-8 grid max-w-4xl gap-4 sm:grid-cols-2">
            {audioSamples.map((sample) => (
              <li
                key={sample.src}
                className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-4"
              >
                <p className="mb-3 text-sm font-medium text-zinc-200">
                  {sample.label}
                </p>
                <audio
                  controls
                  preload="none"
                  src={sample.src}
                  aria-label={sample.label}
                  className="w-full"
                />
              </li>
            ))}
          </ul>
          <p className="mt-6 flex flex-wrap gap-x-8 gap-y-2">
            <a href="media/game-audio-sample-pack.zip" className={linkClass}>
              Download the pack (ZIP)
            </a>
            <a href="source/synth.py" className={linkClass}>
              View the synth script
            </a>
          </p>
        </section>

        <section
          aria-labelledby="web-heading"
          className="border-b border-zinc-800 py-14 sm:py-16"
        >
          <p className="text-sm font-medium tracking-widest text-zinc-500 uppercase">
            Web
          </p>
          <h2
            id="web-heading"
            className="mt-2 text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Shipped sites
          </h2>
          <div className="mt-8 grid max-w-4xl gap-6 sm:grid-cols-2">
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-6">
              <h3 className="text-lg font-semibold text-zinc-100">
                HeatSafe — cinematic pitch site
              </h3>
              <p className="mt-3 leading-relaxed text-zinc-300">
                A single-page cinematic pitch site, live on GitHub Pages.
              </p>
              <p className="mt-5 flex flex-wrap gap-x-6 gap-y-2">
                <a
                  href="https://vibeclauder.github.io/heatsafe/"
                  className={linkClass}
                >
                  Live site
                </a>
                <a
                  href="https://github.com/vibeclauder/heatsafe"
                  className={linkClass}
                >
                  Source
                </a>
              </p>
            </article>
            <article className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-6">
              <h3 className="text-lg font-semibold text-zinc-100">
                Operations dashboard (private)
              </h3>
              <p className="mt-3 leading-relaxed text-zinc-300">
                A live-updating operations dashboard built with Next.js, React,
                and Tailwind CSS. Private deployment; walkthrough available on
                request.
              </p>
            </article>
          </div>
        </section>

        <section
          aria-labelledby="capabilities-heading"
          className="py-14 sm:py-16"
        >
          <h2
            id="capabilities-heading"
            className="text-2xl font-semibold tracking-tight text-zinc-50"
          >
            Capabilities
          </h2>
          <ul className="mt-6 max-w-3xl list-disc space-y-3 pl-5 leading-relaxed text-zinc-300 marker:text-zinc-600">
            {capabilities.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </section>
      </main>

      <footer className="border-t border-zinc-800 py-10">
        <p className="text-sm text-zinc-500">
          All samples on this page are original work produced with the systems
          and workflows described. &copy; 2026 William Bradway
        </p>
      </footer>
    </div>
  );
}
