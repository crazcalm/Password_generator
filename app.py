import flask, flask.views

app = flask.Flask(__name__)

app.secret_key = "asndkva;vb ;v vvfvk v ffv464v16fv16fv1"

class Page1(flask.views.MethodView):
	def get(self):
		
		return flask.render_template("base.html")

	def post(self):
		
		test = flask.request.form

		for key, value in test.iteritems():
			print key, value
		
		flask.flash(test)
		#return self.get()
		return flask.render_template("post.html")

	
app.add_url_rule("/Password_Generator", view_func=Page1.as_view("base"),
				methods=["GET", "POST"])

if __name__ == "__main__":
	app.debug = True
	app.run()
