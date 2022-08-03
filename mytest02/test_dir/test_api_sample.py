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

    