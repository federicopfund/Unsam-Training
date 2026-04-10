"""Alternative image sorting utility with enhanced features.

Provides additional functionality for image management and processing.
"""

import logging
import sys
import os
import datetime
from pathlib import Path
from typing import List, Tuple, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_image_metadata(filepath: str) -> Dict:
    """Extract metadata from an image file.
    
    Args:
        filepath: Path to the image file.
    
    Returns:
        Dictionary with file metadata.
    """
    try:
        stat_info = os.stat(filepath)
        modification_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
        
        return {
            'name': os.path.basename(filepath),
            'size': stat_info.st_size,
            'created': datetime.datetime.fromtimestamp(stat_info.st_ctime),
            'modified': modification_time,
            'path': filepath
        }
    except Exception as e:
        logger.error(f"Error getting metadata for {filepath}: {e}")
        return {}


def organize_images_by_date(
    root_path: str,
    source_folder: str = 'ordenar'
) -> Dict[str, List[str]]:
    """Organize images into groups by modification date.
    
    Args:
        root_path: Root directory to search.
        source_folder: Subdirectory containing images.
    
    Returns:
        Dictionary mapping dates to lists of image paths.
    """
    date_groups = {}
    source_path = os.path.join(root_path, source_folder)
    
    if not os.path.exists(source_path):
        logger.warning(f"Source path not found: {source_path}")
        return date_groups
    
    logger.info(f"Organizing images from: {source_path}")
    
    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if filename.lower().endswith('.png'):
                filepath = os.path.join(root, filename)
                
                try:
                    metadata = get_image_metadata(filepath)
                    if metadata:
                        date_key = metadata['modified'].strftime('%Y-%m-%d')
                        
                        if date_key not in date_groups:
                            date_groups[date_key] = []
                        
                        date_groups[date_key].append(filepath)
                        logger.debug(f"Grouped {filename} to date {date_key}")
                except Exception as e:
                    logger.error(f"Error organizing {filename}: {e}")
    
    logger.info(f"Organized {sum(len(v) for v in date_groups.values())} images")
    return date_groups


def create_shadow_directory(
    root_path: str,
    date_groups: Dict[str, List[str]],
    output_folder: str = 'images_organized'
) -> None:
    """Create a shadow directory structure organized by date.
    
    Args:
        root_path: Root directory path.
        date_groups: Dictionary of images grouped by date.
        output_folder: Name of the output folder.
    """
    output_path = os.path.join(root_path, output_folder)
    
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            logger.info(f"Created output directory: {output_path}")
        
        for date_key in sorted(date_groups.keys()):
            date_dir = os.path.join(output_path, date_key)
            
            if not os.path.exists(date_dir):
                os.makedirs(date_dir)
                logger.info(f"Created date directory: {date_dir}")
        
    except Exception as e:
        logger.error(f"Error creating shadow directory: {e}")
        raise


def display_image_organization(date_groups: Dict[str, List[str]]) -> None:
    """Display organized image groups.
    
    Args:
        date_groups: Dictionary of images grouped by date.
    """
    if not date_groups:
        print("No images found.")
        return
    
    print("\n" + "="*80)
    print("IMAGES ORGANIZED BY DATE")
    print("="*80 + "\n")
    
    total_images = 0
    for date_key in sorted(date_groups.keys()):
        images = date_groups[date_key]
        print(f"{date_key}: {len(images)} image(s)")
        
        for filepath in images:
            print(f"  - {os.path.basename(filepath)}")
        
        total_images += len(images)
    
    print("\n" + "="*80)
    print(f"TOTAL: {total_images} images")
    print("="*80 + "\n")


def generate_organization_report(
    date_groups: Dict[str, List[str]],
    output_file: str = 'organization_report.txt'
) -> None:
    """Generate a report of image organization.
    
    Args:
        date_groups: Dictionary of images grouped by date.
        output_file: Output filename for the report.
    """
    try:
        with open(output_file, 'w') as f:
            f.write("IMAGE ORGANIZATION REPORT\n")
            f.write("="*80 + "\n\n")
            
            for date_key in sorted(date_groups.keys()):
                images = date_groups[date_key]
                f.write(f"{date_key}: {len(images)} image(s)\n")
                
                for filepath in images:
                    size_kb = os.path.getsize(filepath) / 1024
                    f.write(f"  - {os.path.basename(filepath)} ({size_kb:.2f} KB)\n")
                
                f.write("\n")
            
            total_images = sum(len(v) for v in date_groups.values())
            f.write("="*80 + "\n")
            f.write(f"TOTAL: {total_images} images\n")
        
        logger.info(f"Report generated: {output_file}")
        print(f"Report saved to: {output_file}\n")
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        raise


def main(root_directory: str = '../Data') -> None:
    """Main pipeline for enhanced image organization.
    
    Args:
        root_directory: Root directory to process.
    """
    try:
        logger.info("Starting enhanced image organization pipeline")
        
        # Organize images by date
        date_groups = organize_images_by_date(root_directory, 'ordenar')
        
        if not date_groups:
            logger.warning("No images found to organize")
            print("No images found in the specified directory.")
            return
        
        # Display organization
        display_image_organization(date_groups)
        
        # Create shadow directory structure
        create_shadow_directory(root_directory, date_groups, 'images_organized')
        
        # Generate report
        generate_organization_report(date_groups, 'image_organization_report.txt')
        
        logger.info("Enhanced image organization completed successfully")
        
    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        raise


if __name__ == '__main__':
    try:
        root_path = sys.argv[1] if len(sys.argv) > 1 else '../Data'
        main(root_path)
    except Exception as e:
        logger.error(f"Failed to execute main: {e}")
        sys.exit(1)
