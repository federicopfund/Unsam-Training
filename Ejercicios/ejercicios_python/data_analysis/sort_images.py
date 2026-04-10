"""Image file sorting and renaming utilities.

Recursively traverses a directory, detects PNG images with date patterns,
and renames them with their modification timestamps.
"""

import logging
import sys
import os
import datetime
from pathlib import Path
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def is_valid_image_date_format(filename: str) -> bool:
    """Check if filename matches date pattern (name_YYYYMMDD.png).
    
    Args:
        filename: Name of the file to check.
    
    Returns:
        True if filename matches date pattern, False otherwise.
    """
    if not filename.endswith('.png'):
        return False
    
    # Check for underscore and 8 digits before .png
    if len(filename) >= 13 and filename[-13] == '_':
        try:
            date_str = filename[-12:-4]
            # Try to parse as date
            datetime.datetime.strptime(date_str, '%Y%m%d')
            return True
        except ValueError:
            return False
    
    return False


def extract_date_from_filename(filename: str) -> datetime.datetime:
    """Extract date from filename.
    
    Args:
        filename: Filename in format name_YYYYMMDD.png
    
    Returns:
        datetime object representing the date.
    """
    date_str = filename[-12:-4]
    try:
        return datetime.datetime.strptime(date_str, '%Y%m%d')
    except ValueError as e:
        logger.error(f"Error extracting date from {filename}: {e}")
        raise


def sort_and_rename_images(
    root_path: str,
    source_folder: str = 'ordenar'
) -> List[str]:
    """Recursively find PNG images and rename them with timestamps.
    
    Walking through the specified directory, detects images matching the
    pattern 'name_YYYYMMDD.png', extracts the date, and updates the file
    modification timestamp accordingly.
    
    Args:
        root_path: Root directory to search.
        source_folder: Subdirectory containing images to process.
    
    Returns:
        List of processed files.
    """
    processed_files = []
    source_path = os.path.join(root_path, source_folder)
    
    if not os.path.exists(source_path):
        logger.warning(f"Source path not found: {source_path}")
        return processed_files
    
    logger.info(f"Processing images from: {source_path}")
    
    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if filename.endswith('.png'):
                filepath = os.path.join(root, filename)
                
                try:
                    if is_valid_image_date_format(filename):
                        # Extract date and set modification time
                        image_date = extract_date_from_filename(filename)
                        timestamp = image_date.timestamp()
                        
                        # Update file modification time
                        os.utime(filepath, (timestamp, timestamp))
                        
                        # Rename file (remove the date part)
                        new_name = filename[:-13] + '.png'
                        new_filepath = os.path.join(root, new_name)
                        
                        # Only rename if names are different
                        if new_filepath != filepath:
                            os.rename(filepath, new_filepath)
                            logger.info(f"Renamed: {filename} -> {new_name}")
                            processed_files.append(new_filepath)
                        else:
                            processed_files.append(filepath)
                    else:
                        logger.warning(
                            f"File {filename} does not match expected "
                            "format (name_YYYYMMDD.png)"
                        )
                except Exception as e:
                    logger.error(f"Error processing {filename}: {e}")
    
    logger.info(f"Processed {len(processed_files)} image(s)")
    return processed_files


def create_output_directory(root_path: str, output_folder: str = 'imgs_procesadas') -> str:
    """Create output directory for processed images.
    
    Args:
        root_path: Root directory where to create the output folder.
        output_folder: Name of the output folder.
    
    Returns:
        Path to the created or existing output directory.
    """
    output_path = os.path.join(root_path, output_folder)
    
    try:
        if not os.path.exists(output_path):
            os.mkdir(output_path)
            logger.info(f"Created output directory: {output_folder}")
            print(f"Created directory: {output_path}\n")
        else:
            logger.info(f"Output directory already exists: {output_folder}")
            print(f"Directory already exists: {output_path}\n")
    except FileExistsError:
        logger.info(f"Output directory already exists: {output_folder}")
    except Exception as e:
        logger.error(f"Error creating output directory: {e}")
        raise
    
    return output_path


def main(root_directory: str = '../Data') -> None:
    """Main pipeline for image sorting and renaming.
    
    Args:
        root_directory: Root directory containing images to process.
    """
    try:
        logger.info("Starting image sorting pipeline")
        
        # Create output directory
        output_dir = create_output_directory(root_directory, 'imgs_procesadas')
        
        # Process images
        processed_files = sort_and_rename_images(root_directory, 'ordenar')
        
        if processed_files:
            logger.info(f"Successfully processed {len(processed_files)} files")
            print(f"Processed files: {processed_files}")
        else:
            logger.warning("No images were processed")
        
        logger.info("Image sorting pipeline completed successfully")
        
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
