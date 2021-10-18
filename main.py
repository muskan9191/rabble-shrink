from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from flask import Flask, render_template,request, session, url_for, flash,g
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
from werkzeug.utils import secure_filename, redirect
import os
from flask_mail import Mail, Message
import smtplib
app = Flask(__name__)

with open('config.json',"r") as C:
    params = json.load(C)["params"]

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = params['email']
app.config['MAIL_PASSWORD'] = params['password']
app.config['MAIL_USE_SSL'] = True
amail = Mail(app)


db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = params['database']
app.config['UPLOAD_FOLDER'] = params['upload_folder']
app.secret_key = params['secretkey']

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    uname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)

class Merchant(db.Model):
    merchant_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    gst_no = db.Column(db.Integer, nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    uname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)

class Productlist(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    img_name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    merchant_id = db.Column(db.Integer, foreign_key=True)

class Feedback(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(10), nullable=False)
    merchant_id = db.Column(db.Integer, foreign_key=True)
    order_id = db.Column(db.String(30), foreign_key=True)

class Category(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), nullable=False)
    merchant_id = db.Column(db.Integer, foreign_key=True)

class Orderplaced(db.Model):
    order_id = db.Column(db.String(30), primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    cust_name = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(30),nullable=False)
    merchant_id = db.Column(db.Integer, foreign_key=True)
    status = db.Column(db.String(20), nullable=False)

class Orderproducts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(30), primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.before_request
def before_request():
    g.mer = None
    g.user = None
    if 'username' in session:
        user = Users.query.filter_by(uname=session['username']).first()
        g.user= user
    if 'mname' in session:
        mer = Merchant.query.filter_by(uname=session['mname']).first()
        g.mer = mer

@app.route("/")
def home():
    if('username' in session and session['username'] == g.user.uname):
        return redirect(url_for('userpage',user_id=g.user.user_id))
    return render_template("index.html")

# *************************
# user
# *************************

@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        gender = request.form.get('gender')
        uname = request.form.get('uname')
        mail = request.form.get('mail')
        password = request.form.get('password')
        confirm = request.form.get('cfpwd')
        phone = request.form.get('phone')
        address = request.form.get('address')
        pincode = request.form.get('pincode')
        users = Users.query.all()
        for user in users:
            if(uname==user.uname):
                flash("Username not available try a different one","danger")
                return redirect(url_for('register'))
            if(mail==user.mail):
                flash("Email id not available try a different one", "danger")
                return redirect(url_for('register'))
            #print(f" <username={user.uname}>") this line help us to print the value between the sentence
        body = "Hi " + fname + " " + lname + ", Heartly Welcome to Online Grocery Shopping." +  "," + "\n\n" + " Verify you mail id by clicking on the below link." \
               + "\n http://127.0.0.1:5000/verification " + "\n Please Do not reply to this mail."
        msg = MIMEMultipart()
        msg['From'] = params['email']
        msg['To'] = mail
        msg['Subject'] = 'Email Verification by Online Grocery Shopping'
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        text = msg.as_string()
        server.login(params['email'], params['password'])
        server.sendmail(params['email'], mail, text)
        server.quit()

        if password == confirm:
            reg = Users(fname=fname,lname=lname,gender=gender, uname=uname,mail=mail,password=password,phone=phone,address=address,pincode=pincode)
            db.session.add(reg)
            db.session.commit()
            return redirect(url_for('verify'))
            # flash("Registered Successfully", "success")
            # return redirect(url_for('user_login'))
        else:
            flash("Password does not match", "danger")
            return redirect(url_for('register'))
    return render_template("register.html")

@app.route("/verify")
def verify():
    return render_template("verify.html")

@app.route("/verification")
def verification():
    return render_template("verification.html")

@app.route("/user_login",methods=["GET", "POST"])
def user_login():
    if('username' in session and session['username'] == g.user.uname):
        log = Users.query.filter_by(uname=g.user.uname).first()
        user_id = log.user_id
        return redirect(url_for('userpage',user_id=user_id))
    if request.method == "POST":
        uname = request.form.get('uname')
        password = request.form.get('password')
        logg = Users.query.filter_by(uname=uname,password=password).first()
        if logg:
            session['username'] = uname
            user_id = logg.user_id
            cart = {}
            session['cart'] = cart
            return redirect(url_for('userpage',user_id=user_id))
        else:
            flash("The Email and Password does not match our records", "danger")
            return redirect(url_for('user_login'))
    return render_template("userlogin.html")

@app.route("/userlogout")
def userlogout():
    session.pop('username')
    session.pop('cart')
    return redirect(url_for('user_login'))

@app.route("/userpage/<string:user_id>")
def userpage(user_id):
    if not g.user:
        return redirect(url_for('user_login'))
    logg = Users.query.filter_by(user_id=user_id).first()
    mer =  Merchant.query.filter_by(pincode=logg.pincode).all()
    return render_template("userpage.html",merchants = mer)

@app.route("/myorders",methods=["GET", "POST"])
def myorders():
    if not g.user:
        return redirect(url_for('user_login'))
    orders = Orderplaced.query.filter_by(user_id=g.user.user_id).all()
    merchants = []
    for order in orders:
        id = order.merchant_id
        merchants.append(Merchant.query.filter_by(merchant_id =id).first())
    if request.method == "POST":
        feedback = request.form.get('feedback')
        desc = request.form.get('desc')
        mid = request.form.get('mid')
        oid = request.form.get('oid')
        pro = Feedback(feedback=feedback,description=desc,merchant_id=mid,order_id=oid)
        db.session.add(pro)
        db.session.commit()
        return redirect(url_for('myorders'))
    return render_template("myorders.html",packed = zip(merchants,orders))

@app.route("/products/<string:order_id>")
def products(order_id):
    if not g.user:
        return redirect(url_for('user_login'))
    order = Orderplaced.query.filter_by(order_id = order_id).first()
    productss = []
    pro_db = Orderproducts.query.filter_by(order_id=order_id).all()
    for pro in pro_db:
        id = pro.product_id
        productss.append(Productlist.query.filter_by(product_id=id).first())
    return render_template("products.html",order=order,packed = zip(productss,pro_db))

@app.template_filter('is_in_cart')
def is_in_cart(product):
    c = session['cart']
    k = c.keys()
    for id in k:
        if int(id) == product.product_id:
            return c.get(id)
    return 0

@app.route("/shop/<string:merchant_id>",methods=["GET", "POST"])
def shop(merchant_id):
    if not g.user:
        return redirect(url_for('user_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    products = Productlist.query.filter_by(merchant_id=merchant_id).all()
    if request.method == "POST":
        pid = request.form.get('pid')
        remove = request.form.get('minus')
        carts = session['cart']
        if carts:
            quantity = carts.get(pid)
            if quantity:
                if remove:
                    if(quantity<=1):
                        del carts[pid]
                    else:
                        carts[pid] = quantity - 1
                else:
                    carts[pid] = quantity + 1
            else:
                carts[pid] = 1
        else:
            carts = {}
            carts[pid] = 1
        session['cart'] = carts
        return redirect(url_for('shop',merchant_id=merchant_id))
    return render_template("shop.html",products=products,merchant=mer)

@app.route("/cart/<string:user_id>/<string:merchant_id>",methods=["GET", "POST"])
def cart(user_id,merchant_id):
    if not g.user:
        return redirect(url_for('user_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    cart = session['cart']
    has_items = bool(cart)
    if has_items:
        keys = cart.keys()
        products = []
        quantities = []
        total = 0
        for id in keys:
            products.append(Productlist.query.filter_by(product_id=id).first())
            quantities.append(cart.get(id))
        print(products)
        packed = zip(products,quantities)
        for product, quantity in packed:
            total = total + (quantity * product.price)
        return render_template("cart.html",merchant=mer,packed = zip(products,quantities),total=total)
    else:
        return render_template("emptycart.html", merchant=mer)

def pushcart(order_id):
    cart = session['cart']
    keys = cart.keys()
    products = []
    quantities = []
    for id in keys:
        products.append(Productlist.query.filter_by(product_id=id).first())
        quantities.append(cart.get(id))
    packed = zip(products, quantities)
    for product, quantity in packed:
        pro = Orderproducts(order_id=order_id, product_id=product.product_id , quantity=quantity)
        db.session.add(pro)
        db.session.commit()
    session['cart'] = {}

@app.route("/buynow/<string:merchant_id>",methods=["GET", "POST"])
def buynow(merchant_id):
    if not g.user:
        return redirect(url_for('user_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    cart = session['cart']
    keys = cart.keys()
    products = []
    quantities = []
    total = 0
    for id in keys:
        products.append(Productlist.query.filter_by(product_id=id).first())
        quantities.append(cart.get(id))
    packed = zip(products, quantities)
    for product, quantity in packed:
        total = total + (quantity * product.price)
    if request.method == "POST":
        order_id = "ORD-" + merchant_id + str(random.randint(10000, 99999)) + str(random.randint(10000000, 99999999))
        name = request.form.get('name')
        date = datetime.now()
        peca = Orderplaced(order_id=order_id,user_id=g.user.user_id, cust_name=name, amount=total, date=date,merchant_id=merchant_id,status = "Placed")
        db.session.add(peca)
        db.session.commit()
        pushcart(order_id)
        return redirect(url_for('order', merchant_id=merchant_id, order_id=order_id))
    return render_template("buynow.html" , merchant = mer , amt=total)


@app.route("/order/<string:merchant_id>/<string:order_id>")
def order(merchant_id,order_id):
    if not g.user:
        return redirect(url_for('user_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    order = Orderplaced.query.filter_by(order_id=order_id).first()
    return render_template("order.html",merchant=mer,order=order)


# *************************
# merchant
# *************************

@app.route("/merchant_register",methods=["GET", "POST"])
def merchantregister():
    if request.method == "POST":
        shop_name = request.form.get('shop_name')
        gst_no = request.form.get('gst_no')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        gender = request.form.get('gender')
        uname = request.form.get('uname')
        address = request.form.get('address')
        password = request.form.get('password')
        phone = request.form.get('phone')
        confirm = request.form.get('cfpwd')
        pincode = request.form.get('pincode')
        Merchants = Merchant.query.all()
        for user in Merchants:
            if(uname==user.uname):
                flash("Username not available try a different one", "danger")
                return redirect(url_for('merchantregister'))
        if password == confirm:
            reg = Merchant(shop_name=shop_name,gst_no=gst_no,fname=fname,lname=lname,gender=gender, uname=uname,password=password,phone=phone,address=address,pincode=pincode)
            db.session.add(reg)
            db.session.commit()
            flash("Registered Successfully","success")
            return redirect(url_for('merchant_login'))
        else:
            flash("Password does not match", "danger")
            return redirect(url_for('merchantregister'))
    return render_template("merchantregister.html")

@app.route("/merchant_login",methods=["GET", "POST"])
def merchant_login():
    if request.method == "POST":
        uname = request.form.get('uname')
        password = request.form.get('password')
        logg = Merchant.query.filter_by(uname=uname,password=password).first()
        if logg:
            session['mname'] = uname
            return redirect(url_for('merchantdashboard',merchant_id=logg.merchant_id))
        else:
            flash("The Email and Password does not match our records", "danger")
            return redirect(url_for('merchant_login'))
    return render_template("merchantlogin.html")

@app.route("/merchantlogout")
def merchantlogout():
    session.pop('mname',None)
    return redirect(url_for('merchant_login'))

@app.route("/merchant_dashboard/<string:merchant_id>",methods=["GET", "POST"])
def merchantdashboard(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    orders = Orderplaced.query.filter_by(merchant_id=merchant_id).all()
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    if request.method == "POST":
        oid = request.form.get('oid')
        ord = Orderplaced.query.filter_by(order_id=oid).first()
        if ord.status == "Placed":
            ord.status = "Ready"
        elif ord.status == "Ready":
            ord.status = "Completed"
        db.session.commit()
        return render_template("merchantdashboard.html", mercha=logg, orders=orders)
    return render_template("merchantdashboard.html",mercha=logg,orders=orders)

@app.route("/completedorders/<string:merchant_id>")
def completedorders(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    orders = Orderplaced.query.filter_by(merchant_id=merchant_id).all()
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    return render_template("completed_orders.html",mercha=logg,orders=orders)

@app.route("/feedback/<string:merchant_id>")
def feedback(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    feed = Feedback.query.filter_by(merchant_id=merchant_id).all()
    return render_template("feedback.html",mercha=logg,feedback=feed)


@app.route("/orderproducts/<string:order_id>")
def mer_orderproducts(order_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=g.mer.merchant_id).first()
    order = Orderplaced.query.filter_by(order_id = order_id).first()
    productss = []
    pro_db = Orderproducts.query.filter_by(order_id=order_id).all()
    for pro in pro_db:
        id = pro.product_id
        productss.append(Productlist.query.filter_by(product_id=id).first())
    return render_template("mer_orderproducts.html",mercha=logg,order=order,packed = zip(productss,pro_db))


@app.route("/productlist/<string:merchant_id>")
def productlist(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    product = Productlist.query.filter_by(merchant_id=merchant_id).all()
    return render_template("productlist.html",products=product,mercha=logg)

@app.route("/addproducts/<string:merchant_id>",methods=["GET", "POST"])
def addproducts(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    categories = Category.query.filter_by(merchant_id=merchant_id).all()
    if request.method == "POST":
        product_name = request.form.get('pname')
        category = request.form.get('category')
        price = request.form.get('price')
        unit = request.form.get('unit')
        quantity = request.form.get('quantity')
        f = request.files['pimage']
        deca = Productlist.query.filter_by(product_name = product_name,merchant_id=merchant_id).first()
        if deca is None:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            peca = Productlist(product_name=product_name, category=category, quantity=quantity, unit=unit, img_name=f.filename, price=price,merchant_id=merchant_id)
            db.session.add(peca)
            db.session.commit()
            flash("Uploaded Successfully", "success")
            return redirect(url_for('addproducts',merchant_id =merchant_id ))
        else:
            deca.quantity = int(deca.quantity) + int(quantity)
            db.session.commit()
            flash("Uploaded Successfully", "success")
            return render_template("addproducts.html",mercha=logg)
    return render_template("addproducts.html",categories=categories,mercha=logg)

@app.route("/addcategory/<string:merchant_id>",methods=["GET", "POST"])
def addcategory(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    categories = Category.query.filter_by(merchant_id=merchant_id).all()
    if request.method == "POST":
        category = request.form.get('cname')
        catego = Category.query.all()
        for cate in catego:
            if(category == cate.category and merchant_id == cate.merchant_id):
                flash("Category Already Available", "danger")
                return redirect(url_for('addcategory',merchant_id=merchant_id ))
        deca = Category(category = category , merchant_id=merchant_id)
        db.session.add(deca)
        db.session.commit()
        flash("Category Added Successfully", "success")
        return redirect(url_for('addcategory',merchant_id=merchant_id ))
    return render_template("addcategory.html",categories=categories,mercha=logg)

@app.route("/editproduct/<string:merchant_id>",methods=["GET", "POST"])
def editproduct(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    product = Productlist.query.filter_by(merchant_id=merchant_id).all()
    return render_template("editproduct.html",products=product,mercha=logg)

@app.route("/editform/<string:merchant_id>/<string:product_id>",methods=["GET", "POST"])
def editform(merchant_id,product_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    categories = Category.query.filter_by(merchant_id=merchant_id).all()
    pro = Productlist.query.filter_by(product_id=product_id).first()
    if request.method == "POST":
        product_name = request.form.get('pname')
        category = request.form.get('category')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        pro.product_name = product_name
        pro.category = category
        pro.price = price
        pro.quantity = quantity
        db.session.commit()
        flash("Updated Successfully", "success")
        return redirect(url_for('editform',merchant_id =merchant_id,product_id=pro.product_id ))
    return render_template("editform.html",categories=categories,mercha=logg,product=pro)

@app.route("/deleteproduct/<string:merchant_id>",methods=["GET", "POST"])
def deleteproduct(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    logg = Merchant.query.filter_by(merchant_id=merchant_id).first()
    product = Productlist.query.filter_by(merchant_id=merchant_id).all()
    if request.method == "POST":
        pid = request.form.get('pid')
        pro = Productlist.query.filter_by(product_id=pid).first()
        db.session.delete(pro)
        db.session.commit()
        return redirect(url_for('deleteproduct', merchant_id=merchant_id))
    return render_template("deleteproduct.html",products=product,mercha=logg)

@app.route("/personal_info/<string:merchant_id>",methods=["GET", "POST"])
def personal_info(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    if request.method == "POST":
        return redirect(url_for('edit_personalinfo', merchant_id=merchant_id))
    return render_template("personal_info.html",mercha=mer)

@app.route("/edit_personalinfo/<string:merchant_id>",methods=["GET", "POST"])
def edit_personalinfo(merchant_id):
    if not g.mer:
        return redirect(url_for('merchant_login'))
    mer = Merchant.query.filter_by(merchant_id=merchant_id).first()
    if request.method == "POST":
        shop_name = request.form.get('shop_name')
        business_type = request.form.get('business_type')
        gst_no = request.form.get('gst_no')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        uname = request.form.get('uname')
        phone = request.form.get('phone')
        address = request.form.get('address')
        pincode = request.form.get('pincode')
        mer.shop_name = shop_name
        mer.business_type = business_type
        mer.gst_no = gst_no
        mer.fname = fname
        mer.lname = lname
        mer.uname = uname
        mer.phone = phone
        mer.address = address
        mer.pincode = pincode
        db.session.commit()
        flash("Updated Successfully", "success")
        return redirect(url_for('edit_personalinfo',merchant_id = merchant_id))
    return render_template("edit_personalinfo.html",mercha=mer)


if __name__=="__main__":
    app.run(debug=True)