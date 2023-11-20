class MelonMusic:
    def __init__(self):
        self.domain = 'https://www.melon.com'
        self.url = ''
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None

    def set_url(self,url):
        self.url = requests.get(f'{self.domain}/{url}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls = soup.find_all(name='p', attrs=({"class":'title'}))
        for i in ls:
            self.title_ls.append(i.find("a").text)
        return self.title_ls

def get_ranking(self):
    soup = BeautifulSoup(self.url, 'lxml')
    ls1 = soup.find_all(name='p', attrs=({"class": 'artist'}))
    for i in ls1:
        self.artist_ls.append(i.find("a").text)
    return self.artist_ls

    def insert_dict(self):
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')