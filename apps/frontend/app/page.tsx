import { OfficeMap } from "@/components/office-map";

const initialMilestones = [
  "Phase 1: Monorepo + service scaffolds",
  "Phase 2: Domain entities + data mapping",
  "Phase 3: Starter API routes",
];

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-6xl flex-col gap-6 px-6 py-8 text-slate-100">
      <header className="space-y-2">
        <h1 className="text-3xl font-bold tracking-tight text-emerald-300">CollabWorld</h1>
        <p className="text-slate-200">
          Spatial work management starter implementation for the initial project phases.
        </p>
      </header>

      <OfficeMap />

      <section className="rounded-xl border border-slate-700 bg-slate-900 p-6">
        <h2 className="mb-3 text-xl font-semibold">Current implementation scope</h2>
        <ul className="list-disc space-y-1 pl-6 text-slate-200">
          {initialMilestones.map((milestone) => (
            <li key={milestone}>{milestone}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
