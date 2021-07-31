from flask import Flask, render_template

posts = [
    {
        'author': 'author 1',
        'title': 'blogpost 1',
        'content': 'first post content ',
        'date_posted': '21-02-23'       
    },
     {
        'author': 'author 2',
        'title': 'blogpost 3',
        'content': 'second post content ',
        'date_posted': '21-03-23'       
    }



]


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html', posts=posts)



@app.route("/about")
def about():
        return render_template('about.html', title='About')




if __name__ == '__main__':
    app.run(debug=True)