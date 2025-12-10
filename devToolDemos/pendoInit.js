console.log("pendoInit.js module evaluated");

export function initPendo(user) {
  console.log("initPendo() called with", user);

  if (!window.pendo) {
    console.warn("❌ Pendo not available");
    return;
  }

  window.pendo.initialize({
    apiKey: "demo-api-key-123",
    visitor: { id: user.id, email: user.email },
    account: { id: user.org.toLowerCase().replace(" ", "-"), name: user.org },
  });
}
