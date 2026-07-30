"""
Operation Black Vault — CTFd Plugin
Automatically seeds permanent pages and configuration on every fresh setup.
This ensures the design, landing page content, and Rules of Engagement
survive any rebuild, migration, or fresh deployment on AWS / Azure / any host.
"""

import logging

from flask import Blueprint

from CTFd.models import db, Pages

log = logging.getLogger(__name__)

RULES_CONTENT = """
<div style="font-family: 'Share Tech Mono', 'Courier New', monospace;">

  <!-- Top classification banner -->
  <div style="
    background: repeating-linear-gradient(90deg, rgba(255,0,0,0.08) 0px, rgba(255,0,0,0.08) 2px, transparent 2px, transparent 20px);
    border: 1px solid rgba(255,60,60,0.4);
    padding: 10px 18px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 12px;
    color: #ff3c3c;
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
  ">
    <i class="fas fa-radiation" style="font-size:1.1rem;"></i>
    <span>TOP SECRET // OPERATOR CLEARANCE REQUIRED // OPERATION BLACK VAULT</span>
    <i class="fas fa-radiation" style="font-size:1.1rem; margin-left:auto;"></i>
  </div>

  <!-- Directives grid -->
  <div style="display:grid; gap:16px;">

    <!-- Directive 01 -->
    <div style="
      background: linear-gradient(135deg, rgba(0,229,255,0.04) 0%, rgba(0,0,0,0) 100%);
      border: 1px solid rgba(0,229,255,0.2);
      border-left: 4px solid #00e5ff;
      padding: 20px 24px;
      position: relative;
    ">
      <div style="display:flex; align-items:flex-start; gap:16px;">
        <div style="
          background: rgba(0,229,255,0.1);
          border: 1px solid rgba(0,229,255,0.4);
          color: #00e5ff;
          font-size: 1.4rem;
          width: 52px; height: 52px;
          display:flex; align-items:center; justify-content:center;
          flex-shrink: 0;
        ">
          <i class="fas fa-ban"></i>
        </div>
        <div>
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <span style="font-size:0.65rem; color:#00e5ff; letter-spacing:3px; text-transform:uppercase; opacity:0.7;">DIRECTIVE // 01</span>
          </div>
          <h3 style="color:#fff; font-size:1rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; margin:0 0 10px 0;">
            ZERO TOLERANCE
          </h3>
          <p style="color:#a0aec0; font-size:0.875rem; line-height:1.7; margin:0;">
            This is a live operational environment. Any operator caught engaging in <strong style="color:#ff6b6b;">sabotage</strong>, <strong style="color:#ff6b6b;">DDoS attacks</strong>, or <strong style="color:#ff6b6b;">automated brute-forcing</strong> against the Black Vault infrastructure will be immediately disavowed and permanently banned from the operation.
          </p>
        </div>
      </div>
    </div>

    <!-- Directive 02 -->
    <div style="
      background: linear-gradient(135deg, rgba(140,0,255,0.04) 0%, rgba(0,0,0,0) 100%);
      border: 1px solid rgba(140,0,255,0.2);
      border-left: 4px solid #8c00ff;
      padding: 20px 24px;
    ">
      <div style="display:flex; align-items:flex-start; gap:16px;">
        <div style="
          background: rgba(140,0,255,0.1);
          border: 1px solid rgba(140,0,255,0.4);
          color: #8c00ff;
          font-size: 1.4rem;
          width: 52px; height: 52px;
          display:flex; align-items:center; justify-content:center;
          flex-shrink: 0;
        ">
          <i class="fas fa-user-secret"></i>
        </div>
        <div>
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <span style="font-size:0.65rem; color:#8c00ff; letter-spacing:3px; text-transform:uppercase; opacity:0.9;">DIRECTIVE // 02</span>
          </div>
          <h3 style="color:#fff; font-size:1rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; margin:0 0 10px 0;">
            INFORMATION BLACKOUT
          </h3>
          <p style="color:#a0aec0; font-size:0.875rem; line-height:1.7; margin:0;">
            Do <strong style="color:#fff;">not</strong> share flags, intel, or solutions with rival operators or teams. Every operative must earn their clearance. Compromising mission integrity by leaking intel is a <strong style="color:#ff6b6b;">severe violation</strong> of the ROE.
          </p>
        </div>
      </div>
    </div>

    <!-- Directive 03 -->
    <div style="
      background: linear-gradient(135deg, rgba(255,170,0,0.04) 0%, rgba(0,0,0,0) 100%);
      border: 1px solid rgba(255,170,0,0.2);
      border-left: 4px solid #ffaa00;
      padding: 20px 24px;
    ">
      <div style="display:flex; align-items:flex-start; gap:16px;">
        <div style="
          background: rgba(255,170,0,0.1);
          border: 1px solid rgba(255,170,0,0.4);
          color: #ffaa00;
          font-size: 1.4rem;
          width: 52px; height: 52px;
          display:flex; align-items:center; justify-content:center;
          flex-shrink: 0;
        ">
          <i class="fas fa-bug"></i>
        </div>
        <div>
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <span style="font-size:0.65rem; color:#ffaa00; letter-spacing:3px; text-transform:uppercase; opacity:0.9;">DIRECTIVE // 03</span>
          </div>
          <h3 style="color:#fff; font-size:1rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; margin:0 0 10px 0;">
            REPORT EXPLOITS
          </h3>
          <p style="color:#a0aec0; font-size:0.875rem; line-height:1.7; margin:0;">
            If you uncover a critical vulnerability in the <strong style="color:#fff;">Black Vault platform itself</strong> (not a challenge), cease engagement immediately and report it to Command. Do <strong style="color:#ff6b6b;">not</strong> exploit the infrastructure.
          </p>
        </div>
      </div>
    </div>

    <!-- Directive 04 -->
    <div style="
      background: linear-gradient(135deg, rgba(0,255,136,0.04) 0%, rgba(0,0,0,0) 100%);
      border: 1px solid rgba(0,255,136,0.2);
      border-left: 4px solid #00ff88;
      padding: 20px 24px;
    ">
      <div style="display:flex; align-items:flex-start; gap:16px;">
        <div style="
          background: rgba(0,255,136,0.1);
          border: 1px solid rgba(0,255,136,0.4);
          color: #00ff88;
          font-size: 1.4rem;
          width: 52px; height: 52px;
          display:flex; align-items:center; justify-content:center;
          flex-shrink: 0;
        ">
          <i class="fas fa-crosshairs"></i>
        </div>
        <div>
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <span style="font-size:0.65rem; color:#00ff88; letter-spacing:3px; text-transform:uppercase; opacity:0.9;">DIRECTIVE // 04</span>
          </div>
          <h3 style="color:#fff; font-size:1rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; margin:0 0 10px 0;">
            STAY ON TARGET
          </h3>
          <p style="color:#a0aec0; font-size:0.875rem; line-height:1.7; margin:0;">
            Engage only the <strong style="color:#fff;">designated targets</strong> within the challenge scope. Out-of-bounds scanning or attacking external networks will result in <strong style="color:#ff6b6b;">immediate termination</strong>.
          </p>
        </div>
      </div>
    </div>

  </div>

  <!-- Final warning banner -->
  <div style="
    margin-top: 28px;
    background: rgba(255,0,0,0.07);
    border: 1px solid rgba(255,60,60,0.5);
    padding: 20px 24px;
    text-align: center;
  ">
    <p style="
      font-size: 1.1rem;
      font-weight: 900;
      color: #ff3c3c;
      letter-spacing: 4px;
      text-transform: uppercase;
      margin: 0 0 8px 0;
      text-shadow: 0 0 20px rgba(255,60,60,0.6);
    ">
      <i class="fas fa-skull-crossbones"></i>&nbsp;&nbsp;VIOLATORS WILL BE BURNED.&nbsp;&nbsp;<i class="fas fa-skull-crossbones"></i>
    </p>
    <p style="color:#718096; font-size:0.8rem; letter-spacing:2px; margin:0; text-transform:uppercase;">
      Read. Understood. Acknowledged. — Proceed to your objective.
    </p>
  </div>

</div>
"""


def _seed_pages():
    """Upsert permanent pages on every startup — always keeps content up to date."""
    pages_to_seed = [
        {
            "title": "Rules of Engagement",
            "route": "rules",
            "content": RULES_CONTENT,
            "format": "html",
            "draft": False,
            "hidden": False,
            "auth_required": False,
        }
    ]

    for page_data in pages_to_seed:
        existing = Pages.query.filter_by(route=page_data["route"]).first()
        if not existing:
            page = Pages(**page_data)
            db.session.add(page)
            log.info(
                f"[Operation Black Vault] Seeded page: /{page_data['route']}"
            )
        else:
            # Always update content to keep it in sync with the plugin source
            existing.content = page_data["content"]
            existing.title = page_data["title"]
            existing.format = page_data["format"]
            existing.draft = page_data["draft"]
            existing.hidden = page_data["hidden"]
            log.info(
                f"[Operation Black Vault] Updated page: /{page_data['route']}"
            )

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        log.error(f"[Operation Black Vault] Failed to seed pages: {e}")


def load(app):
    """Called by CTFd on startup. Seeds all permanent platform data."""
    blueprint = Blueprint(
        "operation_blackvault",
        __name__,
        template_folder="templates",
    )
    app.register_blueprint(blueprint)

    with app.app_context():
        _seed_pages()

    log.info("[Operation Black Vault] Plugin loaded successfully.")
