from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import PropertyForm
from app.models import Property
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'app/static/uploads'

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            file = form.photo.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            property = Property(
                title=form.title.data,
                description=form.description.data,
                bedrooms=form.bedrooms.data,
                bathrooms=form.bathrooms.data,
                location=form.location.data,
                price=form.price.data,
                property_type=form.property_type.data,
                photo=filename
            )

            db.session.add(property)
            db.session.commit()

            flash('Property successfully added!', 'success')
            return redirect(url_for('properties'))
        else:
            flash_errors(form)

    return render_template('add_property.html', form=form)

@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)
    
@app.route('/properties/<int:id>')
def property_detail(id):
    property = Property.query.get_or_404(id)
    return render_template('property.html', property=property)

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
