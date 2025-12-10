console.log("tracker.js module evaluated");

import { initPendo } from "./pendoInit.js";

export function beginTracking(user) {
  console.log("beginTracking() called");

  // Pretend to do some preprocessing before initializing Pendo
  const enrichedUser = {
    ...user,
    plan: "Pro",
    org: "Example Co",
  };

  console.log("Passing enriched user to initPendo()");
  initPendo(enrichedUser);
}
