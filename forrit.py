from bottle import *
import os

@error(404)
def villa(error):
    return"þessi síða er ekki til "

@route('/')
def index():
    return '''
            <h2>Þetta er aðal siðan</h2>
            <h3><a href="a">liður a</a> <a href="b">liður b</a> </h3>
            '''

@route('/a')
def a():
    return '''
<h3>Verkefni 2A</h3>
<h2><a href="ab/1">liður 1</a> <a href="ab/2">liður 2</a> <a href="ab/3">liður 3</a></h2>
    <h1><a href="/">Til baka</a></h1>
'''
@route('/ab/<id>')
def ab(id):
    return '<h2>þetta er liður ' + id +'</h2>'+ '<h1><a href="/a">Til baka</a></h1>'
        

@route('/b')
def b():
    return '''
<h2>Verkefni 2B</h2>
        <a href="ba"><img src="pix/mynda.jpg"></a>
        <a href="ba"><img src="pix/myndb.jpg"></a>
        <a href="ba"><img src="pix/myndc.jpg"></a>
'''
@route('/pix/<filename>')
def server_static(filename):
    return static_file(filename, root="./pix")

@route('/ba/<id>')
def ba(id):
    return '<h2>þetta er bókstafurinn ' + id +'</h2>'+ '<h1><a href="/b">Til baka</a></h1>'

run(host='0.0.0.0', port=os.environ.get('PORT'))
#run(host='localhost', port=8080)


    
