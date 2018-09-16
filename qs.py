

from sys import argv

import bottle
from bottle import*
bottle.debug(True)

@route('/')
def index():
    return template('index.tpl')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./")

@route('/forum')
def display_forum():
    forum_id = request.query.id
    forum_page = request.query.page
    return "id: " + forum_id + "<br>" + "page: " + forum_page


bottle.run(host="0.0.0.0", port=argv[1] )

