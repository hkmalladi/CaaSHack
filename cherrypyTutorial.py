import random
import string

import cherrypy


class StringGenerator(object):

    cherrypy.config.update({
                           'server.socket_host':'10.2.27.124',
                           'server.socket_port': 8082,
                           })

    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self, skus=[], index=0):
        skus = skus.split(',')
        l = skus[int(index)]
        return l

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
