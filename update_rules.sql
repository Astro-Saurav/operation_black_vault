UPDATE pages 
SET hidden = 1,
    content = '<h3 class="obv-text-primary"><i class="fas fa-exclamation-triangle"></i> TACTICAL DIRECTIVE 01: ZERO TOLERANCE</h3>
<p>This is a live operational environment. Any operator caught engaging in sabotage, DDoS attacks, or automated brute-forcing against the Black Vault infrastructure will be immediately disavowed and permanently banned from the operation.</p>

<h3 class="obv-text-primary"><i class="fas fa-handshake"></i> TACTICAL DIRECTIVE 02: INFORMATION BLACKOUT</h3>
<p>Do not share flags, intel, or solutions with rival operators or teams. Every operative must earn their clearance. Compromising mission integrity by leaking intel is a severe violation of the ROE.</p>

<h3 class="obv-text-primary"><i class="fas fa-bug"></i> TACTICAL DIRECTIVE 03: REPORT EXPLOITS</h3>
<p>If you uncover a critical vulnerability in the Black Vault platform itself (not a challenge), cease engagement immediately and report it to Command. Do not exploit the infrastructure.</p>

<h3 class="obv-text-primary"><i class="fas fa-shield-alt"></i> TACTICAL DIRECTIVE 04: STAY ON TARGET</h3>
<p>Engage only the designated targets within the challenge scope. Out-of-bounds scanning or attacking external networks will result in immediate termination.</p>

<p class="obv-text-danger obv-glitch mt-5" data-text="VIOLATORS WILL BE BURNED."><strong>VIOLATORS WILL BE BURNED.</strong></p>
<p><strong>Acknowledge and proceed.</strong></p>'
WHERE route = 'rules';
