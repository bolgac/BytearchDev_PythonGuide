# Folder Size Analyzer

A Python-based tool for **file management and system monitoring**.  
It calculates the total size of a directory tree, provides an extension-based size distribution, and offers a simple CLI interface for quick analysis.

---

## Features
- Compute total folder size in multiple units: **B, KB, MB, GB, TB**
- Extension-based distribution with percentages
- Auto-formatting of sizes into human-readable units
- CLI interface with arguments for path, unit, and detail flag
- Error handling for inaccessible files (skips unreadable files)
- Helper function for analyzing specific file types (e.g., `.py`, `.txt`)
- Built-in usage examples for quick testing

---

## Requirements
- Python **3.9+**
- Standard libraries: `os`, `argparse`, `pathlib`, `typing`
- Works cross-platform: **Windows, macOS, Linux**

---

## Installation

Clone the repository:
```bash
git clone https://github.com/<username>/Python-Guides.git
cd Python-Guides/FolderSizeAnalyzer

Run the analyzer:
python folder_size_analyzer.py /path/to/folder --unit MB --detail


Examples:
```
# Analyze current directory
python folder_size_analyzer.py .

# Analyze with detailed file type distribution
python folder_size_analyzer.py . --unit GB --detail

# Get size of specific file types (Python files)
python folder_size_analyzer.py . --detail
```

## Contacts
- Blog: [Bytearch Dev](https://bytearch.hashnode.dev)
- Telegram: [@bytearchdev](https://t.me/bytearchdev)
- Email: [BytearchDEV](bytearchsoft@gmail.com)
- GitHub: [@bolgac](https://github.com/bolgac/)
