from livereload import Server

server = Server()

server.watch('/Users/egorsemin/Practice/video-player-jslib-master/*.html')
server.watch('/Users/egorsemin/Practice/video-player-jslib-master/*.css')
server.watch('/Users/egorsemin/Practice/video-player-jslib-master/*.js')

server.serve(root='/Users/egorsemin/Practice/video-player-jslib-master', default_filename='index2.html')
