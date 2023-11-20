class Melon :
    def __init__(self):
        self.domain='https://www.melon.com'
        self.url = ''
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None

    def set_url(self, url):
        self.url = f'{self.domain}/{url}'

        def get_url(self):

if __name__ == '__main__':
    m = Melon()
    m
    url = input('크롤링 대상 url 을 입력하시오.')
    b.set_url(url)
    # https://www.melon.com/chart/index.htm?dayTime=
    b.set_url(url)
    u2 = b.__init__()

    print(f'당신이 원하는 url 은 {u2} 입니다.')

