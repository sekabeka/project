import json


from module_cookies import run


class CookiesAuchan:



    def __init__(self):
        self.result = run()
        self.length = len(self.result)
        self.set = True
        self.lst = self.MyGenerator()

    def MyGenerator(self):
        count = 0
        while True:
            for cookies, proxy in self.result:
                if count == 2000:
                    self.result = run()
                    count = 0
                    break
                yield cookies, proxy
                count = count + 1
        
    def process_request(self, request, spider):
        if self.set is not None:
            spider.custom_settings['COUCURRENT_REQUESTS']  = self.length * 5  
            spider.custom_settings['CONCURRENT_REQUEST_PER_DOMAIN']  = self.length  * 2    
            self.set = None
        request.cookies, request.meta['proxy'] = next(self.lst)
        return None
    
    def process_response(self, request, response, spider):
        if response.status == 401:
            return request
        return response

        
