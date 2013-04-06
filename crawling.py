# routecrawler.py

# Use Requests to make the crawling of information from the websites
import requests

# We'll define an Abstract Base Class for Bus Routes Crawler classes
import abc

class Route(object):
    """ Stores the information about the bus routes, like what times each bus
        passes where, what bus company it belongs to, etc. """

    def __init__(self, name, city, company, bus_travels, places):
        self.name = name
        # Useful because often many cities have the same Bus Route names
        self.city = city
        self.company = company

        # A list of Buses getting out of a place going into somewhere
        self.bus_travels = bus_travels

        # A list of Places this route passes through
        self.places = places

class Bus(object):
    def __init__(self, dep_time, place_from, place_to, wheelchair_adapted):
        self.dep_time = dep_time
        self.place_from = dep_place
        self.place_to = direction
        self.wheelchair_adapted = wheelchair_adapted

class Place(object):
    def __init__(self, lat, lon, name=""):
        self.lat = lat
        self.lon = lon
        self.name = name

        # A list of the buses that pass here
        self.buses = []


class RouteCrawler(object):
    """ This ABC provides an interface to different web crawlers that take
        information from different bus company web pages """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.routes = []

    @abc.abstractmethod
    def crawl(self):
        """ 'Feeds' the class with the website information """
        return


def get_url(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        print "check the url"


