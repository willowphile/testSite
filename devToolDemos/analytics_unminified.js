console.log("analytics.js parsed (ready but not yet executed)");

import { beginTracking } from "./tracker.js";

export function startAnalytics() {
  console.log("startAnalytics() called");

  const user = { id: 42, email: "demo@pendo.io" };

  // Pretend this check is route- or permission-based
  if (user && user.id) {
    console.log("Conditions met. Calling beginTracking()...");
    beginTracking(user);
  } else {
    console.log("Conditions not met. Skipping tracking.");
  }
}