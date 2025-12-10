console.log("app.js loaded");document.getElementById("analyticsBtn").addEventListener("click",async()=>{console.log("Analytics button clicked");(await import("./analytics.js")).startAnalytics()});
