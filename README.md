## AcidLog
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)
![Status](https://img.shields.io/badge/Status-Beta-orange.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)





AcidLog is a sophisticated real-time security monitoring and visualization tool designed for cybersecurity professionals. It provides an intuitive interface for tracking, analyzing, and responding to security events in real-time.
<p align="center">
<img width="307" height="307" alt="acidlog"  src="https://github.com/user-attachments/assets/42eb4b5b-7633-4eae-a342-0605696032c1" />
</p>

## 📚 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Example](#-usage-example)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 📄 Introduction

AcidLog transforms raw security logs into actionable intelligence through real-time visualization, pattern detection, and intelligent alerting. Its modular architecture and extensive customization options make it suitable for SOCs, penetration testers, and security researchers.

## 🌟 Features

- **Real-Time Visualization**: Live timeline with smooth curves and interactive bubbles
- **Multi-View Modes**: Timeline, Vertical, and Split views for different analysis needs
- **Smart Clustering**: Automatic event grouping by severity and time proximity
- **Pattern Detection**: Customizable rules engine with keyword matching
- **Multi-Channel Alerts**: Desktop notifications, Discord webhooks, and email alerts
- **Asset Management**: Custom icons and sounds for different event types
- **Performance Optimized**: Handles 10,000+ events smoothly with WebGL acceleration
- **Offline-First**: Works entirely in the browser with local storage

## 🚀 Getting Started

### 📋 Prerequisites

- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+)
- File System Access API support for folder monitoring (Chrome/Edge)
- 2GB+ RAM recommended for large event volumes

### 🔨 Installation

```bash
# Clone the repository
git clone https://github.com/infinition/acidlog.git
cd acidlog

# Open directly in browser
open index.html

# Or serve with any HTTP server
python -m http.server 8080
# Navigate to http://localhost:8080
```

## ⚡ Quick Start

1. **Connect a Folder**: Click "⚙️ Settings" → "Sources" → "📁 Connect a Folder"
2. **Add Log Monitor**: Enter log file path and refresh interval
3. **Configure Rules**: Set up detection patterns in "🔍 Detection"
4. **Watch Events Flow**: Return to main view to see real-time visualization

## 💡 Usage Example

```javascript
// Example log entry (JSON format)
{
  "timestamp": "2024-01-15T10:30:45Z",
  "type": "critical",
  "message": "Unauthorized access attempt detected",
  "source": "/var/log/auth.log",
  "priority": 5
}

// Detection rule configuration
{
  "keywords": "unauthorized,breach,critical",
  "type": "critical",
  "priority": 5,
  "sound": "alert",
  "notify": {
    "desktop": true,
    "discord": true,
    "email": false
  }
}
```

## ⚙️ Configuration

AcidLog stores configuration in `config/config.json`:

- **Detection Rules**: Pattern matching and alert routing
- **Visualization**: Animation speed, smoothing, graph height
- **Notifications**: Webhook URLs, volume, desktop alerts
- **Performance**: Event limits, update frequency

## 🤝 Contributing

We welcome contributions in:
- New visualization modes
- Additional log parsers
- Performance optimizations
- UI/UX improvements
## Star History

## 🌠 Stargazers

<a href="https://www.star-history.com/#infinition/AcidLog&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=infinition/AcidLog&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=infinition/AcidLog&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=infinition/AcidLog&type=Date" />
 </picture>
</a>

## 📜 License

2024 - AcidLog is distributed under the MIT License.
