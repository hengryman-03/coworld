/**
 * Shared workflow types for future frontend/backend contract alignment.
 * This package exists early so the monorepo has a dedicated boundary for
 * reusable domain vocabulary.
 */
export type StationType =
  | "focus"
  | "collaboration"
  | "review"
  | "qa"
  | "meeting"
  | "delivery"
  | "help";
