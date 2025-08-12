from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/blogs')
def blogs():
    blog_list = [
        {
            "title": "Understanding Flask Basics",
            "author": "Alice",
            "snippet": "Learn the fundamentals of Flask for web development...",
            "featured": True
        },
        {
            "title": "Advanced Jinja2 Templating",
            "author": "Bob",
            "snippet": "Take your Jinja2 skills to the next level with these tips...",
            "featured": False
        },
        {
            "title": "Deploying Flask Apps",
            "author": "Charlie",
            "snippet": "Step-by-step guide on deploying your Flask app to production...",
            "featured": True
        }
    ]
    return render_template('layout/blogs.html', blogs=blog_list)

if __name__ == "__main__":
    app.run(debug=True)
