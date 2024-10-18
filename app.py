from flask import Flask, render_template ,request ,redirect,url_for

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home_page():
    return render_template('index.html')
# @app.route('/contact',methods=['GET','POST'])
# def conact():
#     if request.method=='POST':
#         name=request.form("Name")
#         email=request.form("Email")
#         Message=request.form("Message")
        
#     return render_template("contact.html")



if __name__=='__main__':
    app.run(debug=True)