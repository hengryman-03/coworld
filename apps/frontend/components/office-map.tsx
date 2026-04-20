type Station = {
  id: number;
  name: string;
  meaning: string;
};

const stations: Station[] = [
  { id: 1, name: "Focus Desk", meaning: "Individual execution" },
  { id: 2, name: "Collaboration Table", meaning: "Pair or group work" },
  { id: 3, name: "Review Desk", meaning: "Approval and review" },
  { id: 4, name: "QA Desk", meaning: "Validation" },
  { id: 5, name: "Meeting Room", meaning: "Sync and planning" },
  { id: 6, name: "Delivery Desk", meaning: "Handoff and completion" },
  { id: 7, name: "Help Desk", meaning: "Blocked/support needed" },
];

export function OfficeMap() {
  // This component exists to represent the MVP office concept before movement
  // interactions are added in the next implementation phase.
  return (
    <section className="rounded-xl border border-slate-700 bg-slate-900 p-6 shadow-md">
      <h2 className="mb-4 text-xl font-semibold">Office View (MVP shell)</h2>
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {stations.map((station) => (
          <article key={station.id} className="rounded-lg border border-slate-600 bg-slate-800 p-3">
            <h3 className="font-medium text-emerald-300">{station.name}</h3>
            <p className="text-sm text-slate-200">{station.meaning}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
