"""Life duration calculator.

Calculates the total seconds a person has lived based on their birth date.
"""

import logging
from datetime import date
from typing import Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_birth_date() -> Tuple[int, int, int]:
    """Get birth date from user input.
    
    Returns:
        Tuple of (year, month, day).
    """
    try:
        day = int(input("Enter day of birth: "))
        month = int(input("Enter month of birth: "))
        year = int(input("Enter year of birth: "))
        
        # Validate input
        birth_date = date(year, month, day)
        logger.info(f"Birth date received: {birth_date}")
        
        return year, month, day
    except ValueError as e:
        logger.error(f"Invalid date input: {e}")
        raise


def calculate_life_duration(birth_date: Tuple[int, int, int]) -> float:
    """Calculate total seconds lived since birth.
    
    Args:
        birth_date: Tuple of (year, month, day).
    
    Returns:
        Total seconds lived as float.
    """
    try:
        year, month, day = birth_date
        birth_date_obj = date(year=year, month=month, day=day)
        today = date.today()
        
        # Calculate days lived
        time_elapsed = today - birth_date_obj
        seconds_lived = time_elapsed.total_seconds()
        
        logger.info(f"Calculated life duration: {seconds_lived:.0f} seconds")
        
        return seconds_lived
    except ValueError as e:
        logger.error(f"Error calculating life duration: {e}")
        raise


def display_life_statistics(birth_date: Tuple[int, int, int]) -> None:
    """Display comprehensive life statistics.
    
    Args:
        birth_date: Tuple of (year, month, day).
    """
    try:
        year, month, day = birth_date
        birth_date_obj = date(year=year, month=month, day=day)
        today = date.today()
        
        # Calculate various time units
        time_elapsed = today - birth_date_obj
        days_lived = time_elapsed.days
        seconds_lived = time_elapsed.total_seconds()
        hours_lived = seconds_lived / 3600
        minutes_lived = seconds_lived / 60
        weeks_lived = days_lived / 7
        months_lived = days_lived / 30.44  # Average month length
        years_lived = days_lived / 365.25  # Account for leap years
        
        # Display statistics
        print("\n" + "="*50)
        print("LIFE STATISTICS")
        print("="*50)
        print(f"Birth Date: {birth_date_obj.strftime('%B %d, %Y')}")
        print(f"Today: {today.strftime('%B %d, %Y')}")
        print("-"*50)
        print(f"Years lived: {years_lived:.2f}")
        print(f"Months lived: {months_lived:.0f}")
        print(f"Weeks lived: {weeks_lived:.0f}")
        print(f"Days lived: {days_lived}")
        print(f"Hours lived: {hours_lived:.0f}")
        print(f"Minutes lived: {minutes_lived:.0f}")
        print(f"Seconds lived: {seconds_lived:.0f}")
        print("="*50 + "\n")
        
        logger.info("Life statistics displayed successfully")
        
    except Exception as e:
        logger.error(f"Error displaying statistics: {e}")
        raise


def main() -> None:
    """Main pipeline for life duration calculation."""
    try:
        logger.info("Starting life duration calculator")
        
        # Get birth date from user
        birth_date = get_birth_date()
        
        # Calculate and display duration
        seconds_lived = calculate_life_duration(birth_date)
        print(f"\nSeconds of life: {seconds_lived:.0f}")
        
        # Display comprehensive statistics
        display_life_statistics(birth_date)
        
        logger.info("Life duration calculation completed successfully")
        
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise


if __name__ == "__main__":
    main()
