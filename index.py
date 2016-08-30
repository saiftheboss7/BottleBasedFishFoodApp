from bottle import route, request, template, run, post, get, debug
@route('/')
def index():
    return template ('index')

@post('/result', method='POST')
def result():
	sumFish= float(request.forms.get("TotalFish"))
	fishRange= float(request.forms.get("FishRange"))
	
	if 5000<=sumFish<=8000:
		constant=0.00020
	if 4000<=sumFish<=4999:
		constant=0.00019
	if 3000<=sumFish<=3999:
		constant=0.00017

	newvar=constant*fishRange
	

	return template('output', name=newvar)

debug(True)
run(reloader=True)