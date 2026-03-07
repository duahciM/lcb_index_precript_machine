const screen = document.getElementById("screen");
const generateBtn = document.getElementById("generateBtn");

generateBtn.addEventListener("click", async () => {
  screen.textContent = "接收中...";
  try {
    const res = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ mode: "ritual" })
    });

    const data = await res.json();
    screen.textContent = data.prescript;
  } catch (err) {
    screen.textContent = "信号中断。";
  }
});