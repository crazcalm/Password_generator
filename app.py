import flask, flask.views
import web_script

app = flask.Flask(__name__)

app.secret_key = "asndkva;vb ;v vvfvk v ffv464v16fv16fv1"

class Page1(flask.views.MethodView):
	def get(self):
		
		return flask.render_template("base.html")

	def post(self):
		
		test = flask.request.form

		special_char, pass_len = [x for x in test.itervalues()]		

		print pass_len, special_char

		password = web_script.main(int(pass_len), special_char)

		#return password
		return flask.render_template("post.html", password = password)

	
app.add_url_rule("/Password_Generator", view_func=Page1.as_view("base"),
				methods=["GET", "POST"])

if __name__ == "__main__":
	app.debug = True
	app.run()
