import os
from datetime import timedelta, datetime, date
from flask_migrate import Migrate
from flask import Flask, render_template, redirect, url_for, session, flash, request, get_flashed_messages, jsonify,send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, func
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename, send_from_directory
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SelectField, TextAreaField, IntegerField, FileField, SubmitField, PasswordField, \
    BooleanField, DecimalField, FloatField
from wtforms.validators import InputRequired, DataRequired, Length, Email
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user
from flask_login import login_required
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask import Blueprint
import uuid

def generate_product_id():

    return str(uuid.uuid4())


app = Flask(__name__)


app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.config['UPLOAD_FOLDER_1'] = r'C:\Users\Hp\PycharmProjects\24-04-2000\static\products_image'
app.config['UPLOAD_FOLDER_2'] = r'C:\Users\Hp\PycharmProjects\24-04-2000\static\images'
app.config['UPLOAD_FOLDER_3'] = r'C:\Users\Hp\PycharmProjects\24-04-2000\instance'

db = SQLAlchemy(app)
admin_db = SQLAlchemy()
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired(), Length(max=20)])

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])

class RemoveProductForm(FlaskForm):
    product_id = SelectField('Product', coerce=int, validators=[DataRequired()])
    submit_remove = SubmitField('Remove Product')

custom_admin = Blueprint('custom_admin', __name__)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_text = db.Column(db.Text, nullable=False)
    contact = db.Column(db.Boolean, nullable=False)
    research_group = db.Column(db.Boolean, nullable=False)



# Initialize Flask-Admin
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3', url='/admin')

# Define Flask-Admin ModelView for your ADMIN model
class AdminModelView(ModelView):
    pass  # Customize this class as needed

# Add the Flask-Admin ModelView to the admin instance


app.config['ADMIN_DATABASE_URI'] = 'sqlite:///AdminDatabase.db'
migrate_admin = Migrate(app, admin_db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class ADMIN(db.Model, UserMixin):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"ADMIN('{self.username}', '{self.email}')"

admin.add_view(AdminModelView(ADMIN, db.session, name='UniqueAdminPanel', endpoint='admin_panel'))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    custom_shirts = db.relationship('CustomShirt', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



class ProductModelView(ModelView):
    column_list = ('title', 'content', 'price', 'image_url', 'description')
    column_searchable_list = ('title', 'content', 'description')
    form_excluded_columns = ('id',)

class CustomShirt(db.Model):
    __tablename__ = 'custom_shirt'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Add this line
    username = db.Column(db.String(100), nullable=False)
    shirt_style = db.Column(db.String(50), nullable=False)
    fabric_type = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    fit = db.Column(db.String(20), nullable=False)
    sleeve_length = db.Column(db.String(20), nullable=False)
    neckline = db.Column(db.String(20), nullable=False)
    pattern = db.Column(db.String(100))
    embroidery = db.Column(db.String(100))
    additional_features = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text)
    address = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    payment = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100))

    def __repr__(self):
        return f"CustomShirt('{self.username}', '{self.shirt_style}', '{self.color}', '{self.size}')"


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=True)
    price = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Product('{self.title}', '{self.price}')"

class PaymentData(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    exp_month = db.Column(db.String(2), nullable=False)
    exp_year = db.Column(db.String(4), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PaymentData(name='{self.name}', email='{self.email}', amount_paid='{self.amount_paid}', payment_date='{self.payment_date}')>"

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.message}', '{self.created_at}')"


class CustomShirtForm(FlaskForm):
    username = StringField('Username')
    shirt_style = SelectField('Shirt Style', choices=[('crew-neck', 'Crew Neck'), ('v-neck', 'V-Neck'), ('polo', 'Polo')])
    fabric_type = SelectField('Fabric Type', choices=[('cotton', 'Cotton'), ('polyester', 'Polyester'), ('blend', 'Blend')])
    sleeve_length = SelectField('Sleeve Length', choices=[('short', 'Short Sleeve'), ('three-quarter', 'Three-Quarter Sleeve'), ('long', 'Long Sleeve')])
    size = SelectField('Size', choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    color = StringField('Color')
    fit = SelectField('Fit', choices=[('slim-fit', 'Slim Fit'), ('regular-fit', 'Regular Fit'), ('relaxed-fit', 'Relaxed Fit')])
    neckline = SelectField('Neckline', choices=[('crew-neck', 'Crew Neck'), ('v-neck', 'V-Neck'), ('polo-collar', 'Polo Collar')])
    pattern = StringField('Pattern/Print')
    embroidery = StringField('Embroidery/Logo')
    additional_features = TextAreaField('Additional Features')
    quantity = IntegerField('Quantity')
    instructions = TextAreaField('Special Instructions')
    address = TextAreaField('Shipping Address')
    email = StringField('Email')
    phone = StringField('Phone')
    payment = SelectField('Payment Method', choices=[('credit-card', 'Credit Card'), ('paypal', 'PayPal'), ('bank-transfer', 'Bank Transfer')])
    image = FileField('Image Upload')
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Sign Up')

# Define the form for admin login
class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class FeedbackForm(FlaskForm):
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    contact = BooleanField('I may be contacted about this feedback')
    research_group = BooleanField("I'd like to help improve by joining the Research Group")

class PaymentForm(FlaskForm):
    Name = StringField('Full Name', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired()])
    Address = StringField('Address', validators=[DataRequired()])
    City = StringField('City', validators=[DataRequired()])
    State = SelectField('State', choices=[('','Choose State..'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Telangana', 'Telangana'), ('Rajasthan', 'Rajasthan'), ('Hariyana', 'Hariyana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('West Bengal', 'West Bengal'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Delhi', 'Delhi'), ('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Maharashtra', 'Maharashtra'), ('Bihar', 'Bihar'), ('Odisha', 'Odisha'), ('Meghalaya', 'Meghalaya'), ('Tripura', 'Tripura'), ('Manipur', 'Manipur')])
    ZipCode = IntegerField('Zip Code')
    CardNumber = StringField('Credit Card Number')
    ExpMonth = StringField('Expiry Month')
    ExpYear = SelectField('Expiry Year', choices=[('','Choose Year..')] + [(str(year), str(year)) for year in range(2022, 2040)])
    CVV = IntegerField('CVV')
    AmountPaid = DecimalField('Amount Paid', places=2)
    submit = SubmitField('Proceed to Checkout')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    try:
        # Fetch products from the database
        products = Product.query.all()
        return render_template('index.html', products=products)
    except Exception as e:
        print("Error fetching products:", e)
        return "An error occurred while fetching products."


@app.route('/get_products')
def get_products():
    # Fetch products from the database
    products = Product.query.all()

    # Convert product objects to dictionaries
    products_data = [{
        'title': product.title,
        'imageUrl': product.image_url,
        'Description': product.description,
        'price': product.price
    } for product in products]

    # Return product data as JSON
    return jsonify({'products': products_data})

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        # Check if username or email already exists
        existing_user = User.query.filter(db.or_(User.username == username, User.email == email)).first()
        if existing_user:
            flash('Username or Email already exists!', 'error')
            return redirect(url_for('register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('registration.html')

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid password. Please try again.', 'error')
        else:
            flash('User not found. Please register.', 'error')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        session.clear()
        flash('Logout successful!', 'success')
    return redirect(url_for('login'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/custom_shirt', methods=['GET', 'POST'])
def custom_shirt():

        print("Current user:", current_user)
        form = CustomShirtForm()
        if request.method == 'POST':
            print("Form data:", request.form)
            print("File data:", request.files)
            if 'image' in request.files:
                image = request.files['image']
                print("Image filename:", image.filename)
                if image.filename != '':
                    filename = secure_filename(image.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER_3'], filename)
                    image.save(image_path)
                    print("Image saved to:", image_path)

                    # Save form data to the database
                    custom_shirt = CustomShirt(
                        user_id=current_user.id,
                        username=current_user.username,
                        shirt_style=request.form['shirt-style'],
                        fabric_type=request.form['fabric-type'],
                        sleeve_length=request.form['sleeve-length'],
                        size=request.form['size'],
                        color=request.form['color'],
                        fit=request.form['fit'],
                        neckline=request.form['neckline'],
                        pattern=request.form['pattern'],
                        embroidery=request.form['embroidery'],
                        additional_features=request.form['additional-features'],
                        quantity=request.form['quantity'],
                        instructions=request.form['instructions'],
                        address=request.form['address'],
                        email=request.form['email'],
                        phone=request.form['phone'],
                        payment=request.form['payment'],
                        image=image_path
                    )

                    db.session.add(custom_shirt)
                    db.session.commit()
                    flash('Your custom shirt details have been submitted successfully!', 'success')
                    return redirect(url_for('index'))
                else:
                    flash('No image uploaded!', 'error')
            else:
                flash('Image field not found!', 'error')
        return render_template('customShirt.html', form=form)

@app.route('/shoppingCart')
def shoppingCart():
    return render_template('shoppingCart.html')

@app.route('/paymentGetway',methods=['GET','POST'])
def paymentGetway():
    form = PaymentForm()
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        address = request.form['Address']
        city = request.form['City']
        zip_code = request.form['ZipCod']
        card_number = request.form['Cardnum']
        exp_month = request.form['Month']
        exp_year = request.form['Year']
        cvv = request.form['CVV']

        amount_paid = request.form['AmountPaid']  # Retrieve amount_paid directly from the form

        new_payment = PaymentData(name=name, email=email, address=address, city=city,
                                  zip_code=zip_code, card_number=card_number, exp_month=exp_month,
                                  exp_year=exp_year, cvv=cvv, amount_paid=amount_paid)

        db.session.add(new_payment)
        db.session.commit()

        return redirect(url_for('index'))

def fetch_amount_paid_from_database():
    payment = PaymentData.query.first()
    if payment:
        return payment.amount_paid
    else:
        return 0

def fetch_amount_paid_from_database():
    payment = PaymentData.query.first()
    if payment:
        return payment.amount_paid
    else:
        return 0

@app.route('/contact',methods=['GET','POST'])
def contact():
    form= ContactForm()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        new_contact = Contact(name=name, email=email, message=message)

        db.session.add(new_contact)
        db.session.commit()

        flash('Your message has been submitted successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    form = FeedbackForm()
    if request.method == 'POST' :
        feedback_data = Feedback(
            feedback_text=form.feedback.data,
            contact=form.contact.data,
            research_group=form.research_group.data
        )
        db.session.add(feedback_data)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('feedback.html', form=form)



@app.route('/admin_signup', methods=['GET', 'POST'])
def admin_signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Get form data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        role = form.role.data

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('admin_signup'))

        # Check if the user role is admin
        if role != 'admin':
            flash('Only admins can sign up using this form', 'error')
            return redirect(url_for('admin_signup'))

        # Check if the username or email is already registered
        if ADMIN.query.filter_by(username=username).first() or ADMIN.query.filter_by(email=email).first():
            flash('Username or email already exists', 'error')
            return redirect(url_for('admin_signup'))

        # Create a new user with hashed password
        hashed_password = generate_password_hash(password)
        new_user = ADMIN(username=username, email=email, password=hashed_password, role=role)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully', 'success')
        return redirect(url_for('admin_login'))

    # If it's a GET request, render the sign-up form
    return render_template('signup_admin.html', form=form)

# Admin login route
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Check if username and password match
        username = form.username.data
        password = form.password.data

        user = ADMIN.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful', 'success')
            session['username'] = username  # Storing username in session
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('admin-login.html', form=form)

# Dashboard route
@app.route('/admin', methods=['GET', 'POST'])
def dashboard():
    username = session.get('username')
    current_date = date.today().strftime("%Y-%m-%d")
    if not username:
        flash('Please log in to access this page', 'error')
        return redirect(url_for('admin_login'))
    return render_template('dashboard.html', username=username , current_date=current_date)

# @app.route('/get_product_data')
# def get_product_data():
#     products = Product.query.all()
#     for item in card_data:
#         product = Product(
#             title=item['title'],
#             content=item.get('content', None),
#             price=item['price'],
#             image_url=item.get('image_url', None),  # Adjusted attribute name
#             description=item.get('Description', None)  # Adjusted key name
#
#         )
#         db.session.add(product)
#
#         # Add the Product object to the database session
#         db.session.add(product)
#
#     # Commit the changes to the database
#     db.session.commit()

@app.route('/manage_categories', methods=['GET', 'POST'])
def manage_categories():
    products = Product.query.all()
    remove_product_form = RemoveProductForm()
    remove_product_form.product_id.choices = [(product.id, product.title) for product in products]

    product_images_1 = os.listdir(app.config['UPLOAD_FOLDER_1'])

    product_images_2 = os.listdir(app.config['UPLOAD_FOLDER_2'])

    # Process form submissions for removing a product
    if remove_product_form.validate_on_submit():
        product_id = remove_product_form.product_id.data
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            flash('Product removed successfully!', 'success')
        else:
            flash('Product not found!', 'error')
        return redirect(url_for('manage_categories'))

    return render_template('manage_categories.html', products=products, remove_product_form=remove_product_form,
                           product_images_1=product_images_1, product_images_2=product_images_2)

def is_product_image(filename):
    # Define the list of extensions for product images
    product_image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    # Check if the filename extension is in the list of product image extensions
    return os.path.splitext(filename)[1].lower() in product_image_extensions


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        image = request.files['image']
        content = request.form['content']

        if not title or not description or not price or not image:
            flash("Missing required fields", 'error')
            return redirect(url_for('add_product'))

        # Create the products_image directory if it doesn't exist
        if not title or not description or not price or not image:
            flash("Missing required fields", 'error')
            return redirect(url_for('add_product'))

            # Create the products_image directory if it doesn't exist
        if not os.path.exists(app.config['UPLOAD_FOLDER_1']):
            os.makedirs(app.config['UPLOAD_FOLDER_1'])

            # Create the images directory if it doesn't exist
        if not os.path.exists(app.config['UPLOAD_FOLDER_2']):
            os.makedirs(app.config['UPLOAD_FOLDER_2'])

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            if is_product_image(filename):  # Check if the image is a product image
                image_path = os.path.join(app.config['UPLOAD_FOLDER_1'], filename)
            else:
                image_path = os.path.join(app.config['UPLOAD_FOLDER_2'], filename)  # For non-product images
            image.save(image_path)

            # Store the full image path in the database
            full_image_path = 'products_image/' + filename if is_product_image(filename) else 'images/' + filename

            # Create a new product with the full image path
            new_product = Product(
                title=title,
                description=description,
                price=price,
                image_url=full_image_path,
                content = content
            )

            db.session.add(new_product)
            db.session.commit()

            flash('Product added successfully!', 'success')
            return redirect(url_for('manage_categories'))

    return render_template('add_product.html', form=form)


@app.route('/get_recent_orders/<int:num_items>')
def get_recent_orders(num_items):
    payments = PaymentData.query.order_by(PaymentData.payment_date.desc()).limit(num_items).all()
    payment_data = [{'product_name': payment.name, 'product_number': payment.id, 'payment': payment.amount_paid, 'status': 'Pending'} for payment in payments]
    return jsonify(payment_data)

@app.route('/manage_order')
def manage_order():
    payments = PaymentData.query.order_by(asc(PaymentData.id)).all()
    total_amount = db.session.query(func.sum(PaymentData.amount_paid)).scalar()

    for index, payment in enumerate(payments, start=1):
        payment.id = index

        # Commit the changes to the database
    db.session.commit()
    return render_template('manage_order.html' , payments=payments, total_amount=total_amount)


@app.route('/manage_customers')
def manage_customers():
    customers = User.query.all()
    customers_data = []

    # Iterate through each customer
    for customer in customers:
        # Query associated payments for each customer
        payments = PaymentData.query.filter_by(email=customer.email).all()
        payments_data = []

        # Collect payment details for each payment
        for payment in payments:
            payment_info = {
                'payment_id': payment.id,
                'amount_paid': payment.amount_paid,
                'payment_date': payment.payment_date
            }
            payments_data.append(payment_info)

        # Customer data with associated payments
        customer_info = {
            'id': customer.id,
            'username': customer.username,
            'email': customer.email,
            'payments': payments_data
        }
        customers_data.append(customer_info)

    return render_template('manage_customers.html', customers=customers_data)


@app.route('/customer_details/<int:customer_id>')
def customer_details(customer_id):
    customer = User.query.get(customer_id)
    if customer:
        payment = PaymentData.query.filter_by(email=customer.email).first()

        return render_template('customer_details.html', customer=customer, payment=payment)
    else:
        return "Customer not found"

@app.route('/get_payment')
def get_payment():
    payments = PaymentData.query.all()

    return render_template('get_payment.html', payments=payments)

@app.route('/manage_feedback')
def manage_feedback():
    form = FeedbackForm()
    feedback_entries = Feedback.query.all()
    return render_template('manage_feedback.html', feedback_entries=feedback_entries,form = form)

@app.route('/delete_feedback/<int:feedback_id>', methods=['POST'])
def delete_feedback(feedback_id):
    feedback_entry = Feedback.query.get(feedback_id)
    if feedback_entry:
        db.session.delete(feedback_entry)
        db.session.commit()

        # Update the feedback numbers sequentially
        feedback_entries = Feedback.query.order_by(Feedback.id).all()
        for idx, entry in enumerate(feedback_entries, start=1):
            entry.id = idx

        db.session.commit()

    return redirect(url_for('manage_feedback'))



@app.route('/manage_inquiry')
def manage_inquiry():
    inquiries = Contact.query.all()
    return render_template('manage_inquiry.html', inquiries=inquiries)


@app.route('/admin/delete_inquiry/<int:inquiry_id>', methods=['POST'])
def delete_inquiry(inquiry_id):
    inquiry = Contact.query.get_or_404(inquiry_id)
    db.session.delete(inquiry)
    db.session.commit()
    flash('Inquiry deleted successfully!', 'success')
    return redirect(url_for('manage_inquiry'))

@app.route('/admin/custom_shirt_orders')
def custom_shirt_orders():
    custom_shirts = CustomShirt.query.all()
    return render_template('custom_shirt_orders.html', custom_shirts=custom_shirts)

@app.route('/admin/custom_shirt_images/<path:image_name>')
def custom_shirt_images(image_name):
    images_directory = r'C:\Users\Hp\PycharmProjects\24-04-2000\instance'
    return send_file(f"{images_directory}/{image_name}", mimetype='image/jpeg')

@app.route('/admin/custom_shirt_orders/<int:shirt_id>', methods=['DELETE'])
def delete_custom_shirt(shirt_id):
    shirt = CustomShirt.query.get_or_404(shirt_id)
    try:
        # Delete the custom shirt
        db.session.delete(shirt)
        db.session.commit()

        # Delete the associated image file
        if shirt.image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER_3'], shirt.image)
            if os.path.exists(image_path):
                os.remove(image_path)

        return jsonify({'message': 'Custom shirt and associated image deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        error_message = str(e) if str(e) else 'An error occurred while deleting the custom shirt.'
        print(error_message)
        return jsonify({'error': error_message}), 500


@app.route('/admin/report')
def admin_report():
    # User Statistics
    total_users = User.query.count()
    active_users = User.query.filter(User.last_login >= func.now() - timedelta(days=7)).count() if hasattr(User,
                                                                                                           'last_login') else 0  # Adjusted query
    new_users_today = User.query.filter(func.date(User.created_at) == func.current_date()).count() if hasattr(User,
                                                                                                              'created_at') else 0  # Adjusted query

    # Product Management
    total_products = Product.query.count()
    new_products_today = Product.query.filter(func.date(Product.created_at) == func.current_date()).count() if hasattr(
        Product, 'created_at') else 0  # Adjusted query

    # Payment Summary
    total_revenue = db.session.query(func.sum(PaymentData.amount_paid)).scalar() or 0
    total_transactions = PaymentData.query.count()

    # Feedback and Inquiries
    total_feedback = Feedback.query.count()
    total_inquiries = Contact.query.count()

    return render_template('admin_report.html',
                           total_users=total_users,
                           active_users=active_users,
                           new_users_today=new_users_today,
                           total_products=total_products,
                           new_products_today=new_products_today,
                           total_revenue=total_revenue,
                           total_transactions=total_transactions,
                           total_feedback=total_feedback,
                           total_inquiries=total_inquiries)


# Register your ADMIN model with Flask-Admin
admin.add_view(AdminModelView(ADMIN, db.session, name='UniqueAdminPanel', endpoint='unique_admin_panel'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
