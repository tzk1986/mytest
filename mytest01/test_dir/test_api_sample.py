import seldom


class TestRequest(seldom.TestCase):
    """api test case"""
    
    def start(self):
        self.base_url = "http://httpbin.org"
    
    def test_put_method(self):
        self.put(f'{self.base_url}/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post(f'{self.base_url}/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get(f'{self.base_url}/get', params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete(f'{self.base_url}/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main()


"""以下是seldom中简化了selenium中的API，使操作Web页面更加简单"""
import seldom


class TestCase(seldom.TestCase):

    def test_seldom_api(self):
        # Accept warning box.
        self.accept_alert()

        # Adds a cookie to your current session.
        self.add_cookie({'name': 'foo', 'value': 'bar'})

        # Adds a cookie to your current session.
        cookie_list = [
            {'name': 'foo', 'value': 'bar'},
            {'name': 'foo', 'value': 'bar'}
        ]
        self.add_cookie(cookie_list)

        # Clear the contents of the input box.
        self.clear(css="#el")

        # It can click any text / image can be clicked
        # Connection, check box, radio buttons, and even drop-down box etc..
        self.click(css="#el")

        # Mouse over the element.
        self.move_to_element(css="#el")

        # Click the element by the link text
        self.click_text("新闻")

        # Simulates the user clicking the "close" button in the titlebar of a popup window or tab.
        self.close()

        # Delete all cookies in the scope of the session.
        self.delete_all_cookies()

        # Deletes a single cookie with the given name.
        self.delete_cookie('my_cookie')

        # Dismisses the alert available.
        self.dismiss_alert()

        # Double click element.
        self.double_click(css="#el")

        # Execute JavaScript scripts.
        self.execute_script("window.scrollTo(200,1000);")

        # Setting width and height of window scroll bar.
        self.window_scroll(width=300, height=500)

        # Setting width and height of element scroll bar.
        self.element_scroll(css=".class", width=300, height=500)

        # open url.
        self.open("https://www.baidu.com")

        # Gets the text of the Alert.
        self.get_alert_text

        # Gets the value of an element attribute.
        self.get_attribute(css="#el", attribute="type")

        # Returns information of cookie with ``name`` as an object.
        self.get_cookie()

        # Returns a set of dictionaries, corresponding to cookies visible in the current session.
        self.get_cookies()

        # Gets the element to display,The return result is true or false.
        self.get_display(css="#el")

        # Get a set of elements
        self.get_element(css="#el", index=0)

        # Get element text information.
        self.get_text(css="#el")

        # Get window title.
        self.get_title

        # Get the URL address of the current page.
        self.get_url

        # Set browser window maximized.
        self.max_window()

        # Mouse over the element.
        self.move_to_element(css="#el")

        # open url.
        self.open("https://www.baidu.com")

        # Quit the driver and close all the windows.
        self.quit()

        # Refresh the current page.
        self.refresh()

        # Right click element.
        self.right_click(css="#el")

        # Saves a screenshots of the current window to a PNG image file.
        self.screenshots()  # Save to HTML report
        self.screenshots('/Screenshots/foo.png')  # Save to the specified directory

        # Saves a element screenshot of the element to a PNG image file.
        self.element_screenshot(css="#id")  # Save to HTML report
        self.element_screenshot(css="#id", file_path='/Screenshots/foo.png')  # Save to the specified directory

        """
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.
        <select name="NR" id="nr">
            <option value="10" selected="">每页显示10条</option>
            <option value="20">每页显示20条</option>
            <option value="50">每页显示50条</option>
        </select>
        """
        self.select(css="#nr", value='20')
        self.select(css="#nr", text='每页显示20条')
        self.select(css="#nr", index=2)

        # Set browser window wide and high.
        self.set_window(100, 200)

        # Submit the specified form.
        self.submit(css="#el")

        # Switch to the specified frame.
        self.switch_to_frame(css="#el")

        # Returns the current form machine form at the next higher level.
        # Corresponding relationship with switch_to_frame () method.
        self.switch_to_frame_out()

        # Switches focus to the specified window.
        # This switches to the new windows/tab (0 is the first one)
        self.switch_to_window(1)

        # Operation input box.
        self.type(css="#el", text="selenium")

        # Implicitly wait.All elements on the page.
        self.wait(10)

        # Setting width and height of window scroll bar.
        self.window_scroll(width=300, height=500)

    