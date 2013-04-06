# eptccrawler.py

from BeautifulSoup import BeautifulSoup

import crawling


places_str = 'http://www.eptc.com.br/EPTC_Itinerarios/Linha.asp?cdEmp='
companies = { "Unibus" : 23, "Conorte" : 21, "STS" : 22, "Carris" : 3 }


bus_places_str1 = 'http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp?Linha='
bus_places_str2 = '&Tipo=I&Veiculo=1&Sentido=0&Logradouro=0&Action=Itiner%E1rio'


class EptcCrawler(crawling.RouteCrawler):
    """ Crawls bus routes from the EPTC's website, which controls the traffic
        in Porto Alegre """

    def __init__(self):
        super(EptcCrawler, self).__init__()

    def crawl(self):
        self._crawl_places()

    def _crawl_places(self):
        """ Takes the places the buses pass by """
        for company, c_id in companies.iteritems():
            places_html = crawling.get_url(places_str)
            print places_html

            s = BeautifulSoup(places_html)
            l = s.findAll('option')

            # Makes a list of all the possible different route names
            q_list = []
            for q in l:
                q_list.append(q['value'])

            # crawls over the places lists and return the divs
            for q in q_list:
                places_list_html = crawling.get_url(bus_places_str1 + str(q) +
                                                    bus_places_str2)

                print places_list_html

                places_soup = BeautifulSoup(places_list_html)
                l_query = places_soup.findAll(lambda tag: len(tag.name) == 1)
                for l in l_query:
                    print l

a = EptcCrawler()
a.crawl()

