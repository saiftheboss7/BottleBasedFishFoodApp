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
	if 2000<=sumFish<=2999:
		constant=0.00020
	if 1000<=sumFish<=1999:
		constant=0.00035
	if 800<=sumFish<=899:
		constant=0.00038
	if 500<=sumFish<=599:
		constant=0.00050
	if 400<=sumFish<=499:
		constant=0.00050
	if 300<=sumFish<=399:
		constant=0.00050
	if 100<=sumFish<=299:
		constant=0.00120
	if 75<=sumFish<=99:
		constant=0.00133
	if 50<=sumFish<=74:
		constant=0.00160
	if 40<=sumFish<=49:
		constant=0.00175
	if 25<=sumFish<=39:
		constant=0.00200
	if 15<=sumFish<=24:
		constant=0.00200
	if 10<=sumFish<=14:
		constant=0.00250

	newvar=constant*fishRange
	

	return template('output', name=newvar)

debug(True)
run(reloader=True)