import urllib.request
import ssl
import json
import re

YADISK_TOKEN = 'y0__wgBENifibMHGPSXTyCN697bGe2931gbhKuY-LYTbVLSkQayxVIy'
TILDA_MCP_KEY = 'mcp_tilda_d6de3d32d446dd2dccb5e3846e0c5aa515961c69fccc2c4a'
PROJECT_ID = 53733509
PAGE_ID = 349366209
RECORD_ID = 5576716501

# Read base landing HTML
with open('c:/Work/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read modal code from deploy_configurator.py
with open('c:/Work/deploy_configurator.py', 'r', encoding='utf-8') as f:
    cfg = f.read()

match = re.search(r'modal_code = """(.*?)"""', cfg, re.DOTALL)
if not match:
    raise ValueError("Could not find modal_code in deploy_configurator.py")

modal_code = match.group(1)

# Inject active Yandex Disk token
target_str = "window.YOOREL_YADISK_TOKEN = window.YOOREL_YADISK_TOKEN || '';"
replacement_str = f"window.YOOREL_YADISK_TOKEN = '{YADISK_TOKEN}';"

if target_str in modal_code:
    modal_code = modal_code.replace(target_str, replacement_str)
    print("Injected Yandex Disk token successfully into modal code.")
else:
    print("Warning: target_str not found in modal_code!")

bridge_script = """
<script>
// Bridge landing page buttons to the order modal
window.openOrderModalWithFormat = function(format, price) {
  var heroInput = document.getElementById('heroNameInput');
  var name = heroInput ? heroInput.value.trim() : '';
  
  var modalNameInput = document.getElementById('ybInputName');
  if (modalNameInput && name) {
    modalNameInput.value = name;
  }
  
  // Select format card in modal
  var formatCards = document.querySelectorAll('.yb-format-card');
  formatCards.forEach(function(c) {
    if (c.dataset.format === format) {
      c.click();
    }
  });
  
  // Trigger openModal
  var overlay = document.getElementById('ybModalOverlay');
  if (overlay) {
    overlay.style.display = 'flex';
    setTimeout(function() { overlay.classList.add('active'); }, 10);
    document.body.style.overflow = 'hidden';
  }
};

// Connect Top & Hero buttons to the modal
document.addEventListener('DOMContentLoaded', function() {
  var heroStart = document.getElementById('heroStartBtn');
  var topStart = document.getElementById('topOpenQuizBtn');
  
  if (heroStart) {
    heroStart.onclick = function(e) {
      e.preventDefault();
      window.openOrderModalWithFormat('print', 2990);
    };
  }
  
  if (topStart) {
    topStart.onclick = function(e) {
      e.preventDefault();
      window.openOrderModalWithFormat('print', 2990);
    };
  }
});
</script>
"""

merged_code = "<!-- YOOREL REDESIGN & CONFIGURATOR WITH YANDEX DISK INTEGRATION -->\n" + html + "\n\n" + modal_code + "\n\n" + bridge_script
print('Total merged code length:', len(merged_code))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def call_tilda(method, name, arguments):
    payload = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': method,
        'params': {
            'name': name,
            'arguments': arguments
        }
    }
    req = urllib.request.Request(
        'https://tilda.ru/api/mcp/',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TILDA_MCP_KEY}',
            'MCP-Protocol-Version': '2025-11-25'
        }
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("Updating record on Tilda...")
res1 = call_tilda('tools/call', 'update_record', {
    'pageid': PAGE_ID,
    'projectid': PROJECT_ID,
    'recordid': RECORD_ID,
    'tab': 'content',
    'fields': {
        'code': merged_code
    }
})
print("Update record result:", res1)

print("Publishing page...")
res2 = call_tilda('tools/call', 'publish_page', {
    'pageid': PAGE_ID,
    'projectid': PROJECT_ID
})
print("Publish page result:", res2)
