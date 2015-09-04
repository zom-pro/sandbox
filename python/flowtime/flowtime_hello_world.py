from bottle import route, run, static_file

@route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>title</title>
            <!--<script src='static/flowtime.js'></script>-->
        </head>
        <body>
        hellou!
        </body>
    </html>

    
    
    
    '''
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080)