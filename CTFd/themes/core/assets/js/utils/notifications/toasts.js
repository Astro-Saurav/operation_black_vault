import Alpine from "alpinejs";
import { Toast } from "bootstrap";
import CTFd from "../../index";

export default () => {
  Alpine.store("toast", { title: "", html: "" });

  CTFd._functions.events.eventToast = data => {
    Alpine.store("toast", data);
    let toast = new Toast(document.querySelector("[x-ref='toast']"));
    // TODO: Get rid of this private attribute access
    // See https://github.com/twbs/bootstrap/issues/31266
    let close = toast._element.querySelector("[data-bs-dismiss='toast']");
    let handler = event => {
      CTFd._functions.events.eventRead(data.id);
    };
    close.addEventListener("click", handler, { once: true });
    toast._element.addEventListener(
      "hidden.bs.toast",
      event => {
        close.removeEventListener("click", handler);
      },
      { once: true },
    );

    // --- OBV ALARM MOD ---
    // Flash the screen red
    let alarmOverlay = document.createElement("div");
    alarmOverlay.style.position = "fixed";
    alarmOverlay.style.top = "0";
    alarmOverlay.style.left = "0";
    alarmOverlay.style.width = "100vw";
    alarmOverlay.style.height = "100vh";
    alarmOverlay.style.pointerEvents = "none";
    alarmOverlay.style.zIndex = "9999";
    alarmOverlay.style.backgroundColor = "rgba(255,0,0,0.3)";
    alarmOverlay.style.animation = "obv-alarm-blink 0.5s infinite alternate";
    
    if (!document.getElementById("obv-alarm-style")) {
      let style = document.createElement("style");
      style.id = "obv-alarm-style";
      style.innerHTML = "@keyframes obv-alarm-blink { 0% { opacity: 0; } 100% { opacity: 1; } }";
      document.head.appendChild(style);
    }
    
    document.body.appendChild(alarmOverlay);

    // Play Klaxon Sound using Web Audio API
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        const actx = new AudioContext();
        const osc = actx.createOscillator();
        const gain = actx.createGain();
        osc.type = "square";
        
        // Klaxon siren effect
        osc.frequency.setValueAtTime(600, actx.currentTime);
        osc.frequency.linearRampToValueAtTime(400, actx.currentTime + 0.4);
        osc.frequency.setValueAtTime(600, actx.currentTime + 0.4);
        osc.frequency.linearRampToValueAtTime(400, actx.currentTime + 0.8);
        osc.frequency.setValueAtTime(600, actx.currentTime + 0.8);
        osc.frequency.linearRampToValueAtTime(400, actx.currentTime + 1.2);
        osc.frequency.setValueAtTime(600, actx.currentTime + 1.2);
        osc.frequency.linearRampToValueAtTime(400, actx.currentTime + 1.6);
        osc.frequency.setValueAtTime(600, actx.currentTime + 1.6);
        osc.frequency.linearRampToValueAtTime(400, actx.currentTime + 2.0);

        osc.connect(gain);
        gain.connect(actx.destination);
        gain.gain.setValueAtTime(0.1, actx.currentTime);
        osc.start();
        setTimeout(() => { osc.stop(); }, 2000);
      }
    } catch (e) {
      console.log("Audio not supported or blocked by browser.");
    }
    
    // Remove alarm visual after 3 seconds
    setTimeout(() => {
      if (document.body.contains(alarmOverlay)) {
        document.body.removeChild(alarmOverlay);
      }
    }, 3000);
    // -------------------

    toast.show();
  };
};
