console.log("app.js loaded");

document.getElementById("analyticsBtn").addEventListener("click", async () => {
  console.log("Analytics button clicked");

  // Lazy-load the analytics module
  const analyticsModule = await import("./analytics.js");
  analyticsModule.startAnalytics();
});