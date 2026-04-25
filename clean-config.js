const fs = require('fs');
const path = require('path');

function cleanJsonFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    let json = JSON.parse(data);
    let changed = false;

    function cleanObj(obj) {
      if (typeof obj !== 'object' || obj === null) return;
      
      const keysToRemove = ['autoAccept', 'confirm', 'allowAll', 'fallback'];
      for (const key of keysToRemove) {
        if (key in obj) {
          delete obj[key];
          changed = true;
        }
      }
      
      // Keep searching recursively
      for (const k in obj) {
        cleanObj(obj[k]);
      }
    }

    cleanObj(json);

    if (changed) {
      fs.writeFileSync(filePath, JSON.stringify(json, null, 2));
      console.log(`Cleaned ${filePath}`);
    }
  } catch (e) {
    // Ignore parse errors, maybe it's not pure JSON or not an object
  }
}

function walkDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      walkDir(fullPath);
    } else if (fullPath.endsWith('.json')) {
      cleanJsonFile(fullPath);
    }
  }
}

// Clean global config
walkDir('/Users/jeremy/.config/opencode');
console.log('Done cleaning global config.');
