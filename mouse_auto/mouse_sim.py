import pyautogui
import time

def simulate_mouse_actions():
    # Allow some time to switch to the target application
    print("Starting mouse simulation in 3 seconds. Please prepare your screen.")
    time.sleep(3)
    
    # Move the mouse to (100, 200) over 0.2 seconds
    print("Moving swiftly to (100, 200)")
    pyautogui.moveTo(100, 200, duration=0.2)
    
    # Simulate a right-click at the current position
    print("Right clicking at (100, 200)")
    pyautogui.rightClick()
    
    # Wait a moment before next action
    time.sleep(0.5)
    
    # Move the mouse to (200, 300) and perform a double click over 0.2 seconds
    print("Moving swiftly to (200, 300) and double clicking")
    pyautogui.moveTo(200, 300, duration=0.2)
    pyautogui.doubleClick()
    
    # Wait a moment before drag action
    time.sleep(0.5)
    
    # Drag from the current location (200, 300) to (400, 400) over 0.2 seconds
    print("Dragging swiftly from (200, 300) to (400, 400)")
    pyautogui.dragTo(400, 400, duration=0.2, button='left')
    
if __name__ == '__main__':
    simulate_mouse_actions()
