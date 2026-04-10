"""Image listing utility for PNG files.

Recursively scans a directory to locate all PNG images and displays them.
"""

import logging
import sys
import os
from pathlib import Path
from typing import List
import pprint

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def traverse_and_list_images(root_path: str) -> List[str]:
    """Recursively traverse directory and find all PNG images.
    
    Args:
        root_path: Root directory to start traversal.
    
    Returns:
        List of absolute paths to PNG files found.
    """
    image_files = []
    
    logger.info(f"Scanning directory: {root_path}")
    
    try:
        for root, dirs, files in os.walk(root_path):
            for filename in files:
                if filename.lower().endswith('.png'):
                    filepath = os.path.join(root, filename)
                    image_files.append(filepath)
                    logger.debug(f"Found: {filepath}")
        
        logger.info(f"Found {len(image_files)} PNG image(s)")
        
    except PermissionError as e:
        logger.error(f"Permission denied accessing directory: {e}")
        raise
    except Exception as e:
        logger.error(f"Error traversing directory: {e}")
        raise
    
    return image_files


def get_image_stats(image_files: List[str]) -> dict:
    """Get statistics about found images.
    
    Args:
        image_files: List of image file paths.
    
    Returns:
        Dictionary with image statistics.
    """
    if not image_files:
        return {'total_images': 0, 'directories': set()}
    
    directories = set()
    file_sizes = {}
    
    for filepath in image_files:
        directory = os.path.dirname(filepath)
        directories.add(directory)
        
        try:
            file_size = os.path.getsize(filepath)
            file_sizes[filepath] = file_size
        except OSError as e:
            logger.warning(f"Could not get size for {filepath}: {e}")
    
    return {
        'total_images': len(image_files),
        'unique_directories': len(directories),
        'directories': directories,
        'total_size_bytes': sum(file_sizes.values()) if file_sizes else 0,
        'average_file_size': sum(file_sizes.values()) / len(file_sizes) if file_sizes else 0
    }


def display_images(image_files: List[str], show_stats: bool = True) -> None:
    """Display list of images in a formatted manner.
    
    Args:
        image_files: List of image file paths.
        show_stats: Whether to display statistics.
    """
    if not image_files:
        logger.warning("No images found")
        print("No PNG images found in the specified directory.")
        return
    
    print("\n" + "="*80)
    print("PNG IMAGES FOUND")
    print("="*80 + "\n")
    
    pprint.pprint(image_files)
    
    if show_stats:
        stats = get_image_stats(image_files)
        
        print("\n" + "="*80)
        print("STATISTICS")
        print("="*80)
        print(f"Total images found: {stats['total_images']}")
        print(f"Unique directories: {stats['unique_directories']}")
        
        if stats.get('total_size_bytes'):
            size_mb = stats['total_size_bytes'] / (1024 * 1024)
            avg_size_kb = stats.get('average_file_size', 0) / 1024
            print(f"Total size: {size_mb:.2f} MB")
            print(f"Average file size: {avg_size_kb:.2f} KB")
        
        print("="*80 + "\n")


def export_image_list(image_files: List[str], output_file: str = 'image_list.txt') -> None:
    """Export image list to a text file.
    
    Args:
        image_files: List of image file paths.
        output_file: Output filename for the list.
    """
    try:
        with open(output_file, 'w') as f:
            f.write("PNG IMAGES FOUND\n")
            f.write("="*80 + "\n\n")
            for filepath in sorted(image_files):
                f.write(f"{filepath}\n")
            f.write(f"\nTotal: {len(image_files)} images\n")
        
        logger.info(f"Image list exported to {output_file}")
        print(f"Image list saved to: {output_file}\n")
    except Exception as e:
        logger.error(f"Error exporting image list: {e}")
        raise


def main(root_directory: str = '../Data/', export: bool = False) -> None:
    """Main pipeline for image discovery and listing.
    
    Args:
        root_directory: Root directory to scan.
        export: Whether to export results to a file.
    """
    try:
        logger.info("Starting image discovery pipeline")
        
        # Find all PNG images
        image_files = traverse_and_list_images(root_directory)
        
        # Display results
        display_images(image_files, show_stats=True)
        
        # Export if requested
        if export:
            export_image_list(image_files)
        
        logger.info("Image discovery pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        raise


if __name__ == '__main__':
    try:
        root_path = sys.argv[1] if len(sys.argv) > 1 else '../Data/'
        export_results = '--export' in sys.argv or '-e' in sys.argv
        
        main(root_path, export=export_results)
    except Exception as e:
        logger.error(f"Failed to execute main: {e}")
        sys.exit(1)
