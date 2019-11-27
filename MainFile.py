from flask import Flask,render_template,request,flash,redirect,url_for
from Databases import User

app = Flask(__name__)
app.secret_key = "bnvsdnvsfvdvkvnjvdvdkbvdsc"



@app.route('/view')
def show():
    users = User.select()
    return render_template('vieusers.html', users = users)


@app.route('/',methods=['GET','POST'])
def register():
    if request.method == "POST":
        names = request.form["names"]
        email = request.form["email"]
        password = request.form["password"]
        User.create(names = names, email = email, password = password)
        flash("Account Created Successfully")
    return render_template("register.html")



@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    user = User.get(User.id==id)
    if request.method == "POST":
        names = request.form["name"]
        mail = request.form["email"]
        passwd = request.form["pass"]
        user.names = names
        user.email = mail
        user.password = passwd
        user.save()
        flash("User Updated Successfully")
        return redirect(url_for('show'))
    return render_template("update.html",user = user)


@app.route('/delete/<int:id>')
def delete(id):
    User.delete().where(User.id == id).execute()
    flash("Details Deleted Successfully")
    return redirect(url_for('show'))



if __name__ == '__main__':
    app.run()










