import os
import argparse
from pathlib import Path
from typing import Dict, Tuple

class FolderSizeAnalyzer:
    def __init__(self):
        self.supported_units = {
            'B': 1,
            'KB': 1024,
            'MB': 1024 ** 2,
            'GB': 1024 ** 3,
            'TB': 1024 ** 4
        }
    
    def get_folder_size(self, path: str, unit: str = 'MB') -> Tuple[float, Dict]:
        """
        Calculates the total size of a folder and its subfolders
        
        Args:
            path (str): Folder path to analyze
            unit (str): Return unit ('B', 'KB', 'MB', 'GB', 'TB')
        
        Returns:
            Tuple[float, Dict]: (total_size, file_type_distribution)
        """
        if unit not in self.supported_units:
            raise ValueError(f"Unsupported unit: {unit}. Supported: {list(self.supported_units.keys())}")
        
        total_size = 0
        file_type_distribution = {}
        
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        file_size = os.path.getsize(file_path)
                        total_size += file_size
                        
                        # Update file type distribution
                        file_ext = Path(file).suffix.lower() or '.no_extension'
                        file_type_distribution[file_ext] = file_type_distribution.get(file_ext, 0) + file_size
                        
                    except (OSError, PermissionError):
                        continue
                        
        except Exception as e:
            print(f"Error: {e}")
            return 0, {}
        
        # Unit conversion
        converted_size = total_size / self.supported_units[unit]
        return round(converted_size, 2), file_type_distribution
    
    def format_size(self, size_bytes: int, unit: str = 'MB') -> str:
        """Converts size in bytes into a readable format"""
        if unit == 'auto':
            for unit_name, divisor in reversed(list(self.supported_units.items())):
                if size_bytes >= divisor:
                    return f"{size_bytes / divisor:.2f} {unit_name}"
            return f"{size_bytes} B"
        else:
            return f"{size_bytes / self.supported_units[unit]:.2f} {unit}"
    
    def analyze_file_types(self, file_type_distribution: Dict, unit: str = 'MB') -> None:
        """Analyzes and prints file type distribution"""
        print("\nFile Type Distribution:")
        print("-" * 40)
        
        total_size = sum(file_type_distribution.values())
        divisor = self.supported_units[unit]
        
        for file_type, size in sorted(file_type_distribution.items(), 
                                    key=lambda x: x[1], reverse=True):
            percentage = (size / total_size) * 100
            formatted_size = size / divisor
            print(f"{file_type:>15}: {formatted_size:8.2f} {unit} (%{percentage:5.2f})")

def main():
    analyzer = FolderSizeAnalyzer()
    
    # Process command line arguments
    parser = argparse.ArgumentParser(description='Folder size analysis tool')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Folder path to analyze (default: current directory)')
    parser.add_argument('--unit', '-u', default='MB', 
                       choices=['B', 'KB', 'MB', 'GB', 'TB'],
                       help='Display unit (default: MB)')
    parser.add_argument('--detail', '-d', action='store_true',
                       help='Show detailed file type analysis')
    
    args = parser.parse_args()
    
    # Calculate folder size
    total_size, file_type_distribution = analyzer.get_folder_size(args.path, args.unit)
    
    print(f"Folder: {os.path.abspath(args.path)}")
    print(f"Total Size: {total_size} {args.unit}")
    
    if args.detail and file_type_distribution:
        analyzer.analyze_file_types(file_type_distribution, args.unit)

# Advanced feature: Filtering by specific file types
def get_size_by_filetype(path: str, file_extensions: list) -> float:
    """
    Calculates size based on specific file extensions
    
    Args:
        path (str): Folder path
        file_extensions (list): Extensions to filter ['.py', '.txt', ...]
    
    Returns:
        float: Filtered total size (MB)
    """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in file_extensions):
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, PermissionError):
                    continue
    
    return round(total_size / (1024 * 1024), 2)

if __name__ == "__main__":
    main()

    # Practical usage examples
    print("\n" + "="*50)
    print("Practical Usage Examples:")
    print("="*50)
    
    analyzer = FolderSizeAnalyzer()
    
    # Example 1: Analyze current directory
    size, distribution = analyzer.get_folder_size(".", "MB")
    print(f"1. Current directory size: {size} MB")
    
    # Example 2: Size of Python files
    python_files_size = get_size_by_filetype(".", [".py", ".pyw"])
    print(f"2. Python files size: {python_files_size} MB")
    
    # Example 3: Detailed analysis
    print("\n3. Detailed Analysis:")
    analyzer.analyze_file_types(distribution, "MB")
