from flask import Flask,request
app = Flask(__name__)


@app.route('/')
@app.route('/hello',methods=['POST'])
def HelloWorld():
	if request.method == 'POST':
		tes = request.data
		print (tes)
		return tes
	else:
		return "Hello wdfckydg World"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)