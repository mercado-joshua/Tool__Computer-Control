import pyautogui

class Automation:
    # Planning Your Mouse Movements
    def mouse_info(self):
        pyautogui.mouseInfo()

    def get_screen_size(self):
        self.__dimension = pyautogui.size()
        return self.__dimension

    # Moving the Mouse
    def move_mouse(self, x, y, duration):
        pyautogui.moveTo(x, y, duration)

    def move_mouse_relative_pos(self, x, y, duration):
        pyautogui.move(x, y, duration)

    def get_mouse_current_pos(self):
        return pyautogui.position()

    # Clicking the Mouse
    def set_left_mouse_click(self, x, y):
        pyautogui.click(x, y, button='left')

    def set_middle_mouse_click(self, x, y):
        pyautogui.click(x, y, button='middle')

    def set_right_mouse_click(self, x, y):
        pyautogui.click(x, y, button='right')

    def push_mouse_button_down(self):
        pyautogui.mouseDown()

    def release_mouse_button_up(self):
        pyautogui.mouseUp()

    def left_mouse_doubleclick(self):
        pyautogui.doubleClick()

    def left_mouse_click(self):
        pyautogui.click()

    def right_mouse_click(self):
        pyautogui.rightClick()

    def middle_mouse_click(self):
        pyautogui.middleClick()

    # Dragging the Mouse
    def drag_mouse(self, x, y, duration):
        pyautogui.drag(x, y, duration)

    def drag_mouse_relative_pos(self, x, y, duration):
        pyautogui.dragTo(x, y, duration)

    # Scrolling the Mouse
    def mouse_scroll(self, units):
        pyautogui.scroll(units)

    # Working with the Screen
    def get_screenshot(self):
        return pyautogui.screenshot()

    def get_rgb_color(self, x, y):
        return pyautogui.pixel((x, y))

    def is_pixel_matches_color(self, x, y, rgb):
        return pyautogui.pixelMatchesColor(x, y, rgb)

    # Image Recognition - a slow and fragile way to find things on the screen
    def get_image_screen_coordinates(self, image_path):
        try:
            return pyautogui.locateOnScreen(image_path)
        except:
            return 'Image could not be found.'

    def get_images_screen_coordinates(self, image_path):
        try:
            return list(pyautogui.locateAllOnScreen(image_path))
        except:
            return 'Image could not be found.'

    # Getting Window Information
    def get_active_window(self):
        """Returns the Window object for the window that is currently receiving keyboard focus."""
        self.__active_window = pyautogui.getActiveWindow()
        return self

    def get_all_windows(self):
        """Returns a list of Window objects for every visible window on the screen."""
        return pyautogui.getAllWindows()

    def get_windows_at(self, x, y):
        """Returns a list of Window objects for every visible window that includes the point (x, y)."""
        return pyautogui.getWindowsAt(x, y)

    def get_windows_with_title(self, title):
        """Returns a list of Window objects for every visible window that includes the string title in its title bar."""
        return pyautogui.getWindowsWithTitle(title)

    def get_all_titles(self):
        """ Returns a list of strings of every visible window."""
        return pyautogui.getAllTitles()

    # Manipulating Windows
    def aw_maximize(self):
        """Maximizes the window."""
        self.__active_window.maximize()
        return self

    def aw_minimized(self):
        """Minimizes the window."""
        self.__active_window.minimize()
        return self

    def aw_close(self):
        """This will close the window you're typing in."""
        self.__active_window.close()

    def aw_restore(self):
        """Undoes a minimize/maximize action."""
        self.__active_window.restore()
        return self

    def is_aw_maximized(self):
        """Returns True if window is maximized."""
        return self.__active_window.isMaximized

    def is_aw_minimized(self):
        """Returns True if window is minimized."""
        return self.__active_window.isMinimized

    def is_aw_active(self):
        """Returns True if window is the active window."""
        return self.__active_window.isActive

    #---------------------------------------------------------
    @property
    def aw_width(self):
        """Gets the current width of the window."""
        return self.__active_window.width

    @aw_width.setter
    def aw_width(self, width):
        """Sets the current width of the window."""
        self.__active_window.width = width

    @property
    def aw_title(self):
        return self.__active_window.title

    @aw_title.setter
    def aw_title(self, title):
        self.__active_window.title = title

    @property
    def aw_size(self):
        return self.__active_window.size

    @aw_size.setter
    def aw_size(self, size):
        self.__active_window.size = size

    @property
    def aw_top(self):
        return self.__active_window.top

    @aw_top.setter
    def aw_top(self, top):
        self.__active_window.top = top

    @property
    def aw_left(self):
        return self.__active_window.left

    @aw_left.setter
    def aw_left(self, left):
        self.__active_window.left = left

    @property
    def aw_bottom(self):
        return self.__active_window.bottom

    @aw_bottom.setter
    def aw_bottom(self, bottom):
        self.__active_window.bottom = bottom

    @property
    def aw_right(self):
        return self.__active_window.right

    @aw_right.setter
    def aw_right(self, right):
        self.__active_window.right = right

    @property
    def aw_topleft(self):
        """Gets the current position of the window."""
        return self.__active_window.topleft

    @aw_topleft.setter
    def aw_topleft(self, topleft):
        """Sets the current position of the window."""
        self.__active_window.topleft = topleft

    @property
    def aw_area(self):
        return self.__active_window.area

    @aw_area.setter
    def aw_area(self, area):
        self.__active_window.area = area

    # Controlling the Keyboard
    def write_text_from_keyboard(self, text, pause=0):
        pyautogui.write(text, pause)

    # Pressing and Releasing the Keyboard
    def press_key_down(self, key_name):
        self.__key = pyautogui.keyDown(str(key_name))
        return self

    def press_key(self, key_name):
        self.__key = pyautogui.press(str(key_name))
        return self

    def release_key_up(self, key_name):
        self.__key = pyautogui.keyUp(str(key_name))
        return self

    def hot_key(self, *key_names):
        """Combination of keypresses to invoke some application function."""
        self.__key = pyautogui.hotkey(*key_names)
        return self

    # Message Box
    def messagebox_alert(self, text, title='This is a message.'):
        pyautogui.alert(title, text)

    def messagebox_prompt(self, text):
        pyautogui.prompt(text)

    def messagebox_confirm(self, text):
        pyautogui.confirm(text)

    def messagebox_password(self, text):
        pyautogui.password()

def main():
    a = Automation()
    # print(a.get_screen_size())

    # for _ in range(11):
    #     a.move_mouse(100, 100, 0.25)
    #     a.move_mouse(200, 100, 0.25)
    #     a.move_mouse(200, 200, 0.25)
    #     a.move_mouse(100, 200, 0.25)

    # for _ in range(11):
    #     a.move_mouse_relative_pos(100, 0, 0.25) # right
    #     a.move_mouse_relative_pos(0, 100, 0.25) # down
    #     a.move_mouse_relative_pos(-100, 0, 0.25) # up
    #     a.move_mouse_relative_pos(0, -100, 0.25) # left

    # print(a.get_mouse_current_pos())

    # a.right_mouse_click(10, 5)
    # a.left_mouse_click()

    # distance = 300
    # change = 20
    # while distance > 0:
    #     a.drag_mouse(distance, 0, 0.2) # Move right.
    #     distance = distance - change
    #     a.drag_mouse(0, distance, 0.2) # Move down.
    #     a.drag_mouse(-distance, 0, 0.2) # Move left.
    #     distance = distance - change
    #     a.drag_mouse(0, -distance, 0.2) # Move up.
    # a.left_mouse_click()
    # a.mouse_scroll(2000)

    # a.mouse_info()
    # print(a.get_image_screen_coordinates('Capture.JPG'))
    # print(a.get_active_window().aw_title())

    # print(a.get_active_window().aw_topleft)
    # a.get_active_window().aw_topleft =  (800, 400)

    # text = """
    # The pyautogui.write() function sends virtual keypresses to the computer. What these keypresses do depends on what window is active and what text field has focus. You may want to first send a mouse click to the text field you
    # want in order to ensure that it has focus. As a simple example, let’s use Python to automatically type the words
    # Hello, world! into a file editor window. First, open a new file editor window and position it in the upper-left corner of your screen so that PyAutoGUI will click in the right place to bring it into focus. Next, enter the following into the interactive shell:
    # """
    # a.left_mouse_click()
    # a.write_text_from_keyboard(text, 0.25)

    """
    'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', and so on

    'enter' (or 'return' or '\n')

    'esc'

    'shiftleft', 'shiftright'

    'altleft', 'altright'

    'ctrlleft', 'ctrlright'

    'tab' (or '\t')

    'backspace', 'delete'

    'pageup', 'pagedown'

    'home', 'end'

    'up', 'down', 'left', 'right'

    'f1', 'f2', 'f3', and so on

    'volumemute', 'volumedown', 'volumeup'

    'pause'

    'capslock', 'numlock', 'scrolllock'

    'insert'

    'printscreen'

    'winleft', 'winright' The left and right win keys (on Windows)

    'command' The Command key (on macOS)
    'option' The option key (on macOS)
    """

    # text = ['a', 'b', 'left', 'left', 'X', 'Y']
    # a.left_mouse_click()
    # a.write_text_from_keyboard(text, 0.25)

    # a.press_key_down('shift').press_key('4').release_key_up('shift')
    # a.hot_key('ctrl', 'a')

    a.messagebox_alert('hello world')

if __name__ == '__main__':
    main()