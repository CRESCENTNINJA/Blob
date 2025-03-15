import pyautogui
import time
import os

def click_icon(icon_name, confidence=0.6):
    """
    Locate an icon on the screen based on its image file and click it.
    
    Args:
        icon_name (str): The name of the icon (expects an image file named '<icon_name>.png')
        confidence (float): Matching confidence threshold (requires OpenCV)
    
    Returns:
        bool: True if the icon was found and clicked, False otherwise.
    """
    image_file = f"{icon_name}.png"
    
    # Check if the image file exists
    if not os.path.exists(image_file):
        print(f"Image file '{image_file}' not found.")
        return False
    
    print(f"Searching for '{icon_name}' icon on the screen...")
    
    # Attempt to locate the center of the icon on the screen
    location = pyautogui.locateCenterOnScreen(image_file, confidence=confidence)
    
    if location is not None:
        print(f"Found '{icon_name}' at {location}. Clicking...")
        pyautogui.rightClick(location)
        return True
    else:
        print(f"Could not locate the '{icon_name}' icon on the screen.")
        return False

def main():
    # Allow a few seconds to set up your screen if needed
    print("Starting icon clicker. Prepare your screen. You have 3 seconds...")
    time.sleep(3)
    
    while True:
        # Get user input for the icon name
        icon_name = input("Enter the icon name to click (or type 'exit' to quit): ").strip()
        if icon_name.lower() == 'exit':
            break
        
        # Attempt to find and click the icon
        clicked = click_icon(icon_name)
        if clicked:
            print(f"Successfully clicked on '{icon_name}'.")
        else:
            print(f"Failed to click on '{icon_name}'.")
        
        # Optional: small pause before next command
        time.sleep(1)

if __name__ == '__main__':
    main()
